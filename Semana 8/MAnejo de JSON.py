import json

def open_and_print_file(path):
	with open(path) as file:
		print(file.read())
		

def write_text_to_file(file_path, text):
  with open(file_path, 'w') as file:
    file.write(text)
		


Pokemons_JSON= """[{"name": {"english": "Pikachu"},"type": ["Electric"],"base": {"HP": 35,"Attack": 55,"Defense": 40,"Sp. Attack": 50,"Sp. Defense": 50,"Speed": 90}},{"name": {"english": "Charmander"},"type": ["Fire"],"base": {"HP": 39,"Attack": 52,"Defense": 43,"Sp. Attack": 60,"Sp. Defense": 50,"Speed": 65}},{"name": {"english": "Squirtle"},"type": ["Water"],"base": {"HP": 44,"Attack": 48,"Defense": 65,"Sp. Attack": 50,"Sp. Defense": 64,"Speed": 43}}]"""

# parse Pokemons_JSON:
Pokemons_Py = json.loads(Pokemons_JSON)


print('Ingrese la informacion del Pokemon que desea agregar a la lista llenando la informacion del formulario')
p_name = input('name: ')
p_type = input('type: ')
print('base')
p_HP = int(input('HP: '))
p_Attack = int(input('Attack: '))
p_Defense = int(input('Defense: '))
p_Sp_Attack = int(input('Sp. Attack: '))
p_Sp_Defense = int(input('Sp. Defense: '))
p_Speed = int(input('Speed: '))

New_Pokemon = {
    'name':{'english':p_name},
    'type':[p_type],
    'base':{
        'HP': p_HP, 
        'Attack': p_Attack, 
        'Defense': p_Defense, 
        'Sp. Attack': p_Sp_Attack, 
        'Sp. Defense': p_Sp_Defense, 
        'Speed': p_Speed
    }
}

Pokemons_Py.append(New_Pokemon)

Pokemons_JSON_updated = json.dumps(Pokemons_Py, indent=4)
print('JSON Object:\n')
print(Pokemons_JSON_updated)

write_text_to_file('Semana 8/Pokemons.json',Pokemons_JSON_updated)








