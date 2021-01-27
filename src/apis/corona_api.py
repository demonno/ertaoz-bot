import csv

import requests

from src import settings


def data_not_found():
    return "ვერ მოვიძიე ინფორმაცია 😢"


class Corona:
    corona_api_id = None

    def __init__(self):
        self.corona_api_id = settings.CORONA_API_ID

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

    def vaccination(self, city):
        resp = requests.get(
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
        )

        if resp.status_code == 200:
            decoded_content = resp.content.decode("utf-8")

            cr = csv.reader(decoded_content.splitlines(), delimiter=",")
            data_list = list(cr)
            country_row = []
            for row in data_list:
                country_name = row[2]
                country_code = row[0]
                if (
                    country_name.lower() == city.lower()
                    or country_code.lower() == city.lower()
                ):
                    country_row = row

            print(country_row)
            if country_row:
                population = "{:.2f}".format((float(country_row[44]) / 1000000))
                people_vaccinated = country_row[34]
                people_vaccinated_per_100 = country_row[39]
                people_fully_vaccinated_per_100 = country_row[40]
                gdp = country_row[49]
                result = (
                    f"{city} სულ მოსახლეობა: 🧍 {population} მილიონი\n"
                    f"აცრილი მოსახლეობა: 💉 {people_vaccinated}\n"
                    f"აცრილი ყოველ 100 კაცზე: {people_vaccinated_per_100}\n"
                    f"ორივე აცრა ყოველ 100 კაცზე: {people_fully_vaccinated_per_100}\n"
                    f"მთლიანი შიდა პროდუქტი {gdp} 💲\n"
                )
                return result
            else:
                return data_not_found()
        else:
            return data_not_found()
