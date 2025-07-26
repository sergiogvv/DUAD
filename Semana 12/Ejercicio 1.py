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



my_savings = SavingsAccount(1000) #Nueva cuenta creada, balance inicial: 1000
my_other_savings = SavingsAccount(5000) #Nueva cuenta creada, balance inicial: 5000

my_savings.print_balance() #Su balance es: 1000

my_other_savings.print_balance() #Su balance es: 5000


my_savings.deposit_money(4000) # 1000 + 4000: Deposito de 4000, Su nuevo balance es: 5000
my_savings.withdraw_money(5000) # 5000 - 5000: Transacción inválida: No se puede retirar dinero por debajo del balance minimo
my_savings.withdraw_money(500) # 5000 - 500: Retiro de 500, Su nuevo balance es: 4500

my_other_savings.print_balance() #Su balance es: 5000

