import requests

urlPlace = 'https://rickandmortyapi.com/api/location/68'
payload = {}
headers= {}
response = requests.request("GET", urlPlace, headers=headers, data = payload)
data = response.json() 

# Hasta acá ya se tiene la info del lugar, se procede a sacar a los residentes
if len(data['residents']):
    characters_url = data['residents']
    characters_numbers = ''
    for url in characters_url:
        lista = url.split('/')
        #characters_numbers.append(lista[-1])
        characters_numbers += (lista[-1]+',')

    characters_numbers = characters_numbers[0:-1]

    urlCharacters = 'https://rickandmortyapi.com/api/character/{}'.format(characters_numbers)
    payload = {}
    headers= {}
    response = requests.request("GET", urlCharacters, headers=headers, data = payload)
    characters = response.json() 
    data['residents'] = characters

print(data)