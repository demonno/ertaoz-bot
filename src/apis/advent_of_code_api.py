import requests

from src.dal.advent_of_code_user import AdventUser


def data_not_found():
    return "ვერ მოვიძიე ინფორმაცია 😢"


class AdventOfCode:
    def leaderboard(self):
        resp = requests.get(
            "https://adventofcode.com/2020/leaderboard/private/view/806524.json",
            headers={
                "cookie": "session=53616c7465645f5f5ca7760da729cd1d9320586020588532702cd89c78d1f2a3ae548bd97496fbd39da874d970abf9fd"
            },
        )

        if resp.status_code == 200:
            result = ""
            leaderboard_data = resp.json()
            members = leaderboard_data["members"]

            members_list = []

            for (key, value) in members.items():
                name = value["name"]
                local_score = value["local_score"]
                stars = value["stars"]
                members_list.append(AdventUser(name, local_score, stars))

            members_list.sort(key=lambda x: x.local_score, reverse=True)

            for advent_user in members_list:
                result += f"{advent_user.formatted}\n"

            return result
        else:
            return data_not_found()
