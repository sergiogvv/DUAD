

def valid_menu_option(option):
    try:
        option = int(option)
        if option in [1,2,3,4,5,6,7]:
            return True
        else:
            raise ValueError()
    except:
        print('Opcion inválida, ingrese un numero ente 1 y 7')


def valid_number_of_students(n):
    while True:
        try:
            n = int(n)
            if n > 0:
                return True
            else:
                raise ValueError()
        except:
            print('Ingrese un numero mayor a cero')

        
def execute_option(option):
    if option == 1:
        while True:
            n=input('Ingrese la cantidad de estudiantes cuya informacion desea ingresar: ')
            if valid_number_of_students(n):
                n=int(n)
                #enter_information_4_all_students(n)
                break
    if option == 2:
        pass
    if option == 3:
        pass
    if option == 4:
        pass
    if option == 5:
        pass
    if option == 6:
        pass
    else:
        exit()   





while True:
    option = input('Ingrese una opción: ')
    if valid_menu_option(option):
        option = int(option)
        break
while True:
    n=input('numero de estudiantes: ')
    if valid_number_of_students(n):
        n=int(n)
        break