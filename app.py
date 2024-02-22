from flask import Flask, render_template
import urllib.request
import json
# # urllib ajuda a manipular as requisições e o json ajuda a tratar o resultado

app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])
    # characters.html é o arquivo
    # Uma lista de characters recebendo o resultado


@app.route("/profile/<id>")
def get_profile_page(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


# @app.route("/lista")
# def get_list_elements():
#     url = "https://rickandmortyapi.com/api/character/"
#     response = urllib.request.urlopen(url)
#     characters = response.read()
#     dict = json.loads(characters)

#     characters = []

#     for character in dict["results"]:
#         character = {
#             "name": character["name"],
#             "status": character["status"]
#         }

#         characters.append(character)

#     return {"characters": characters}

@app.route("/locations")
def get_list_locations_page():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])


@app.route("/location/<id>")
def get_location_page(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("location.html", location=dict)


@app.route("/episodes")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"])


@app.route("/episode/<id>")
def get_episode_page(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episode.html", episode=dict)


# @app.route("<link>")
# def perfilPersonagem_page(link):
#     url = link
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     dict = json.loads(data)

#     return render_template("perfilPersonagem.html", teste=dict)
