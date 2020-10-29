import requests

from src import settings


class ImageFlipApiException(Exception):
    pass


class ImageflipAPI:
    """Imageflip API integration

    Docs: https://api.imgflip.com/"""

    def __init__(self) -> None:
        self.api_url = "https://api.imgflip.com"
        self.username = settings.IMGFLIP_API_USERNAME
        self.password = settings.IMGFLIP_API_PASSWORD
        self.mocking_spongebob_meme_id = 102156234

    def mocking_spongebob_url(self, text_top, text_bottom) -> str:
        data = {
            "username": self.username,
            "password": self.password,
            "template_id": self.mocking_spongebob_meme_id,
            "boxes[0][text]": text_top,
            "boxes[1][text]": text_bottom,
        }
        url = f"{self.api_url}/caption_image"
        r = requests.post(url, data=data)
        r.raise_for_status()
        data = r.json()
        if data["success"] and "url" in data["data"]:
            return data["data"]["url"]
        raise ImageFlipApiException
