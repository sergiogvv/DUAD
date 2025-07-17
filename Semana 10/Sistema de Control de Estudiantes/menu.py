from actions import enter_information_4_all_students, view_student_grades, top_3_students_by_avg_grade, all_grade_avg

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
        try:
            n = int(n)
            if n > 0:
                return True
            else:
                raise ValueError()
        except:
            print('Valor inválido: Ingrese un numero mayor a cero')


def print_menu():
    print('\nMenu de opciones:\n')
    print('1. Ingresar información de estudiantes')
    print('2. Ver la información de todos los estudiantes ingresados')
    print('3. Ver el top 3 de los estudiantes con la mejor nota promedio')
    print('4. Ver la nota promedio entre las notas de todos los estudiantes')
    print('5. Exportar todos los datos actuales a un archivo CSV')
    print('6. Importar los datos de un archivo CSV previamente exportado')
    print('7. Salir del programa\n')



def execute_menu():
    student_grade_list = []
    while True:
        print_menu()
        while True:
            option = input('Ingrese una opción: ')
            if valid_menu_option(option):
                option = int(option)
                break
        if option == 1:
            while True:
                n=input('Ingrese la cantidad de estudiantes cuya informacion desea ingresar: ')
                if valid_number_of_students(n):
                    n=int(n)
                    student_grade_list += enter_information_4_all_students(n)
                    break
        if option == 2:
            view_student_grades(student_grade_list)
        if option == 3:
            top_3_students_by_avg_grade(student_grade_list)
        if option == 4:
            all_grade_avg(student_grade_list)
        if option == 5:
            continue
        if option == 6:
            pass
        if option == 7:
            exit() 
        else:
            input('\n...presione cualquier tecla para continuar...')
        


execute_menu()



# while True:
#     option = input('Ingrese una opción: ')
#     if valid_menu_option(option):
#         option = int(option)
#         break
# while True:
#     n=input('numero de estudiantes: ')
#     if valid_number_of_students(n):
#         n=int(n)
#         break