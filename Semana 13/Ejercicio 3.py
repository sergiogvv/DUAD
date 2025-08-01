#3. Cree una clase de `User` que:
#    - Tenga un atributo de `date_of_birth`.
#    - Tenga un property de `age`.
#    
#    Luego cree un decorador para funciones que acepten un `User` 
#    como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

def validate_age(func):
    def wrapper(user,*args):
        if user.age < 18:
            raise PermissionError('El usuario es menor de edad')
        else:
            print('Acceso concedido: el usuario es mayor de edad')
        func(user,*args) # Primero se hace la validacion, despues se ejecuta la func(*args)
    return wrapper


class User:
    date_of_birth: date
    user_name: str

    def __init__(self, user_name, date_of_birth):
        self.date_of_birth = date_of_birth
        self.user_name = user_name

    @property
    def age(self):
        # Debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


@validate_age
def get_a_beer(user):
    print(f'{user.user_name} ha ordenado una cerveza')


my_user = User('sergiogvv',date(1985, 3, 20))
print(f"Hola soy {my_user.user_name} y tengo {my_user.age} años")
print()
get_a_beer(my_user)
print()
another_user = User('C-3PO',date(2008, 4, 14))
print(f"Hola soy {another_user.user_name} y tengo {another_user.age} años")
print()
get_a_beer(another_user)