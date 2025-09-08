print("Ingrse 3 numeros enteros cualquiera")
number1 = int(input("Primer numero: "))
number2 = int(input("Segundo numero: "))
number3 = int(input("Tercer numero: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
    print("Correcto")
else:
    print("Incorrecto")