i=0
while (i < 2):
    n = int(input("Ingrese la cantidad de elementos de su lista: "))
    if n<2:
        print("La lista debe contener al menos 2 elementos")
    list = []
    i=n

for i in range(n):
    element = input(f"Ingrese el elemento {i+1}: ")
    list.append(element)

print("Su lista:", list)

print("Intercambiando el primer y ultimo elemento de su lista")
first_element = list[0]
last_element = list[n-1]
list[0]=last_element
list[n-1]=first_element
print("Su lista modificada:", list)