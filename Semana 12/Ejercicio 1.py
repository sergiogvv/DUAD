class BankAccount():
    balance = 0

    def deposit_money(self, money):
        self.balance += money
        print(f' Su nuevo balance es: {self.balance}')


    def withdraw_money(self, money):
        self.balance -= money
        print(f' Su nuevo balance es: {self.balance}')



class SavingsAccount(BankAccount):

    def __init__(self, min_balance,):
        self.min_balance = min_balance
        self.balance = min_balance
        print('Nueva cuenta creada')
        print(f'Balance = {min_balance}')

    def withdraw_money(self, money):
        self.balance -= money
        if self.balance < self.min_balance:
            print('Transacción inválida: No se puede retirar dinero por debajo del balance minimo')
            self.balance += money 
            print(f'Su balance sigue siendo {self.balance}')
        else:
            print(f' Su nuevo balance es: {self.balance}')



my_savings = SavingsAccount(1000)

my_savings.deposit_money(4000)

my_savings.withdraw_money(5000)

my_savings.withdraw_money(500)

