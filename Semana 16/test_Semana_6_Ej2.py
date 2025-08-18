import pytest
from Semana_6.Ej3 import sum_list
from Semana_6.Ej4 import reverse_string
from Semana_6.Ej5 import upper_lower
from Semana_6.Ej6 import sort_words
from Semana_6.Ej7 import is_prime, list_primes

# test sum_list
def test_sum_list_result_with_short_list():
    #Arrange
    test_list = [18, -11, 68, 6, 32, 53, -2]
    #Act
    result = sum_list(test_list)
    #Assert
    assert result == 164

def test_sum_list_result_w_large_list():
    #Arrange
    test_list = [472, 85, 913, 628, 134, 791, 256, 390, 678, 12, 843, 301, 98, 715, 667, 59, 284, 503, 720, 149, 366, 901, 237, 41, 654, 788, 112, 329, 870, 245, 697, 5, 183, 92, 814, 376, 621, 58, 964, 210, 347, 631, 799, 123, 440, 17, 553, 289, 690, 38, 741, 206, 314, 872, 66, 497, 185, 960, 74, 328, 888, 103, 222, 456, 648, 11, 583, 934, 142, 379, 268, 726, 94, 861, 707, 350, 219, 476, 808, 33, 695, 120, 604, 172, 398, 777, 268, 84, 517, 640, 232, 93, 712, 860, 346, 264, 441, 682, 199, 870]
    #Act
    result = sum_list(test_list)
    #Assert
    assert result == 43313

def test_sum_list_result_w_empty_list():
    #Arrange
    test_list = []
    #Act
    result = sum_list(test_list)
    #Assert
    assert result == 0

# test reverse_string

def test_reverse_string_result_with_short_string():
    #Arrange
    test_string= 'Hola mundo'
    #Act
    result = reverse_string(test_string)
    #Assert
    assert result == 'odnum aloH'

def test_reverse_string_result_with_paragraph_string():
    #Arrange
    test_string= 'Rugen runs away. Inigo chases him throughout the castle until Rugen suddenly throws a knife at him and seriously wounds him, mocking his quest as he prepares to deliver the fatal blow. At the last second, Inigo recovers his strength and duels his father''s murderer, repeating his fateful words as he corners Rugen, inflicting on him the same dueling scars. Rugen begs for his life and offers to give Inigo anything he wants before trying to attack him again; Inigo catches Rugen''s sword arm and replies, "I want my father back, you son of a bitch," as he kills him.'
    #Act
    result = reverse_string(test_string)
    #Assert
    assert result == '.mih sllik eh sa ",hctib a fo nos uoy ,kcab rehtaf ym tnaw I" ,seilper dna mra drows sneguR sehctac oginI ;niaga mih kcatta ot gniyrt erofeb stnaw eh gnihtyna oginI evig ot sreffo dna efil sih rof sgeb neguR .sracs gnileud emas eht mih no gnitcilfni ,neguR srenroc eh sa sdrow lufetaf sih gnitaeper ,reredrum srehtaf sih sleud dna htgnerts sih srevocer oginI ,dnoces tsal eht tA .wolb lataf eht reviled ot seraperp eh sa tseuq sih gnikcom ,mih sdnuow ylsuoires dna mih ta efink a sworht ylneddus neguR litnu eltsac eht tuohguorht mih sesahc oginI .yawa snur neguR'

def test_reverse_string_result_with_empty_string():
    #Arrange
    test_string= ''
    #Act
    result = reverse_string(test_string)
    #Assert
    assert result == ''


# test upper_lower
def test_upper_lower_result_with_short_string():
    #Arrange
    test_string= 'WTF stands for World Trade Federation'
    #Act
    result = upper_lower(test_string)
    #Assert
    assert result == (6,26)

def test_upper_lower_result_with_long_string():
    #Arrange
    test_string= 'Rugen runs away. Inigo chases him throughout the castle until Rugen suddenly throws a knife at him and seriously wounds him, mocking his quest as he prepares to deliver the fatal blow. At the last second, Inigo recovers his strength and duels his father''s murderer, repeating his fateful words as he corners Rugen, inflicting on him the same dueling scars. Rugen begs for his life and offers to give Inigo anything he wants before trying to attack him again; Inigo catches Rugen''s sword arm and replies, "I want my father back, you son of a bitch," as he kills him.'
    #Act
    result = upper_lower(test_string)
    #Assert
    assert result == (11,439)

def test_upper_lower_result_with_empty_string():
    #Arrange
    test_string= ''
    #Act
    result = upper_lower(test_string)
    #Assert
    assert result == (0,0)


# test sort_words
def test_sort_words_result_with_long_string():
    #Arrange
    test_string= 'python-variable-funcion-computadora-monitor'
    #Act
    result = sort_words(test_string)
    #Assert
    assert result == 'computadora-funcion-monitor-python-variable'

def test_sort_words_result_with_empty_string():
    #Arrange
    test_string = ''
    #Act
    result = sort_words(test_string)
    #Assert
    assert result == ''

def test_sort_words_result_with_no_dash_string():
    #Arrange
    test_string= 'python variable funcion computadora monitor'
    #Act
    result = sort_words(test_string)
    #Assert
    assert result == 'python variable funcion computadora monitor'


# test list_primes
def test_list_primes_with_short_list():
    #Arrange
    test_list = [1, 4, 6, 7, 13, 9, 67]
    #Act
    result = list_primes(test_list)
    #Assert
    assert result == [7, 13, 67]

def test_list_primes_with_list_from_0_to_1200():
    #Arrange
    test_list = range(0,1200)
    #Act
    result = list_primes(test_list)
    #Assert
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193]

def test_list_primes_with_even_numbers_from_0_to_1000000():
    #Arrange
    test_list = range(0,1000000,2)
    #Act
    result = list_primes(test_list)
    #Assert
    assert result == [2]