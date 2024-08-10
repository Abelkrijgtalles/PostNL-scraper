import requests
from iso3166 import countries

result = "PostNL Scraper - Abel van Hulst\n:):):):):):):):):):)"

# def brief(country):
#     url = ("https://jouw.postnl.nl/online-versturen/api/country/"
#            + country.alpha2 + "/productGroup/LetterBoxParcel/weightclass")
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         prijs = 0
#         for ding in data:
#             if ding["identifier"] == "10_0_00_0":
#                 prijs = ding["minPrice"]
#         if prijs == 0:
#             print("Womp womp iets ging verkeerd bij " + country.name)
#             print(data)
#             result += "\n" + country.alpha2 + ": womp womp"
#         else:
#             result += "\n" + country.alpha2 + ": " + str(prijs)
#
#     else:
#         print("Womp womp iets ging verkeerd bij " + country.name)
#         print(response.status_code)
#         result += "\n" + country.alpha2 + ": womp womp"

for country in countries:

    if country.alpha2 == "NL":
        continue

    url = ("https://jouw.postnl.nl/online-versturen/api/country/"
           + country.alpha2 + "/productGroup/LetterBoxParcel/weightclass")
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        prijs = 0
        for ding in data:
            if ding["identifier"] == "50_0_00_0":
                prijs = ding["minPrice"]
            elif ding["identifier"] == "50_1_00_0":
                prijs = ding["minPrice"] - 1
        if prijs == 0:
            print("Womp womp iets ging verkeerd bij " + country.name)
            print(data)
            result += "\n" + country.alpha2 + ": womp womp"
        else:
            result += "\n" + country.alpha2 + ": " + str(prijs)
    else:
        print("Womp womp iets ging verkeerd bij " + country.name)
        print(response.status_code)
        result += "\n" + country.alpha2 + ": womp womp"

    print(country.alpha2)

with open("result.txt", "w") as result_file:
    print(result, file=result_file)