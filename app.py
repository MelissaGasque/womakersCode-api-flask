from flask import Flask, render_template
import urllib.request
import json
# # urllib ajuda a manipular as requisições e o json ajuda a tratar o resultado

app = Flask(__name__)
base_url = "http://127.0.0.1:5000/"

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
    url = (f"https://rickandmortyapi.com/api/character/" + id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    origin_link = dict["origin"]["url"]
    origin_id = origin_link.split('/')[-1]

    location_link = dict["location"]["url"]
    location_id = location_link.split('/')[-1]

    dict["origin"]["url"] = (f"{base_url}location/{origin_id}")
    dict["location"]["url"] = (f"{base_url}location/{location_id}")

    episodes = []

    for unique_episode in dict["episode"]:
        url2 = unique_episode
        response2 = urllib.request.urlopen(url2)
        data2 = response2.read()
        dict2 = json.loads(data2)

        episode = {
            "name": dict2["name"],
            "link": (f"{base_url}episode/{dict2["id"]}")
        }

        episodes.append(episode)



    result = {
        "name": dict["name"],
        "image": dict["image"],
        "species": dict["species"],
        "gender": dict["gender"],
        "origin": dict["origin"],
        "location": dict["location"],
        "status": dict["status"],
        "episodes": episodes
    }

    return render_template("profile.html", profile=result)


@app.route("/locations")
def get_list_locations_page():
    url = (f"https://rickandmortyapi.com/api/location/")
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])


@app.route("/location/<id>")
def get_location_page(id):
    url = (f"https://rickandmortyapi.com/api/location/" + id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    residents = []

    for resident in dict["residents"]:
        url2 = resident
        response2 = urllib.request.urlopen(url2)
        data2 = response2.read()
        dict2 = json.loads(data2)

        character = {
             "name": dict2["name"],
             "link": (f"{base_url}profile/{dict2["id"]}")
        }

        residents.append(character)

    result = {
        "name": dict["name"],
        "type": dict["type"],
        "dimension": dict["dimension"],
        "residents": residents
    }

    return render_template("location.html", location=result)


@app.route("/episodes")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"])


@app.route("/episode/<id>")
def get_episode_page(id):
    url = (f"https://rickandmortyapi.com/api/episode/" + id)
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    characters = []

    for unique_character in dict["characters"]:
        url2 = unique_character
        response2 = urllib.request.urlopen(url2)
        data2 = response2.read()
        dict2 = json.loads(data2)

        character = {
             "name": dict2["name"],
             "link": (f"{base_url}profile/{dict2["id"]}")
        }

        characters.append(character)

    result = {
        "name": dict["name"],
        "air_date": dict["air_date"],
        "episode": dict["episode"],
        "characters": characters
    }

    return render_template("episode.html", episode=result)



