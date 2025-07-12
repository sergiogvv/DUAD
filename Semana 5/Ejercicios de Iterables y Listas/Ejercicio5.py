print("ingrese 10 numeros enteros cualesquiera: ")
list = []
for i in range(10):
    element = int(input(f"Ingrese el elemento {i+1}: "))
    list.append(element)
mayor = 0
for element in list:
    if element > mayor:
        mayor = element
    

print(f'{list}. El más alto fue {mayor}')