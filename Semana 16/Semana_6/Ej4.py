def reverse_string(string):
    reversed = ""
    for index in range(len(string)-1, -1,-1):
        reversed += string[index]
    return reversed


my_string = ''
print(reverse_string(my_string))