import asyncio
import mido
import pandas as pd
import dataclasses
from pathlib import Path
import music21
from collections import defaultdict
import enum
from typing import List, NamedTuple, Optional
import numpy as np


class MidiEventType(enum.Enum):
    NOTE_ON = 1
    NOTE_OFF = 2


@dataclasses.dataclass
class MidiEvent:
    midi_event_type: MidiEventType
    note: int
    time: float


def to_piano_roll(midi_file_path: str, resolution: int = 256) -> None:
    midi_file = mido.MidiFile(midi_file_path)

    filtered_messages: List[MidiEvent] = []

    # message: mido.messages.messages.Message
    for message in midi_file:
        match message.type:
            case "note_on":
                filtered_messages.append(
                    MidiEvent(
                        midi_event_type=MidiEventType.NOTE_ON,
                        note=message.note,
                        time=message.time,
                    )
                )
            case "note_off":
                filtered_messages.append(
                    MidiEvent(
                        midi_event_type=MidiEventType.NOTE_OFF,
                        note=message.note,
                        time=message.time,
                    )
                )

    print(filtered_messages[0:100])
    pass


class QuantizedValue(NamedTuple):
    quantized_value: int
    scaled_value: float

def quantize(value, in_min, in_max, steps: int, out_min=0.0, out_max=1.0) -> QuantizedValue:
    normalized_value = (value - in_min) / (in_max - in_min)
    scaled_value = np.floor(normalized_value*steps) / steps
    quantized_value = (scaled_value * (out_max - out_min)) + out_min
    return QuantizedValue(
        quantized_value=int(quantized_value),
        scaled_value=scaled_value,
    )

class PianoRoll:
    def __init__(self, midi_file_path: str):
        self._midi_file_path = midi_file_path
        self.midi_file = mido.MidiFile(self._midi_file_path)
        self.tempo = self.get_tempo()

    def get_tempo(self) -> Optional[float]:
        for msg in self.midi_file:
            if msg.type == "set_tempo":
                return mido.tempo2bpm(msg.tempo)
        return None

    def events(self, hold_notes_with_pedal: bool = False) -> pd.DataFrame:
        """ """
        if hold_notes_with_pedal:
            raise NotImplementedError()

        events = []
        time = 0.0
        for msg in self.midi_file:
            time += msg.time
            if any([x == msg.type for x in ["note_on", "note_off"]]):
                events.append(
                    {
                        "note": msg.note,
                        "velocity": msg.velocity if msg.type == "note_on" else 0,
                        "time": time,
                    }
                )
            # pedal
            elif msg.is_cc(64):
                events.append(
                    {
                        "note": -1,
                        "velocity": msg.value,
                        "time": time,
                    }
                )
        df_events = pd.DataFrame(events)

        return df_events

    def piano_roll(self, fill_empty_notes: bool = True) -> pd.DataFrame:
        events = self.events()
        events = events.pivot_table(
            values="velocity", index="time", columns="note", aggfunc="max"
        )
        events = events.ffill().fillna(0.0)
        events.index = pd.TimedeltaIndex(events.index * 10e8)

        if fill_empty_notes:
            # highest note is 108, but range is excluding upper boundary
            piano_range = set(range(21, 109))
            # check for piano pedal as well
            piano_range.add(-1)
            existing_columns = set(events.columns)
            missing_columns = piano_range - existing_columns # type: ignore
            for missing_column in missing_columns:
                events[missing_column] = 0
            events = events.reindex(sorted(events.columns), axis=1)

        return events

    @staticmethod
    def quantize(value, in_min, in_max, steps: int, out_min=0.0, out_max=1.0) -> QuantizedValue:
        normalized_value = (value - in_min) / (in_max - in_min)
        scaled_value = np.floor(normalized_value*steps) / steps
        quantized_value = (scaled_value * (out_max - out_min)) + out_min
        return QuantizedValue(
            quantized_value=int(quantized_value),
            scaled_value=scaled_value,
        )
    
    def performance_vector(self, num_time_slots: int = 125, num_velocities: int = 32):
        events_df = self.events()

        # create time bins and put events into said bins
        time_slots = np.arange(0.0, np.ceil(events_df['time'].max()), 0.008)
        events_df['time_slot'] = pd.cut(
            events_df['time'],
            bins=time_slots,
            include_lowest=True,
            labels=np.arange(0, len(time_slots)-1),
        ) # type: ignore

        midi_vector = list()
        latest_time_slot = 0

        for time_slot, time_group in events_df.groupby("time_slot", observed=True):
            note_on = np.zeros(shape=(89))
            note_off = np.zeros(shape=(89))
            velocity_vector = np.zeros(shape=(num_velocities))
            time_vector = np.zeros(shape=(num_time_slots))

            velocity = None

            for _, event in time_group.iterrows():
                if event['note'] == -1:
                    midi_note = 88
                else:
                    midi_note = event['note'] - 21
                if event['velocity'] > 0:
                    note_on[int(midi_note)] = 1
                    velocity = event['velocity']
                else:
                    note_off[int(midi_note)] = 1
            
            if velocity:
                velocity_pos = self.quantize(velocity, in_min=0, in_max=127, out_min=0, out_max=31, steps=num_velocities).quantized_value
                velocity_vector[velocity_pos] = 1
            
            time_pos = min(max(0,  time_slot - latest_time_slot), num_time_slots-1)
            time_vector[time_pos] = 1

            midi_vector.append(np.concatenate([
                note_on,
                note_off,
                time_vector,
                velocity_vector,
            ]))
            latest_time_slot = time_slot
        
        return np.array(midi_vector)
    
    def performance_vector_one_hot(self, num_time_slots: int = 125, num_velocities: int = 32, include_pedal: bool = True) -> np.ndarray:
        events_df = self.events()
        vectors = []
        events_df['time_delta'] = events_df['time'].diff(1).fillna(0.0)

        performance_vector_factory = PerformanceVectorFactory(
            num_notes=88,
            num_velocities=num_velocities,
            num_time=num_time_slots,
            include_pedal=include_pedal,
        )

        for _, event in events_df.iterrows():
            vectors.append(performance_vector_factory.time_vector(event['time_delta']))
            if event['velocity'] > 0:
                vectors.append(performance_vector_factory.velocity_vector(event['velocity']))
                vectors.append(performance_vector_factory.note_on_vector(event['note']))
            else:
                vectors.append(performance_vector_factory.note_off_vector(event['note']))
        
        return np.array(vectors)


    def __repr__(self) -> str:
        return f"PianoRoll({self._midi_file_path})"


