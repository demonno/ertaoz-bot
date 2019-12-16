from dataclasses import dataclass


@dataclass
class Contributor:
    github: str

    @property
    def github_url(self):
        return f"https://github.com/{self.github}"


CONTRIBUTORS = [
    Contributor("demonno"),
    Contributor("pepela"),
    Contributor("dmuml10"),
    Contributor("Dgebu"),
    Contributor("MadViper"),
]
