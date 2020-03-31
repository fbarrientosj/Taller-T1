from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():

    url1 = "https://rickandmortyapi.com/api/episode/"
    url2 = "https://rickandmortyapi.com/api/episode?page=2"
    payload = {}
    headers= {}
    response1 = requests.request("GET", url1, headers=headers, data = payload)
    response2 = requests.request("GET", url2, headers=headers, data = payload)
    data1 = response1.json() 
    data2 = response2.json() 
    episodes1 = data1['results']
    episodes2 = data2['results']
    episodes = episodes1 + episodes2
    return render_template('home.html', episodes=episodes)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/episode/<int:episode_id>')
def find_episode(episode_id): 
    urlChapter = 'https://rickandmortyapi.com/api/episode/{}'.format(episode_id)
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

    return render_template('episode.html', episode=data)

@app.route('/character/<int:character_id>')
def find_character(character_id): 
    urlCharacter = 'https://rickandmortyapi.com/api/character/{}'.format(character_id)
    payload = {}
    headers= {}
    response = requests.request("GET", urlCharacter, headers=headers, data = payload)
    data = response.json()

    episode_url = data['episode']
    episode_numbers = ''
    for url in episode_url:
        lista = url.split('/')
        episode_numbers += (lista[-1]+',')

    episode_numbers = episode_numbers[0:-1]

    urlEpisodes = 'https://rickandmortyapi.com/api/episode/{}'.format(episode_numbers)
    payload = {}
    headers= {}
    response = requests.request("GET", urlEpisodes, headers=headers, data = payload)
    episodes = response.json() 
    data['episode'] = episodes

    # Podría ocurrir que el personaje solo aparezca en un cápitulo

    if type(episodes) == list:
        data['typeEpisode'] = 'list'
    else:
        data['typeEpisode'] = 'dict'

    # Para sacar el id del planeta del personaje
    if data['origin']['name'] != 'unknown':
        data['origin']['id'] = data['origin']['url'].split('/')[-1]
    
    else:
        data['origin']['id'] = 'unknown'

    return render_template('character.html', character=data)

    
@app.route('/place/<int:place_id>')
def find_place(place_id): 

    urlPlace = 'https://rickandmortyapi.com/api/location/{}'.format(place_id)
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

    # Podría ocurrir que el lugar solo tuviese un habitante
    print(characters)
    
    if type(data['residents']) == list:
        data['typeCharacters'] = 'list'
    else:
        data['typeCharacters'] = 'dict'
    return render_template('place.html', place=data)
    



if __name__ == '__main__':
    app.run(debug=True)