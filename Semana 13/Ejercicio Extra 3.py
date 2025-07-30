from datetime import date

def log_call(func):
    def wrapper(*args):
        print(f'{func}')
        for index, arg in enumerate(args):
            print(f"Arg {index}: {arg}")
        print(date.today())
        func(*args)
    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        func(*args)
        try:
            for arg in args:
                if isinstance(arg, int) == False and isinstance(arg, float) == False :
                    raise ValueError()
        except:
            print('Error: Esta funcion posee argumentos que no son numeros')
    return wrapper


@validate_numbers
@log_call
def multiply(number_1,number_2):
    product = number_1*number_2
    print(f'Resultado {product}')



multiply('k',4)
print('\n\n')
multiply(3,4)