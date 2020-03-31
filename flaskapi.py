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
    print(type(episodes))
    if type(episodes) == list:
        data['typeEpisode'] = 'list'
        print('entre')
        print('entre')
        print('entre')
        print('entre')
    else:
        data['typeEpisode'] = 'dict'
    return render_template('character.html', character=data)


if __name__ == '__main__':
    app.run(debug=True)