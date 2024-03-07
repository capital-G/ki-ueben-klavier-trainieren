from pathlib import Path
from typing import List
import glob


class Maestro3:
    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path
    
    def get_midi_files(self) -> List[Path]:
        return glob.glob("**/*.midi", root_dir=self.base_path)
