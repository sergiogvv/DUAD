class BankAccount():
    balance = 0

    def deposit_money(self, money):
        self.balance += money
        print(f'\nDeposito de {money}\nSu nuevo balance es: {self.balance}')

    def withdraw_money(self, money):
        self.balance -= money
        print(f'\nRetiro de {money}\nSu nuevo balance es: {self.balance}')

    def print_balance(self):
        print(f'\nSu balance es: {self.balance}')


class SavingsAccount(BankAccount):

    def __init__(self, min_balance,):
        self.min_balance = min_balance
        self.balance = min_balance
        print(f'\nNueva cuenta creada, balance inicial: {min_balance}')
        

    def withdraw_money(self, money):
        self.balance -= money
        if self.balance < self.min_balance:
            print('\nTransacción inválida: No se puede retirar dinero por debajo del balance minimo')
            self.balance += money 
            print(f'Su balance sigue siendo {self.balance}\n')
        else:
            print(f'\nRetiro de {money}\nSu nuevo balance es: {self.balance}\n')


a = BankAccount()
b = BankAccount()
a.deposit_money(100)
print(b.balance) # Hubiese esperado ver el balance como 100 si fuera un problema...


