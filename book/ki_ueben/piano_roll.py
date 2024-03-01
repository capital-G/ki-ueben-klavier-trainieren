from pathlib import Path

import mido


class PianoRoll:
    def __init__(self):
        pass

    @classmethod
    def from_midi_file(cls, midi_file_path: Path):
        if isinstance(midi_file_path, str):
            midi_file_path = Path(midi_file_path)
        midi_file = mido.MidiFile(filename=str(midi_file_path.absolute()))
        for track in midi_file:
            for msg in track:
                print(msg)
        pass
