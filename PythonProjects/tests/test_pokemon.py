import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4443b8771bde2866d737fb39c70a1990'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = 29532
TRAINER_NAME = 'Кот Василий'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers/{TRAINER_ID}', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()['trainer_name'] == 'Кот Василий'


