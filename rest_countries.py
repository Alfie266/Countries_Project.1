import requests

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
    if response == 200:
        response = response.json()
    else:
        print("There has been an error in fetching the data.")
    # print(response.json())
    return response


def parse_info():
    """Extract relevant information from the JSON response"""
    response = get_data()

    for i in response:
        official_name.append(response[i]['name']['official'])
        num_code.append(response[i]['ccn3'])
        alpha_code.append(response[i]['cca3'])
        un_mem.append(response[i]['unMember'])
        currencies.append(response[i]['currencies'])
        capital.append(response[i]['capital'])
        region.append(response[i]['region'])
        continent.append(response[i]['continents'])
        timezone.append(response[i]['timezones'])
        lat_lng.append(response[i]['latlng'])
        area.append(response[i]['area'])
        flags.append(response[i]['flags'])
        population.append(response[i]['population'])
        demonyms.append(response[i]['demonyms'])

# print(response[0])
