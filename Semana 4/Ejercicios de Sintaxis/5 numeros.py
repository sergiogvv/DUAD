print("Ingrese 5 numeros enteros:")
index = 0
mayor = 0
while index < 5:
    num = int(input())
    if num > mayor:
        mayor = num
    index += 1

print("El numero mayor es:", mayor)
# Este código solicita al usuario ingresar 5 números enteros y determina cuál es el mayor de ellos