
def sum(number_1,number_2):
    return number_1+number_2


def subtract(number_1,number_2):
    return number_1-number_2


def multiply(number_1,number_2):
    return number_1*number_2


def divide(number_1,number_2):
    try:
        return number_1/number_2
    except ZeroDivisionError:
        print('Error: División entre cero')
        return number_1


def operation(string, float1, float2):
    if string == '+':
        return sum(float1,float2)
    elif string == '-':
        return subtract(float1,float2) 
    elif string == '*':
        return multiply(float1,float2)
    elif string == '/':
        return divide(float1,float2)
    elif string == 'x' or string == 'X':
        return 0


def validate_option(value):
    if value == 'x' or value == 'X':
        return '0'
    elif value == '-':
        return value 
    elif value == '*':
        return value
    elif value == '/':
        return value
    elif value == '+':
        return value
    elif value.isdigit():
        return value
    else:
        raise ValueError

def main():
    actual_number = 0
    print('\nCALCULADORA')
    while True:
        try:
            print(f'\n{actual_number}')
            print(f'\n[ + ]  [ - ]  [ * ]  [ / ]   [ x ]   (Ingrese un numero, elija una operacion dentro de los signos [ ], la "x" borra el resultado )')
            print('')

            operation_option = validate_option(input())
            if operation_option.isdigit():
                actual_number = float(operation_option)
                continue
            entered_number = float(input(f'(Ingrese un numero) '))

            actual_number = operation(operation_option, actual_number, entered_number)

        except ValueError:
            print('Error: numero u operacion invalida')
            continue

if __name__ == "__main__":
    main()