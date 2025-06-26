import requests

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}?strict=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n{country.title()} COVID-19 Stats:")
        print(f" Total Case: {data['cases']}")
        print(f" Toatal Deaths: {data['deaths']}")
        print(f" Total Recovered: {data['recovered']}")
    else:
        print("Invalid country name or API error.")

country = input("Enter a country name: ")
get_covid_data(country)