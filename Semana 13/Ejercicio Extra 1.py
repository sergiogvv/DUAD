def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        func(*args)
    return wrapper

@repeat_twice
def print_greeting_name(name):
    print(f'Hola, {name}')



name = 'Sergio'
print_greeting_name(name)

print_greeting_name('Luke Skywalker')