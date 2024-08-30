import requests
from bs4 import BeautifulSoup as bs4
from unidecode import unidecode
from app.crud import get_all_countries, get_all_cities, insert_city
from app.db_config import get_db_connection


def get_temperature(country, city):
    url = f"https://www.timeanddate.com/weather/{country}/{city}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = bs4(response.text, "html.parser")
        element = soup.select_one("#qlook > div.h2")
        if element:
            temperature = element.text.strip()
            return temperature
        else:
            return "Temperature element not found"
    else:
        return f"Failed to retrieve data, status code: {response.status_code}"


def update_cities_requests(conn, countries, cities):
    seletor = "body > main > article > section.pdflexi > div > table > *"

    for country in countries:
        try:
            response = requests.get(f"https://www.timeanddate.com/weather/{country}")
            if response.status_code == 200:
                soup = bs4(response.text, "html.parser")
                table = soup.select(seletor)
                for row in table:
                    city_list = row.select("a")
                    for city in city_list:
                        city = unidecode(city.text).strip().lower().replace(" ", "-")
                        if city not in cities:
                            insert_city(conn=conn, city=city)
            else:
                print(
                    f"Failed to get data for country {country}, status code: {response.status_code}"
                )
        except Exception as e:
            print(f"Skipping country {country}, ERRO: {e}")
