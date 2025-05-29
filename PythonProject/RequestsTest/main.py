import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'af9f7e8a600d64db99c14326fa4b732f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33231'

pokemon_name = "Агент 007"
pokemon_id = "0"

body_create_pokemon = {
    "name": pokemon_name,
    "photo_id": -1
}

response_create_pok = requests.post (url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create_pokemon )
print(response_create_pok.text)
if response_create_pok.status_code == 201:
    pokemon_id = response_create_pok.json()['id']
    print(f'Свежий покемон по имени {pokemon_name} имеет номер {pokemon_id}')
else: 
    print(response_create_pok.json()['message'])
    response_json = requests.get (url = f'{URL}/v2/pokemons', headers = HEADER, params={'trainer_id': TRAINER_ID}).json()
    pokemon_id = response_json["data"][0]['id']
    pokemon_name = response_json["data"][0]['name']
    print(f'Дальше используем покемона с номером {pokemon_id} и именем {pokemon_name}')

body_change_pok = {
    "pokemon_id": pokemon_id,
    "name": "Спец агент на пенсии",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": pokemon_id
}
    
response_change_pok = requests.put (url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change_pok)
print(response_change_pok.text)

response_add_pokeball = requests.post (url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)