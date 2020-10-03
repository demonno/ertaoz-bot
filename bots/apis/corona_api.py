import requests

from bots import env


def data_not_found():
    return "ვერ მოვიძიე ინფორმაცია 😢"


class Corona:
    corona_api_id = None

    def __init__(self):
        self.corona_api_id = env.str("CORONA_API_ID")

    def corona(self, city):
        resp = requests.get(
            "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php",
            headers={
                "X-RapidAPI-Host": "coronavirus-monitor.p.rapidapi.com",
                "X-RapidAPI-Key": self.corona_api_id,
            },
        )

        if resp.status_code == 200:
            corona_data = resp.json()
            countries_data = corona_data["countries_stat"]

            if city.lower() == "top":
                result = ""
                for i in range(10):
                    city_name = countries_data[i]["country_name"]
                    cases = countries_data[i]["cases"]
                    new_cases = countries_data[i]["new_cases"]
                    result += f"{city_name}: {cases}  +{new_cases}\n"
                return result
            else:
                for data in countries_data:
                    if data["country_name"].lower() == city.lower():
                        cases = data["cases"]
                        new_cases = data["new_cases"]
                        recovered = data["total_recovered"]
                        critical = data["serious_critical"]
                        death = data["deaths"]
                        new_death = data["new_deaths"]
                        result = (
                            f"{city} დაავადებული: 😷 {cases}\n"
                            f"ახალი შემთხვევა: 🤧 +{new_cases}\n"
                            f"გამოჯანმრთელებული: 😊 {recovered}\n"
                            f"კრიტიკულ მდგომარეობაში: 🤒 {critical}\n"
                            f"გარდაცვლილი: 💀 {death}  +{new_death}"
                        )
                        return result
            return data_not_found()
        else:
            return data_not_found()
