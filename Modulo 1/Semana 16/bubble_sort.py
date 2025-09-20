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

def validate_numbers(func):
    def wrapper(list_of_numbers):
            for element in list_of_numbers:
                if isinstance(element, int) == False and isinstance(element, float) == False :
                    raise TypeError('Error: La lista contiene elementos no numéricos')
            return func(list_of_numbers) # Primero se hace la validacion, despues se ejecuta la func(*args)
    return wrapper

def validate_non_empty_list(func):
    def wrapper(arg):
        if not arg:
            raise ValueError('Error: La lista esta vacia')
        return func(arg)
    return wrapper


@validate_non_empty_list
@validate_numbers
def bubble_sort(unsorted_list):
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
            return unsorted_list
        iteration += 1
    print(f'Lista ordenada: {unsorted_list}')
    print(f'Iteraciones: {iteration}')
    print(f'Intercambios: {flippings}')
    return unsorted_list





