from dataclasses import dataclass


@dataclass
class AdventUser:
    name: str
    local_score: int
    stars: int

    @property
    def formatted(self) -> str:
        star_message = "*" * self.stars
        return f"{star_message:<30} - {self.name:<22} {self.local_score:<3}"
