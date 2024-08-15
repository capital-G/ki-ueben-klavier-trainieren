from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple
import logging
from typing import TypedDict

from pathlib import Path
from typing import Iterator, List
from torch.utils.data import DataLoader, IterableDataset, get_worker_info
import math

import pandas as pd
import torch.utils.data
from torchvision.datasets.utils import download_and_extract_archive
from .midi import PianoRoll

logger = logging.getLogger()


class MIDIFileRecord(TypedDict):
    file_path: Path


class MIDIFilesDataset(torch.utils.data.Dataset):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.midi_file_paths: List[Path] = []

    def __len__(self):
        return len(self.midi_file_paths)

    def __getitem__(self, index) -> MIDIFileRecord:
        if torch.is_tensor(index):
            index = index.tolist()

        midi_file_path = self.midi_file_paths[index]

        return {"file_path": midi_file_path}


class Maestro3Dataset(MIDIFilesDataset):
    def __init__(
        self,
        base_path: Optional[Path] = None,
        force_download: bool = False,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self._base_path = (
            base_path
            or Path(__file__).joinpath("../../data/maestro-v3.0.0").absolute().resolve()
        )
        self._download_url = "https://storage.googleapis.com/magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0-midi.zip"
        # self._content_folder = "maestro-v3.0.0"

        if not self._base_path.exists() or force_download:
            self.download_dataset()

        self.midi_file_paths = list(self._base_path.glob("**/*.mid*"))

    def download_dataset(self):
        logger.info("Start downloading dataset")
        download_and_extract_archive(
            url=self._download_url,
            download_root=self._base_path,
            remove_finished=True,
        )


class MIDIEventRecord(TypedDict):
    pass


class MIDIEventDataset(torch.utils.data.IterableDataset):
    def __init__(
        self,
        midi_files_dataset: MIDIFilesDataset,
        num_past_events: int,
        num_future_events: int,
        *args,
        **kwargs,
    ):
        self.midi_files_dataset = midi_files_dataset
        self.num_past_events = num_past_events
        self.num_future_events = num_future_events

        # state for caching
        self._file_counter = 0
        self._exhausted = True
        self._piano_roll = None
        self._current_file: Optional[Path] = None
        self._current_offset: int = 0
        self._events: Dict[str, pd.DataFrame] = {}

        self._get_next_midi_file()

        super().__init__(*args, **kwargs)

    def _get_next_midi_file(self):
        if worker_info := torch.utils.data.get_worker_info():
            num_workers = worker_info.num_workers
            worker_id = worker_info.id
        else:
            # worker info is not always available?
            num_workers = 1
            worker_id = 1

        file_idx = worker_id + (num_workers * self._file_counter) % len(
            self.midi_files_dataset
        )
        self._current_file = self.midi_files_dataset[file_idx]["file_path"]

        if self._current_file not in self._events:
            piano_roll = PianoRoll(
                midi_file_path=self._current_file,
            )
            self._events[str(self._current_file)] = piano_roll.events
        self._file_counter += 1

    @property
    def current_events(self) -> pd.DataFrame:
        return self._events[str(self._current_file)]

    def __iter__(self) -> Iterator[Tuple[List[MIDIEventRecord], List[MIDIEventRecord]]]:
        X = self.current_events.iloc[
            self._current_offset : self._current_offset + self.num_past_events
        ]
        Y = self.current_events.iloc[
            self._current_offset
            + self.num_past_events : self._current_offset
            + self.num_past_events
            + self.num_future_events
        ]

        self._current_offset += 1
        if self.num_past_events + self.num_future_events + self._current_offset >= len(
            self.current_events
        ):
            self._current_offset = 0
            self._get_next_midi_file()

        yield X, Y


class PianoRollDataset(IterableDataset):
    def __init__(self, midi_files: List[Path], window_size):
        super().__init__()
        self.midi_files = midi_files
        self.window_size = window_size
        self.piano_roll = None

    def __iter__(self):
        # determine the file offset for each worker
        worker_info = get_worker_info()
        if worker_info is None:
            iter_start = 0
            iter_end = len(self.midi_files)
        else:
            per_worker = int(
                math.ceil((len(self.midi_files)) / float(worker_info.num_workers))
            )
            iter_start = per_worker * worker_info.id
            iter_end = min(iter_start + per_worker, len(self.midi_files))

        for midi_file_path in self.midi_files[iter_start:iter_end]:
            # print(f"Load {midi_file_path}")
            piano_roll = PianoRoll(midi_file_path).piano_roll()
            for i in range(0, len(piano_roll) - (self.window_size + 1)):
                yield torch.Tensor(
                    piano_roll.iloc[i : i + self.window_size].to_numpy()
                ), torch.Tensor(
                    piano_roll.iloc[
                        i + self.window_size : 1 + i + self.window_size
                    ].to_numpy()
                )
