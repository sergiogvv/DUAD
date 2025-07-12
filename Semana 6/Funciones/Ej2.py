#def print_label1():
#    print("label 1")
#    text1 = "one"


#print(text1)

text1 = "one"

def print_text1():
    global text1
    text1 = "new text one"
    print("""""")
    print(f"El valor de text1 dentro de la funcion print_text1 es: {text1}")
    print("""""")
    

print(f"valor de la variable global text1: {text1}")

print_text1()

print(f"Valor de la variable text1 despues de haber corrido la funcion print_text1: {text1}")

