time_seconds = int(input("Ingrese tiempo en segundos: "))
if time_seconds < 600:
    rest = 600 - time_seconds
    print(f"El tiempo restante para llegar a 600 segundos es: {rest} segundos")
elif time_seconds == 600:
    print("igual")
else:
    print("mayor")

