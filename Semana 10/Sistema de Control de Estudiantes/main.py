from menu import execute_menu
from colorama import Fore, init
import os




def main():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    init(autoreset=True)  # Initialize colorama for Windows

    print(Fore.BLUE+'-----------------------------------')
    print(Fore.LIGHTBLUE_EX+' Sistema de Control de Estudiantes')
    print(Fore.BLUE+'-----------------------------------')

    execute_menu()





if __name__ == "__main__":
    main()