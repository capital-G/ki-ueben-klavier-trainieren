import mido
import pandas as pd
import dataclasses
from pathlib import Path
import music21
from collections import defaultdict
import enum
from typing import List, Optional

class MidiEventType(enum.Enum):
    NOTE_ON = 1
    NOTE_OFF = 2

@dataclasses.dataclass
class MidiEvent:
    midi_event_type: MidiEventType
    note: int
    time: float

@dataclasses.dataclass
class PianoRoll:
    pass

def to_piano_roll(
        midi_file_path: str,
        resolution: int = 256
    ) -> None:
    midi_file = mido.MidiFile(midi_file_path)

    filtered_messages: List[MidiEvent] = []
    
    # message: mido.messages.messages.Message
    for message in midi_file:
        match message.type:
            case "note_on":
                filtered_messages.append(MidiEvent(
                    midi_event_type=MidiEventType.NOTE_ON,
                    note=message.note,
                    time=message.time,
                ))
            case "note_off":
                filtered_messages.append(MidiEvent(
                    midi_event_type=MidiEventType.NOTE_OFF,
                    note=message.note,
                    time=message.time,
                ))
    
    print(filtered_messages[0:100])

    

    piano_roll = []


    current_time = 0.0
    pass


class PianoRoll:
    def __init__(self, midi_file_path: str):
        self.midi_file = mido.MidiFile(midi_file_path)
        self.tempo = self.get_tempo()
    
    def get_tempo(self) -> Optional[float]:
        for msg in self.midi_file:
            if msg.type == 'set_tempo':
                return mido.tempo2bpm(msg.tempo)
        return None
    
    def events(self) -> pd.DataFrame:
        """
        """
        events = []
        time = 0.0
        for msg in self.midi_file:
            time += msg.time
            if any([x == msg.type for x in ["note_on", "note_off"]]):
                events.append({
                    "note": msg.note,
                    "velocity": msg.velocity if msg.type=="note_on" else 0,
                    "time": time,
                })
            # pedal
            elif msg.is_cc(64):
                events.append({
                    "note": -1,
                    "velocity": msg.value,
                    "time": time,
                })
        events = pd.DataFrame(events)
        return events

    def piano_roll(self) -> pd.DataFrame:
        events = self.events()
        events = events.pivot_table(values="velocity", index="time", columns="note", aggfunc="max")
        events = events.ffill().fillna(0.0)
        events.index = pd.TimedeltaIndex(events.index*10e8)
        return events

class MidiPlayer:
    def __init__(self, device_name: str) -> None:
        pass

    @staticmethod
    def print_devices(self) -> None:
        pass

    def playback(self, midi_data):
        pass

    async def async_playbac(self):
        pass

if __name__ == "__main__":
    to_piano_roll(
        midi_file_path="/home/dennis/git/ki-ueben-klavier-trainieren/resources/kolessova04.mid"
    )
