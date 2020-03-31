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


if __name__ == '__main__':
    app.run(debug=True)