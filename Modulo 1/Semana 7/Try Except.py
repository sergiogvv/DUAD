# try:
#     name = input("Ingrese su nombre: ")
#     if name.isdigit():
#       raise ValueError()
# except Exception as error:
# 	  # unhappy path
#     print("Su nombre no puede ser un numero!")
    

# happy path
# edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
# empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")

def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('El numero es muy bajo')
	elif number > 100:
		raise ValueError('El numero es muy alto')
	

def main():
	number = input('Ingrese un numero ')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except Exception as ex:
		print(f'Error: {ex}')


if __name__ == '__main__':
	main()

# def ask_for_user_information():
# 	try:
# 		age = int(input('Ingrese su edad'))
# 		if age < 1 or age > 100:
# 			raise ValueError()

# 	except ValueError as ex:
# 		print("Ingrese una edad valida!")
# 		raise ex


# def main():
# 	try:
# 		ask_for_user_information()
# 		# create_order()

# 	except Exception as ex:
# 		exit()


# if __name__ == '__main__':
# 	main()