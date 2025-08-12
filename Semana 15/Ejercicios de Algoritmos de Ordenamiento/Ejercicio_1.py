# 1. Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
# (pasos implementados del ejercicio extra 2 y 3)
# 2. Conteo de pasos (`bubble_sort_steps`)
#     - Modifique su implementación de `bubble_sort` para que:
#         - Cuente cuántas iteraciones (pasadas) realiza el algoritmo
#         - Cuente cuántos intercambios se hicieron en total
# 3. Validación de entrada antes de ordenar
#     - Cree una función que reciba una lista y valide:
#         - Que todos los elementos sean números
#         - Que no esté vacía
#         - Luego aplique `bubble_sort` si pasa las validaciones
#         - Si hay error, debe lanzar un mensaje apropiado


def bubble_sort(unsorted_list):
    try:
        if not unsorted_list:
            raise ValueError
        for element in unsorted_list:
            if not str(element).isdigit():
                raise TypeError
        flippings = 0
        iteration = 0
        for j in range(0,len(unsorted_list)-1):
            flipped = False
            
            for i in range(0,len(unsorted_list)-1-j):
                current = unsorted_list[i]
                next = unsorted_list[i+1]
            
                if current > next:
                    unsorted_list[i+1] = current
                    unsorted_list[i] = next
                    flipped = True
                    flippings += 1
            if flipped == False:
                print(f'Lista ordenada: {unsorted_list}')
                print(f'Iteraciones: {iteration}')
                print(f'Intercambios: {flippings}')
                return
            iteration += 1
        print(f'Lista ordenada: {unsorted_list}')
        print(f'Iteraciones: {iteration}')
        print(f'Intercambios: {flippings}')
    except ValueError:
        print("Error: La lista esta vacia")
    except TypeError:
        print("Error: La lista contiene elementos no numéricos")


# my_test_list = []
# my_test_list = ['cinco', 4,'tres', 2, 'uno']
my_test_list = [5,4,3,2,1]
bubble_sort(my_test_list)



