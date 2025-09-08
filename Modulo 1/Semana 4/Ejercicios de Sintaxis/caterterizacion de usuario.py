nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
print(f"Hola {nombre} {apellido}, tienes {edad} años.")

if edad < 2:
    print("Eres un bebé.")
elif 2 <= edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 15:
    print("Eres un preadolescente.")
elif 15 <= edad < 25:
    print("Eres un adolescente.")
elif 25 <= edad < 35:  
    print("Eres un adulto joven.") 
elif 35 <= edad < 65:
    print("Eres un adulto.") 
else:
    print("Eres un adulto mayor.")