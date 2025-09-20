from actions import enter_information_4_all_students, view_student_grades, top_3_students_by_avg_grade, all_grade_avg, spanish_headers, english_headers
from data import import_csv_file, write_csv_file
from colorama import Fore, init
init(autoreset=True)  # Initialize colorama for Windows


def valid_menu_option(option):
    try:
        option = int(option)
        if option in [1,2,3,4,5,6,7]:
            return True
        else:
            raise ValueError()
    except:
        print(Fore.RED +'Error: Opcion inválida, ingrese un numero ente 1 y 7')


def valid_number_of_students(n):
        try:
            n = int(n)
            if n > 0:
                return True
            else:
                raise ValueError()
        except:
            print(Fore.RED +'Error: Valor inválido: Ingrese un numero mayor a cero')


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
            if  student_grade_list:
                view_student_grades(student_grade_list)
            else: 
                print(Fore.RED +'\nError: Primero debe ingresar o importar la información de estudiantes')
        if option == 3:
            if student_grade_list:
                top_3_students_by_avg_grade(student_grade_list)
            else:
                print(Fore.RED +'\nError: Primero debe ingresar o importar la información de estudiantes')
        if option == 4:
            if student_grade_list:
                all_grade_avg(student_grade_list)
            else:
                print(Fore.RED +'\nError: Primero debe ingresar o importar la información de estudiantes')   
        if option == 5:
            if student_grade_list:
                headers = ['Nombre', 'Seccion', 'Español', 'Inglés', 'Sociales', 'Ciencias']
                data = spanish_headers(student_grade_list)
                file_path = 'C:/Users/sergi/OneDrive/Documents/Lyfter/Repos/DUAD/DUAD/Semana 10/Sistema de Control de Estudiantes/Data/Student_Info.csv'
                write_csv_file(file_path, data , headers)
            else:
                print(Fore.RED +'\nError: Primero debe ingresar o importar la información de estudiantes') 
        if option == 6:
            file_path = 'C:/Users/sergi/OneDrive/Documents/Lyfter/Repos/DUAD/DUAD/Semana 10/Sistema de Control de Estudiantes/Data/Student_Info.csv'
            try:
                student_grade_list = import_csv_file(file_path)
                student_grade_list = english_headers(student_grade_list)
            except:
                print(Fore.RED +'\nError: Archivo de datos no encontrado, debe ingresar información y luego expotar los datos')
        if option == 7:
            exit() 
        else:
            input(Fore.LIGHTGREEN_EX +'\n...presione la tecla ENTER para continuar...')







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