import csv

import flag
import pycountry
import requests

from src import settings


def data_not_found():
    return "ვერ მოვიძიე ინფორმაცია 😢"


class Corona:
    corona_api_id = None
    vaccination_data_etag = None
    vaccination_data_list = None

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
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv",
            headers={"If-None-Match": self.vaccination_data_etag},
        )

        if resp.status_code == 200:
            decoded_content = resp.content.decode("utf-8")
            self.vaccination_data_etag = resp.headers.get("etag")
            self.vaccination_data_list = list(
                csv.reader(decoded_content.splitlines(), delimiter=",")
            )
            return self.parse_vaccination_data(city)
        elif resp.status_code == 304:
            return self.parse_vaccination_data(city)
        else:
            return data_not_found()

    def parse_vaccination_data(self, city):
        data_list = self.vaccination_data_list
        country_row = []
        for row in data_list[:-1]:
            country_name = row[2]
            country_code = row[0]
            if (
                country_name.lower() == city.lower()
                or country_code.lower() == city.lower()
            ):
                country_row = row

        if country_row:
            country_iso = pycountry.countries.search_fuzzy(country_row[2])[0].alpha_2
            vaccinated_int = int(float(country_row[34])) if country_row[34] else 0
            population = "{:.2f}".format((float(country_row[44]) / 1000000))
            people_vaccinated = format((vaccinated_int), ",").replace(",", " ")
            people_vaccinated_per_100 = country_row[40]
            people_fully_vaccinated_per_100 = country_row[41]
            gdp = format(int(float(country_row[49])), ",").replace(",", " ")
            result = flag.flagize(
                (
                    f"<b>{city}</b> :{country_iso}:  სულ მოსახლეობა: 🧍 <b>{population} მილიონი</b>\n"
                    f"აცრილი მოსახლეობა: 💉 <b>{people_vaccinated if people_vaccinated else 0}</b>\n"
                    f"აცრილი: 📈 <b>{people_vaccinated_per_100 if people_vaccinated_per_100 else 0} %</b>\n"
                    f"ორივე აცრა: 📊 <b>{people_fully_vaccinated_per_100 if people_fully_vaccinated_per_100 else 0} %</b>\n"
                    f"მშპ ერთ სულ მოსახლეზე (PPP) <b>{gdp} 💲</b>\n"
                )
            )
            return result
        else:
            return data_not_found()
