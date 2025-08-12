#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero

def validate_numbers(func):
    def wrapper(list_of_numbers):
            for element in list_of_numbers:
                if isinstance(element, int) == False and isinstance(element, float) == False :
                    raise TypeError('Error: La lista contiene elementos no numéricos')
            func(list_of_numbers) # Primero se hace la validacion, despues se ejecuta la func(*args)
    return wrapper

def validate_non_empty_list(func):
    def wrapper(arg):
        if not arg:
            raise ValueError('Error: La lista esta vacia')
        func(arg)
    return wrapper

@validate_non_empty_list
@validate_numbers
def bubble_sort(unsorted_list):
    flippings = 0
    iteration = 0
    for j in range(0,len(unsorted_list)-1):
        flipped = False
        
        for i in range(len(unsorted_list)-1,0+j,-1):
            current = unsorted_list[i]
            next = unsorted_list[i-1]
        
            if current < next:
                unsorted_list[i-1] = current
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


# my_test_list = []
# my_test_list = ['cinco', 4,'tres', 2, 'uno']
my_test_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(my_test_list)



