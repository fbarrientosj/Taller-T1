import requests

urlChapter = 'https://rickandmortyapi.com/api/episode/1'
payload = {}
headers= {}
response = requests.request("GET", urlChapter, headers=headers, data = payload)
data = response.json() 
characters_url = data['characters']
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
data['characters'] = characters

print(data)