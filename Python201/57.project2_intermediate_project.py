#ask for user input
#create dynamic url
#fetch data using url
#convert json to dictionary
#print out pokemon data
import requests

while True:
    pokemon = input("which pokemon do you want to find? ")
    pokemon = pokemon.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()

        print(f"name is\t{data['name']}")

        print("abilities: ")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found!")