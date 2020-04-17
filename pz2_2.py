numCountries = int(input())
countries = {}
for i in range(numCountries):
  countryInfo = input().split()
  country = countryInfo[0]
  citiesSet = set(countryInfo[1:len(countryInfo)])
  countries[countryInfo[0]] = citiesSet

numCitiesToFind = int(input())
cities = [];
for i in range(numCitiesToFind):
  cities.append(input())

for i in range(numCitiesToFind):
  for j in countries.keys():
    if (cities[i] in countries[j]):
      print(j)
    
