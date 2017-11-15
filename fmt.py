import json

divisions = []
countries = []
divisionsByCountry = {}

with open('./countries-raw.json') as countriesFile:
    for line in countriesFile:
        country = json.loads(line)
        countries.append(country)

with open('./subdivisions-raw.json') as subdivisionsFile:
    for line in subdivisionsFile:
        division = json.loads(line)
        country_code = division['countryAlpha3']

        divisions.append(division)

        if country_code not in divisionsByCountry:
            divisionsByCountry[country_code] = []
        else:
            divisionsByCountry[country_code].append(division)

with open('./data/countries/all.json', mode="w+") as subdivisionsFile:
    subdivisionsFile.write(json.dumps(countries, indent=2, ))

with open('./data/subdivisions/all.json', mode="w+") as subdivisionsFile:
    subdivisionsFile.write(json.dumps(divisions, indent=2, ))

with open('./data/subdivisions/grouped.json', mode="w+") as subdivisionsFile:
    subdivisionsFile.write(json.dumps(divisionsByCountry, indent=2))

for key in divisionsByCountry:
    with open('./data/subdivisions/by_country/{countryCode}.json'.format(countryCode=key), mode="w+") as countryDivisionsFile:
        countryDivisionsFile.write(json.dumps(divisionsByCountry[key], indent=2))
