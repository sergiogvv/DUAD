user_logged_in = False

def requires_login(func):
    def wrapper(*args):
        if user_logged_in == True:
            func(*args)
        else:
            print('Usuario no autenticado')
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


view_profile()