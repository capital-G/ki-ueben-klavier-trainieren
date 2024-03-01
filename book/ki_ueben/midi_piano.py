import mido


class MidiPiano:
    def __init__(self, out_port: mido.ports.BaseOutput, channel: int = 0) -> None:
        self.out_port = out_port
        self.channel = channel

    @classmethod
    def spirio(cls):
        return cls()

    @classmethod
    def iac(cls):
        return cls(
            out_port=mido.open_output("IAC Driver Bus 1"),
        )

    def play(self, note: int = 100, velocity: int = 50):
        self.out_port.send(
            mido.Message(
                "note_on",
                channel=self.channel,
                note=note,
                velocity=velocity,
            )
        )

    def all_notes_off(self):
        self.out_port.send(
            mido.Message(
                "control_change",
                channel=self.channel,
                control=123,
            )
        )
