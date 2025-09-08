import csv

def read_csv_file(file_path):
  with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
      print(row)


def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(data)


def register_game(games):
  games_list = []
  
  ESRB_rating = ['', 'E', 'E10+', 'T', 'M', 'AO']
  for i in range(n):
    game_register = {}
    print(f'\nRegistrando juego {i+1}')
    game_register['Nombre']=  input('Ingrese el nombre del videojuego: ')
    game_register['Genero']=  input('Ingrese el género: ')
    game_register['Desarrollador']=  input('Ingrese el desarrollador: ')
    print('Selecione la clasificación ESRB de lista\n\t0. Sin clasificación\n\t1. E\n\t2. E10+\n\t3. T\n\t4. M\n\t5. AO ')
    ESRB = int(input())
    game_register['Clasificación ESRB']= ESRB_rating[ESRB]
    games_list.append(game_register)

  return games_list, game_register.keys()


  
n= int(input('Ingrese la cantidad de videojuegos que desea registrar '))
csv_data, csv_headers = register_game(n)
write_csv_file('Semana 8/Lista de videojuegos.csv', csv_data, csv_headers)


