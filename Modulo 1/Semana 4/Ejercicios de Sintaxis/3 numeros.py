print("Ingrese 3 números y se mostrará el mayor de ellos")
user_number1 = float(input("1er numero: "))
user_number2 = float(input("2do numero: "))
user_number3 = float(input("3er numero: "))
if user_number1 > user_number2 and user_number1 > user_number3:
    print(f"El mayor es: {user_number1}")
elif user_number2 > user_number3:
    print(f"El mayor es: {user_number2}")
else:
    print(f"El mayor es: {user_number3}")
    