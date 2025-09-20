import random
secret_number = random.randint(1, 10)
user_number = 0
while (user_number != secret_number):
    user_number = int(input("Adivina el número secreto entre 1 y 10: "))
    if user_number > 10 or user_number < 1:
        print("Número fuera de rango, debe ser entre 1 y 10.")
    elif user_number == secret_number:
        print("¡Felicidades! Has adivinado el número secreto.")
    else:
        print("Número incorrecto, inténtalo de nuevo.")

