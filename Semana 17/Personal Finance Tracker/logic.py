from datetime import date, datetime
from os import path



def validate_transaction_fields(date_transaction, title, amount,category_name): #validar formulario de transacciones
    try:
        if title.strip() == '':
            raise ValueError('Transaction Name can not be empty')
        if amount == '': 
            raise ValueError('Amount can not be empty')
        if category_name =='':
            raise ValueError('Category can not be empty.')
        if datetime.strptime(date_transaction,"%m/%d/%Y").date() > date.today():
            raise ValueError('Date cannot be a future date')
        else:
            return True
    except Exception as e:
        return e


def validate_category_fields(category_name,color): #validar categoria y color
    try:
        if category_name.strip() == '':
            raise ValueError('Category Name can not be empty')
        if color == '':
            raise ValueError('Color can not be empty')
        else:
            return True
    except Exception as e:
        return e


def list_transaction_row_w_color(transaction_list,category_collection): #producir lista de fila y color
    returned_tuple = []
    for i in range(len(transaction_list)):
        returned_tuple.append((i, category_collection.category_dict[transaction_list[i][3]]) )
    return returned_tuple


class Category(): #categoria y color
    def __init__(self, category_name,color):
        self.category_name = category_name
        self.color = color


class Category_Collection(): #Base de datos de categorias
    category_dict = {}
   
    def add_category(self, category):
        self.category_dict[category.category_name]= category.color

    def return_list_of_category_names(self):
        list_of_category_names = []
        for category_name in self.category_dict.keys():
            list_of_category_names.append(category_name)
        return list_of_category_names


class Transaction(): #transaccion
    date_transaction: date 
    title: str
    amount: float
    category: Category
    transaction_type: str


    def __init__(self, date_transaction, title, amount, category, transaction_type):
        self.date_transaction = datetime.strptime(date_transaction,"%m/%d/%Y").date()
        self.title  = title
        self.amount = -float(amount) if transaction_type == 'Expense'else float(amount)
        self.category = category
        self.transaction_type = transaction_type


class FinanceTracker(): #base de datos de transacciones
    transaction_list = []
    def add_transaction(self,transaction):
        self.transaction_list.append([transaction.date_transaction.strftime("%m/%d/%Y"),transaction.title,transaction.amount,transaction.category,transaction.transaction_type])

    def return_transactions(self):
        return self.transaction_list



# transaction_list = []
# list_transaction_w_color()