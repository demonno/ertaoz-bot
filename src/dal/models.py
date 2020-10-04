from dataclasses import dataclass


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    telegram_id: int = 0

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def telegram_url(self) -> str:
        return f"tg://user?id={self.telegram_id}"


@dataclass
class Wisdom:
    text: str
    animation: str
