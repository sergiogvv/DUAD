i=0
while (i < 2):
    n = int(input("Ingrese la cantidad de elementos de su lista: "))
    if n<2:
        print("La lista debe contener al menos 2 elementos")
    list = []
    i=n

for i in range(n):
    element = int(input(f"Ingrese el elemento {i+1}: "))
    list.append(element)

print("Su lista:", list)


for i in range(len(list)-1,-1,-1):
    if list[i] % 2 != 0:
        list.pop(i)


print(list)