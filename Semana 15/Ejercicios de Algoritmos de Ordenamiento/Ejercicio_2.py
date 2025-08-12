#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero


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
    except ValueError:
        print("Error: La lista esta vacia")
    except TypeError:
        print("Error: La lista contiene elementos no numéricos")


# my_test_list = []
# my_test_list = ['cinco', 4,'tres', 2, 'uno']
my_test_list = [5,4,3,2,1]
bubble_sort(my_test_list)