class MidiPlayer:
    def __init__(self, device_name: str = "MIDILINK-mini") -> None:
        self
        pass

    @staticmethod
    def print_devices(self) -> None:
        pass

    def playback(self, midi_data):
        pass

    async def async_playback(self):
        asyncio.sleep()

    def stop_all(self):
        pass

def quantize(value, in_min, in_max, steps: int, out_min=0.0, out_max=1.0) -> QuantizedValue:
    normalized_value = (value - in_min) / (in_max - in_min)
    scaled_value = np.floor(normalized_value*steps) / steps
    quantized_value = (scaled_value * (out_max - out_min)) + out_min
    return QuantizedValue(
        quantized_value=int(quantized_value),
        scaled_value=scaled_value,
    )

class PerformanceVectorFactory:
    def __init__(self, num_notes: int = 88, num_time=125, num_velocities: int =32, include_pedal: bool = True, midi_note_offset: int = 21) -> None:
        self.num_note_on = num_notes
        self.num_note_off = num_notes
        self.num_time = num_time
        self.num_velocities = num_velocities
        self.include_pedal = include_pedal
        if self.include_pedal:
            self.num_note_on += 1
            self.num_note_off += 1
        self.midi_note_offset = midi_note_offset
    
    def _blank_vector(self) -> np.ndarray:
        return np.zeros(shape=(self.num_note_on + self.num_note_off + self.num_time + self.num_velocities))

    def velocity_vector(self, velocity: int) -> np.ndarray:
        velocity = np.clip(velocity, 0, 127)
        quantized_velocity_num = int(np.round(quantize(
            value=velocity,
            in_min=0,
            in_max=127,
            steps=self.num_velocities,
        ).scaled_value * (self.num_velocities - 1)))
        vector = self._blank_vector()
        vector[self.num_note_on + self.num_note_off + self.num_time + quantized_velocity_num] = 1.0
        return vector

    def time_vector(self, time: float) -> np.ndarray:
        # time in s
        time = np.clip(time, 0, 1.0)
        quantized_time_num = int(np.round(quantize(
            value=time,
            in_min=0,
            in_max=1.0,
            steps=self.num_time,
        ).scaled_value * (self.num_time - 1)))
        vector = self._blank_vector()
        vector[self.num_note_on + self.num_note_off + quantized_time_num] = 1.0
        return vector
        

    def note_on_vector(self, note_on: int) -> np.ndarray:
        if note_on == -1:
            if not self.include_pedal:
                raise Exception("Encountered pedal on value in non-pedal factory")
            note_on = self.num_note_on
        else:
            note_on = np.clip(note_on - self.midi_note_offset, 0, self.num_note_on)
        vector = self._blank_vector()
        vector[int(note_on)] = 1.0
        return vector

    def note_off_vector(self, note_off: int) -> np.ndarray:
        if note_off == -1:
            if not self.include_pedal:
                raise Exception("Encountered pedal off value in non-pedal factory")
            note_off = self.num_note_off
        else:
            note_off = np.clip(note_off - self.midi_note_offset, 0, self.num_note_off)
        vector = self._blank_vector()
        vector[self.num_note_on + int(note_off)] = 1.0
        return vector

    def reverse_vector(self, vector: np.ndarray):
        raise NotImplemented()
    

if __name__ == "__main__":
    to_piano_roll(
        midi_file_path="/home/dennis/git/ki-ueben-klavier-trainieren/resources/kolessova04.mid"
    )
