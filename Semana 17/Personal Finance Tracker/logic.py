from datetime import date
from os import path

class Transaction():
    def __init__(self, date, title, amount, category, transaction_type):
        self.date = date
        self.title  = title
        self.amount = -float(amount) if transaction_type == 'Expense'else float(amount)
        self.category = category
        self.transaction_type = transaction_type


class FinanceTracker():
    transaction_list = []
    def add_transaction(self,transaction):
        self.transaction_list.append([transaction.date,transaction.title,transaction.amount,transaction.category,transaction.transaction_type])

    def return_transactions(self):
        return self.transaction_list


class Category():
    def __init__(self, category_name,color):
        self.category_name = category_name
        self.color = color





