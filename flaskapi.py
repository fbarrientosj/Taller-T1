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
    print(type(episode_id))
    print(episode_id)
    return render_template('episode.html', episode=episode_id)


if __name__ == '__main__':
    app.run(debug=True)