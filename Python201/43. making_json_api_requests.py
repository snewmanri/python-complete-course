import requests
req = requests.get("https://swapi.tech/api/people/2")
props = req.json()
person = props['result']['properties']

print(f"name is \t\t{person['name']}")
print(f"birth year is \t\t{person['birth_year']}")

# print("props", props)
# #sw api is broke but you get the point
# for film in person['films']:
#     req = requests.get(film)
#     film = req.json()
#     print(film)
#     print("film is: ", film['title'])

