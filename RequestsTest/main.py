import requests

"""response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/reg',
               json ={
                "trainer_token": "2ddf82170250fa8958d0af5081a419ca",
                "email": "br07e@greencafe24.com",
                "password": "Iloveqa1"
                },
                headers= {'Content-Type':'application/json'}, timeout=5)
print(response)"""


"""response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/confirm_email',
               json ={"trainer_token": "2ddf82170250fa8958d0af5081a419ca"},
                headers= {'Content-Type':'application/json'}, timeout=5)
print(response)"""

"""response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
               json ={
                "name": "Avicii",
                "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                headers= {'Content-Type':'application/json',
                         "trainer_token": "2ddf82170250fa8958d0af5081a419ca"},
                )
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')"""

"""response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
               json ={
                "pokemon_id": "21039",
                "name": "Tiesto",
                "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                headers= {'Content-Type':'application/json',
                         "trainer_token": "2ddf82170250fa8958d0af5081a419ca"},
                )
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')"""

"""response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
               json ={"pokemon_id": "21039"},
                headers= {'Content-Type':'application/json',
                         "trainer_token": "2ddf82170250fa8958d0af5081a419ca"},
                )
print(f'Code:{response.status_code} - {response.reason}. Message:{response.text}')"""
