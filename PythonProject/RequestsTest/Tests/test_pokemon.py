import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'af9f7e8a600d64db99c14326fa4b732f'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '33231'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers/{TRAINER_ID}')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID})
    '''assert response_get.status_code == 200'''
    assert response_get.json()["data"][0]["trainer_name"] == 'БОБДжингер'

@pytest.mark.parametrize('key, value',[(TRAINER_ID, 'БОБДжингер2'),('38558', 'Грин'),('38555', 'Бак2')])
def test_parametrize(key,value):
    response_json = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id': key}).json()
    assert response_json["data"][0]['trainer_name'] == value
