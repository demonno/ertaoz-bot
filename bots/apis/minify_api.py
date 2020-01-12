import requests


class MinifyAPIException(Exception):
    pass


class MinifyAPI:
    def __init__(self):
        self.api_url = "https://megrulad.ge/u/save/"

    def set_url(self, url=""):
        self.api_url = url

    def minify_link(self, link: str) -> str:
        form_data = {"url": link}
        response = requests.post(self.api_url, data=form_data, verify=True)
        response.raise_for_status()
        response.encoding = "utf-8"
        response = response.json()
        if not response["success"]:
            raise MinifyAPIException
        return response["url"]
