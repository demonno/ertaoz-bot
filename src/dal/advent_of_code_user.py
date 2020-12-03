from dataclasses import dataclass


@dataclass
class AdventUser:
    name: str
    local_score: int
    stars: int

    @property
    def formatted(self) -> str:
        star_message = "*" * self.stars
        return f"{self.name}: {self.local_score}  {star_message}"
