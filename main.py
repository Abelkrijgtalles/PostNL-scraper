import requests
from iso3166 import countries

# [[[land, land2], 200, 300, 400, 500]]
zones = []

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
        prijs100 = 0
        prijs500 = 0
        prijs1000 = 0
        prijs2000 = 0
        for ding in data:
            match ding["identifier"]:
                case "50_0_00_0":
                    prijs100 = ding["minPrice"]
                case "50_1_00_0":
                    prijs100 = ding["minPrice"] - 100
                case "300_0_00_0":
                    prijs500 = ding["minPrice"]
                case "300_1_00_0":
                    prijs500 = ding["minPrice"] - 100
                case "750_0_00_0":
                    prijs1000 = ding["minPrice"]
                case "750_1_00_0":
                    prijs1000 = ding["minPrice"] - 100
                case "1500_0_00_0":
                    prijs2000 = ding["minPrice"]
                case "1500_1_00_0":
                    prijs2000 = ding["minPrice"] - 100
                case _:
                    print("Womp womp iets ging verkeerd bij " + country.name)
                    print(data)
        if prijs100 == 0 or prijs500 == 0 or prijs1000 == 0 or prijs2000 == 0:
            print("Womp womp iets ging verkeerd bij " + country.name)
            print(data)
            continue
        in_zone = False
        for zone in zones:
            if prijs100 == zone[1] and prijs500 == zone[2] and prijs1000 == zone[3] and prijs2000 == zone[4]:
                zone[0].append(country.name)
                in_zone = True
                break
        if not in_zone:
            zones.append([[country.name], prijs100, prijs500, prijs1000, prijs2000])
    else:
        print("Womp womp iets ging verkeerd bij " + country.name)
        print(response.status_code)
        continue

    print(country.alpha2)

with open("result.txt", "w") as result_file:
    print(zones, file=result_file)
    print("\nZones:\n")
    sorted_zones = sorted(zones, key=lambda x: x[1], reverse=False)
    for zone in sorted_zones:
        print("Zone " + str(sorted_zones.index(zone) + 1), file=result_file)
        print("---", file=result_file)
        print("Countries:", file=result_file)
        for country in zone[0]:
            print(country)
        print("0-100g: " + str(zone[1]), file=result_file)
        print("100-500g: " + str(zone[2]), file=result_file)
        print("500-1000g: " + str(zone[3]), file=result_file)
        print("1000-2000g: " + str(zone[4]), file=result_file)
        print("---\n", file=result_file)
    result_file.close()