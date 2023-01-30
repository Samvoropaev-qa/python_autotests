import requests
import json

token = '4fba7c9449b48a8ab5f9841e5f085353'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token': token},
json = {
  "name": "Карась",
  "photo": "https://dolnikov.ru/pokemons/albums/10.png"
})

print(response.text) 

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-Type' : 'application/json', 
'trainer_token': token}, json = 
{
  "pokemon_id": pokemon_id,
  "name": "Карасик",
  "photo": "https://dolnikov.ru/pokemons/albums/10.png"
})

print (response_change.text)


pokemon_id = response.json()['id']

response_change = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 
'trainer_token': token},
json = {
    "pokemon_id": pokemon_id,
})

print(response_change.text)