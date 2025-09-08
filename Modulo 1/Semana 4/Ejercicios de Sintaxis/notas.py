grade_counter = 1
approved_grades = 0
failed_grades = 0
avg_approved = 0
avg_failed = 0
avg_all_grades = 0

print("Ingrese la cantidad de notas")
grade_quantity = int(input())
while grade_counter <= grade_quantity:  
    print(f"Ingrese la nota numero {grade_counter}")
    grade = int(input())
    
    if grade < 70:
        failed_grades += 1
        avg_failed += grade
    else:
        approved_grades += 1
        avg_approved += grade
    
    avg_all_grades += (grade/grade_quantity)
    grade_counter += 1

avg_approved = avg_approved / approved_grades if approved_grades > 0 else 0
avg_failed = avg_failed / failed_grades if failed_grades > 0 else 0

print(f"El estudiante tiene esta cantidad de notas aprobadas {approved_grades}")
print(f"Este es el promedio de notas aprobadas {avg_approved}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas {failed_grades}")
print(f"Este es el promedio de notas desaprobadas {avg_failed}")
print(f"Este es el promedio total de notas {avg_all_grades}")





