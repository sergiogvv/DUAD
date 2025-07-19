from colorama import Fore, init
init(autoreset=True)  # Initialize colorama for Windows


def enter_student():
    name = input('\nNombre completo: ')
    grade_and_section = input('Seccion: ') 
    while True:
        spanish_grade = input('Nota de español: ')
        if check_if_valid(spanish_grade):
            spanish_grade = float(spanish_grade)
            break  
    while True:
        english_grade = input('Nota de inglés: ')
        if check_if_valid(english_grade):
            english_grade = float(english_grade)
            break 
    while True:
        social_studies_grade = input('Nota de sociales: ')
        if check_if_valid(social_studies_grade):
            social_studies_grade = float(social_studies_grade) 
            break
    while True:
        science_grade = input('Nota de ciencias: ')
        if check_if_valid(science_grade):
            science_grade = float(science_grade) 
            break
    student_dict = {
        'name': name,
        'section': grade_and_section,
        'spanish': spanish_grade,
        'english': english_grade,
        'social_s': social_studies_grade,
        'science': science_grade}
    return student_dict


def check_if_valid(number):
        try:
            number = float(number)    
            if number < 0:
                raise ValueError()
            if number > 100:
                raise ValueError()
            else:
                return True
        except:
            print(Fore.RED +'Error: Valor inválido, ingrese un numero ente 0 y 100')        


def enter_information_4_all_students(number_of_students):
    student_grade_list = []
    for i in range(number_of_students):
        student_grade_list.append(enter_student())
    while True:
        try:
            add_more=input('\n¿Desea ingresar otro estudiante [s/n] ? ')
            if add_more == 's':
                student_grade_list.append(enter_student())
                break
            if add_more == 'n':
                break
            else:
                raise ValueError()
        except:
            print(Fore.RED +'Error: Respuesta inválida, digite "s" para ingresar otro estudiante, "n" para no agregar mas')
    return student_grade_list


def english_headers(student_grade_list):
    english_dict = {} #to be used to show information in english
    student_grade_list_ENG_headers = [] #to be used to show information in english
    for student in student_grade_list:
        english_dict = {
        'name': student['Nombre'],
        'section': student['Seccion'],
        'spanish': float(student['Español']),
        'english': float(student['Inglés']),
        'social_s': float(student['Sociales']),
        'science': float(student['Ciencias'])
        } 
        student_grade_list_ENG_headers.append(english_dict)
    return student_grade_list_ENG_headers


def spanish_headers(student_grade_list):
    spanish_dict = {} #to be used to show information in spanish
    student_grade_list_ESP_headers = [] #to be used to show information in spanish
    for student in student_grade_list:
        spanish_dict = {  
        'Nombre': student['name'],
        'Seccion': student['section'],
        'Español': student['spanish'],
        'Inglés': student['english'],
        'Sociales': student['social_s'],
        'Ciencias': student['science'],
        }
        student_grade_list_ESP_headers.append(spanish_dict)
    return student_grade_list_ESP_headers

def view_student_grades(student_grade_list):
    dict_print = spanish_headers(student_grade_list)
    for student in dict_print:
        print(student)


def student_avg_grade(student):
	avg_grade = (student['spanish']+student['english']+student['social_s']+student['science'])/4
	return avg_grade


def sort_students_by_avg_grade(student_grade_list):
    # Outer loop to iterate through the list n times
    for n in range(len(student_grade_list)-1,0, -1):
        # Initialize swapped to track if any swaps occur
        swapped = False
        # Inner loop to compare adjacent elements
        for i in range(n):
            if student_avg_grade(student_grade_list[i]) < student_avg_grade(student_grade_list[i+1]):
                # Swap elements if they are in the wrong order
                student_grade_list[i], student_grade_list[i+1] = student_grade_list[i+1], student_grade_list[i]
                # Mark that a swap has occurred
                swapped = True
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
    return student_grade_list


def top_3_students_by_avg_grade(student_grade_list):
    list_of_avg_grades_by_student = []
    sorted_student_grades = sort_students_by_avg_grade(student_grade_list)
    for student in sorted_student_grades: 
        dict_student_with_avg_grade = {}
        student_avg = student_avg_grade(student)
        dict_student_with_avg_grade['name'] = student['name']
        dict_student_with_avg_grade['avg'] = student_avg
        list_of_avg_grades_by_student.append(dict_student_with_avg_grade)
    print()
    if len(list_of_avg_grades_by_student) < 3:
        for i in range(len(list_of_avg_grades_by_student)):         
            print(f'Nombre: {list_of_avg_grades_by_student[i]['name']}\tPromedio: {list_of_avg_grades_by_student[i]['avg']}')
    else:
        for i in range(3):
            print(f'Nombre: {list_of_avg_grades_by_student[i]['name']}\tPromedio: {list_of_avg_grades_by_student[i]['avg']}')
    print()


def all_grade_avg(student_grade_list):
    sum_student_avg = 0
    for student in student_grade_list: 
        student_avg = student_avg_grade(student)
        sum_student_avg+=student_avg
    avg_grade_for_all_students = sum_student_avg/len(student_grade_list)
    print(f'Nota promedio entre las notas de todos los estudiantes: {avg_grade_for_all_students}')


