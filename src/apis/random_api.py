import random
from dataclasses import dataclass
from enum import Enum

import requests


class RandomNotImplemented(Exception):
    pass


class ResourceType(Enum):
    GIF = "gif"
    IMG = "img"
    TEXT = "text"


@dataclass
class Resource:
    type: ResourceType
    content: str


class RandomAPI:
    """
    Integration with some random api


    https://some-random-api.ml/docs
    """

    def __init__(self) -> None:
        self.api_url = "https://some-random-api.ml"

    def fetch_img_resource(self, resource: str) -> Resource:
        url = f"{self.api_url}/img/{resource}"
        r = requests.get(url)
        r.raise_for_status()

        return Resource(ResourceType.IMG, r.json()["link"])

    def fetch_animu_resource(self, resource: str) -> Resource:
        url = f"{self.api_url}/animu/{resource}"
        r = requests.get(url)
        r.raise_for_status()

        return Resource(ResourceType.GIF, r.json()["link"])

    def fetch_fact_resource(self, resource: str) -> Resource:
        url = f"{self.api_url}/facts/{resource}"
        r = requests.get(url)
        r.raise_for_status()

        return Resource(ResourceType.TEXT, r.json()["fact"])

    def fetch(self, resource, **params) -> Resource:
        if resource is None:
            random_resource = random.choice(["panda", "dog", "cat", "birb", "koala"])
            return self.fetch_img_resource(random_resource)
        elif resource in ["panda", "პანდა"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("panda")
            return self.fetch_img_resource("panda")
        elif resource in ["dog", "ძაღლი"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("dog")
            return self.fetch_img_resource("dog")
        elif resource in ["cat", "კატა", "ფისო", "კნუტი"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("cat")
            return self.fetch_img_resource("cat")
        elif resource in ["fox", "მელა", "მელაკუდა"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("fox")
            return self.fetch_img_resource("fox")
        elif resource in ["bird", "ჩიტი"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("bird")
            return self.fetch_img_resource("birb")
        elif resource in ["koala", "კოალა"]:
            if params.get("fact") is True:
                return self.fetch_fact_resource("koala")
            return self.fetch_img_resource("koala")
        elif resource in ["wink"]:
            return self.fetch_animu_resource("wink")
        elif resource in ["hug"]:
            return self.fetch_animu_resource("hug")

        raise RandomNotImplemented
