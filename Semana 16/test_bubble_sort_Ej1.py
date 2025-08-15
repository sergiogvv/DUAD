# 1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
#     1. Funciona con una lista pequeña.
#     2. Funciona con una lista grande (de más de 100 elementos.)
#     3. Funciona con una lista vacía.
#     4. No funciona con parámetros que no sean una lista.
import pytest
from bubble_sort import bubble_sort

def test_bubble_sort_returns_result_with_short_list():
    #Arrange: Lista de entrada
    my_test_list = [18, -11, 68, 6, 32, 53, -2]
    #Act
    result = bubble_sort(my_test_list)
    #Assert
    assert result == [-11, -2, 6, 18, 32, 53, 68]


def test_bubble_sort_returns_result_with_large_list():
    #Arrange: Lista de entrada
    my_test_list = [472, 85, 913, 628, 134, 791, 256, 390, 678, 12, 843, 301, 98, 715, 667, 59, 284, 503, 720, 149, 366, 901, 237, 41, 654, 788, 112, 329, 870, 245, 697, 5, 183, 92, 814, 376, 621, 58, 964, 210, 347, 631, 799, 123, 440, 17, 553, 289, 690, 38, 741, 206, 314, 872, 66, 497, 185, 960, 74, 328, 888, 103, 222, 456, 648, 11, 583, 934, 142, 379, 268, 726, 94, 861, 707, 350, 219, 476, 808, 33, 695, 120, 604, 172, 398, 777, 268, 84, 517, 640, 232, 93, 712, 860, 346, 264, 441, 682, 199, 870]
    #Act
    result = bubble_sort(my_test_list)
    #Assert
    assert result == [5, 11, 12, 17, 33, 38, 41, 58, 59, 66, 74, 84, 85, 92, 93, 94, 98, 103, 112, 120, 123, 134, 142, 149, 172, 183, 185, 199, 206, 210, 219, 222, 232, 237, 245, 256, 264, 268, 268, 284, 289, 301, 314, 328, 329, 346, 347, 350, 366, 376, 379, 390, 398, 440, 441, 456, 472, 476, 497, 503, 517, 553, 583, 604, 621, 628, 631, 640, 648, 654, 667, 678, 682, 690, 695, 697, 707, 712, 715, 720, 726, 741, 777, 788, 791, 799, 808, 814, 843, 860, 861, 870, 870, 872, 888, 901, 913, 934, 960, 964]


def test_bubble_sort_returns_result_with_empty_list():
    #Arrange
    my_test_list = []
    #Act and Assert
    with pytest.raises(ValueError):
        bubble_sort(my_test_list)


def test_bubble_sort_returns_exception_with_non_numeric_list():
    #Arrange
    my_test_list = ['cinco', 4,'tres', 2, 'uno']
    #Act and Assert
    with pytest.raises(TypeError):
        bubble_sort(my_test_list)







