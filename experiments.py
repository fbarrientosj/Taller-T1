import requests


url8 = 'https://integracion-rick-morty-api.herokuapp.com/api/character/'
payload = {}
headers= {}
response1 = requests.request("GET", url8, headers=headers, data = payload)
data1 = response1.json() 
characters = data1['results']

for i in range(2, data1['info']['pages'] + 1):
    url = "https://integracion-rick-morty-api.herokuapp.com/api/character/?page={}".format(i)
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    data = response.json() 
    characters += data['results']

for character in characters:
    if search.lower() in character['name'].lower():

        print(character['name'])
        personajesCoincidentes.append(character)