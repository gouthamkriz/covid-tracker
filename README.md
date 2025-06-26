# 🦠 COVID-19 Tracker

A Python-based application that fetches and displays real-time global COVID-19 statistics using the [disease.sh](https://disease.sh/) API. This project demonstrates API integration, JSON parsing, and basic data presentation in the terminal.

---

## 👨‍💻 About the Developer

**Name**: Goutham Krishna C M  
**GitHub**: [gouthamkriz](https://github.com/gouthamkriz)  
**Role**: Aspiring AI Engineer focused on building impactful, real-world applications using Python and machine learning.

---

## 🚀 Features

- Fetches up-to-date global COVID-19 data
- Displays:
  - Total confirmed cases
  - Total deaths
  - Total recovered
  - Today's new cases and deaths
- Simple and clean command-line interface

---

## 🛠️ Tech Stack

- Python 3.x
- `requests` library
- [disease.sh API](https://disease.sh/)

---

## 📦 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/gouthamkriz/covid-tracker.git
cd covid-tracker
```
### Step 2: Install Dependencies

```bash
pip install requests
```


### Step 3: Create the Python Script
Create a file named covid_tracker.py and paste the following code:
import requests
from datetime import datetime

def get_covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()

    print("\n🌍 Global COVID-19 Statistics")
    print(f"🦠 Total Cases: {data['cases']}")
    print(f"💀 Total Deaths: {data['deaths']}")
    print(f"💚 Total Recovered: {data['recovered']}")
    print(f"📈 Today's Cases: {data['todayCases']}")
    print(f"📉 Today's Deaths: {data['todayDeaths']}")
    print(f"🕒 Last Updated: {datetime.fromtimestamp(data['updated']/1000)}\n")

if __name__ == "__main__":
    get_covid_data()


### Step 4: Run the Script

```bash
python covid_tracker.py
```



