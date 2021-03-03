import requests
import covid
# get data using api
respons_state = requests.get(url="https://api.covid19india.org/data.json")  # statewise covid data
response_district = requests.get(url="https://api.covid19india.org/state_district_wise.json")  # district data
respons_state.raise_for_status()
response_district.raise_for_status()

state_data = respons_state.json()["statewise"]
district_data = response_district.json()
del district_data["State Unassigned"]

country = "INDIA"
covid_19_detail = covid.CovidTracker(country, state_data, district_data) #pass data to class
covid_19_detail