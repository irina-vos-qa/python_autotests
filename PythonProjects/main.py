
import requests
import json

# URL для API
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4443b8771bde2866d737fb39c70a1990'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}


# Создание покемона
create_pokemon_url = f'{URL}/pokemons'
create_pokemon_data = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(create_pokemon_url, headers=HEADER, json=create_pokemon_data)
print("Создание покемона:", response_create.json())

pokemon_id = response_create.json()['id']
print(pokemon_id)

# Смена имени покемона
change_url = f'{URL}/pokemons'
change_data ={
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}
response_change = requests.put(change_url, headers=HEADER, json=change_data)
print("Смена имени покемона:", response_change.json())

# Поймать покемона в покебол
catch_pokemon_url = f'{URL}/trainers/add_pokeball'
catch_pokemon_data = {
    "pokemon_id": pokemon_id
}
response_catch = requests.post(catch_pokemon_url, headers=HEADER, json=catch_pokemon_data)
print("Поймать покемона в покебол:", response_catch.json())
