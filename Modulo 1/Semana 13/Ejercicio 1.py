# Cree un decorador que haga print de los parámetros y retorno de la función que decore.
from datetime import date

def print_parameters(func):
    def wrapper(*args):
        for index, arg in enumerate(args):
            print(f"Arg {index}: {arg}")
        func(*args)
    return wrapper


@print_parameters
def age_and_experience(date_of_birth,date_of_first_job):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    experience = today.year - date_of_first_job.year - ((today.month, today.day) < (date_of_first_job.month, date_of_first_job.day))
    print(f'Su edad es {age} años y su experiencia es {experience} años')    



my_birthday = date(1985,3,20)
my_experience = date(2011,2,15)


age_and_experience(my_birthday,my_experience)