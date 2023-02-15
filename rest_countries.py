import requests
# import pandas as pd


official_name = []
num_code = []
alpha_code = []
un_mem = []
currencies = []
capital = []
region = []
continent = []
timezone = []
lat_lng = []
area = []
flags = []
population = []
demonyms = []


def get_data():
    """Request the data from the online API"""
    countries_url = "https://restcountries.com/v3.1/all"
    response = requests.get(countries_url)
    # print(response.json())
    return response.json()


def parse_info():
    """Extract relevant information from the JSON response"""
    response = get_data()

    for i in response:
        official_name.append(i['name']['official'])
        # num_code.append(i['ccn3'])
        alpha_code.append(i['cca3'])
        un_mem.append(i['unMember'])
        # currencies.append(i['currencies'])
        # capital.append(i['capital'])
        region.append(i['region'])
        continent.append(i['continents'])
        timezone.append(i['timezones'])
        lat_lng.append(i['latlng'])
        area.append(i['area'])
        flags.append(i['flags'])
        population.append(i['population'])
        # demonyms.append(i['demonyms'])

    # print(response[0])


def create_dataframe():
    pass


def plot_graphs():
    pass


def plot_maps():
    pass


# parse_info()
# print(len(official_name))
# print(len(num_code))
# print(len(alpha_code))
# print(len(un_mem))
# print(len(currencies))
# print(len(capital))
# print(len(region))
# print(len(continent))
# print(len(timezone))
# print(len(lat_lng))
# print(len(area))
# print(len(flags))
# print(len(population))
# print(len(demonyms))
