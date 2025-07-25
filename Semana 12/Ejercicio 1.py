class BankAccount():
    balance = 0

    def deposit_money(self, money):
        self.balance += money
        print(f'Deposito de {money}\nSu nuevo balance es: {self.balance}\n')


    def withdraw_money(self, money):
        self.balance -= money
        print(f'Retiro de {money}\nSu nuevo balance es: {self.balance}\n')


class SavingsAccount(BankAccount):

    def __init__(self, min_balance,):
        self.min_balance = min_balance
        self.balance = min_balance
        print(f'Nueva cuenta creada, balance inicial: {min_balance}\n')
        

    def withdraw_money(self, money):
        self.balance -= money
        if self.balance < self.min_balance:
            print('Transacción inválida: No se puede retirar dinero por debajo del balance minimo')
            self.balance += money 
            print(f'Su balance sigue siendo {self.balance}\n')
        else:
            print(f'Retiro de {money}\nSu nuevo balance es: {self.balance}\n')



my_savings = SavingsAccount(1000)

my_savings.deposit_money(4000)

my_savings.withdraw_money(5000)

my_savings.withdraw_money(500)

