from datetime import date

def log_call(func):
    def wrapper(*args): 
        print(f'function: {func.__name__} - args: {args} - {date.today()} - Resultado: {func(*args)} ')
        return func(*args)
    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        
        for arg in args:
            if isinstance(arg, int) == False and isinstance(arg, float) == False :
                raise ValueError('Esta funcion posee argumentos que no son numeros')
        result = func(*args)
        return result 
    return wrapper


@validate_numbers
@log_call
def multiply(number_1,number_2):
    return number_1*number_2


#En este ejemplo se observo que cuando el return no se incluia dentro de la funcion wrapper, su retorno no se guardaba en memoria haciendo que el resultado de la funcion decorada fuera None


print(f'Resultado {multiply('k',4)}')
print('\n\n')

product =multiply(3,4)
print(f'Restultado {product}')