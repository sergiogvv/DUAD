#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

from datetime import date


def validate_numbers(func):
    def wrapper(*args):
            for arg in args:
                if isinstance(arg, int) == False and isinstance(arg, float) == False :
                    raise ValueError('Esta funcion posee argumentos que no son numeros')
            func(*args) # Primero se hace la validacion, despues se ejecuta la func(*args)
    return wrapper
   

@validate_numbers
def add(a,b):
    add = a + b
    print (f'{a}+{b} = {add}')


my_number = 5.5
my_other_number = 5
my_string = 'Hola'
my_2nd_string = ' mundo!'

age_and_experience(my_birthday,my_experience)
print()
add(my_number,my_other_number)
print()
add(my_string,my_2nd_string)
