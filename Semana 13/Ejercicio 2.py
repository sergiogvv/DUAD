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
def age_and_experience(date_of_birth,date_of_first_job):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    experience = today.year - date_of_first_job.year - ((today.month, today.day) < (date_of_first_job.month, date_of_first_job.day))
    print(f'Su edad es {age} años y su experiencia es {experience} años')   

@validate_numbers
def add(a,b):
    add = a + b
    print (f'{a}+{b} = {add}')



my_birthday = date(1985,3,20)
my_experience = date(2011,2,15)
my_number = 5.5
my_other_number = 5
my_string = 'Hola'
my_2nd_string = ' mundo!'

age_and_experience(my_birthday,my_experience)
print()
add(my_number,my_other_number)
print()
add(my_string,my_2nd_string)