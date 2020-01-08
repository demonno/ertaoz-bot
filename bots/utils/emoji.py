import re

# http://stackoverflow.com/a/13752628/6762004
RE_EMOJI = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)


def strip_emoji(text: str) -> str:
    return RE_EMOJI.sub(r"", text)


def strip_spaces(text: str) -> str:
    return re.sub(" +", " ", text)
