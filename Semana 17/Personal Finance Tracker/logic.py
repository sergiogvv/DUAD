from datetime import date, datetime
from json import (load as jsonload, dump as jsondump, dumps as jsondumps)

def validate_path(path):
    try:
        if path.strip() == '':
            raise ValueError('Invalid path: Please enter a valid path to export csv file')
        else:
            return True
    except Exception as e:
        return e
    

def validate_date_format(date_transaction):
    try:
        if datetime.strptime(date_transaction,"%m/%d/%Y").date():
            return True
    except:
        return 'Invalid date format (use mm/dd/yyyy)'


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
    def __init__(self):
        self.category_dict = {}

    def add_category(self, category):
        self.category_dict[category.category_name]= category.color

    def return_list_of_category_names(self):
        list_of_category_names = []
        for category_name in self.category_dict.keys():
            list_of_category_names.append(category_name)
        return list_of_category_names
    
    def categories_json(self):
        return jsondumps(self.category_dict, indent=2)


class Transaction(): #transaccion
    date_transaction: date 
    title: str
    amount: float
    category: Category
    transaction_type: str

    def __init__(self, date_transaction, title, amount, category_name, transaction_type):
        self.date_transaction = date_transaction                        #datetime.strptime(date_transaction,"%m/%d/%Y").date()
        self.title  = title
        self.amount = -float(amount) if transaction_type == 'Expense'else float(amount)
        self.category_name = category_name
        self.transaction_type = transaction_type

    def to_dict(self):
        return {
            'date_transaction' : self.date_transaction,
            'title' : self.title,  
            'amount' : self.amount, 
            'category_name' : self.category_name,
            'transaction_type' : self.transaction_type 
        }
    
    def to_list(self):
        return [self.date_transaction,self.title,self.amount,self.category_name,self.transaction_type]
    
    @staticmethod
    def from_dict(dict):
        return Transaction(dict['date_transaction'],dict['title'], dict['amount'], dict['category_name'], dict['transaction_type'])


class FinanceTracker(): #base de datos de transacciones
    def __init__(self):
        self.transactions_list = []

    def add_transaction(self,transaction):
        self.transactions_list.append(transaction)

    def transactions(self):
        return [transaction.to_list() for transaction in self.transactions_list]
    
    def transactions_json(self):
        return jsondumps([transaction.to_dict() for transaction  in self.transactions_list], indent=2) 
    
    def transactions_from_list_of_dict(self, data):
        for dict in data:
            self.add_transaction(Transaction(**dict))

    def total_income(self):
        transaction_sum = 0
        for transaction in self.transactions_list:
            if transaction.transaction_type == 'Income':
                transaction_sum += transaction.amount
        return transaction_sum
        
    def total_expenses(self):
        transaction_sum = 0
        for transaction in self.transactions_list:
            if transaction.transaction_type == 'Expense':
                transaction_sum += abs(transaction.amount)
        return transaction_sum
    


#validate_transaction_fields('34','1era quincena',750000.0,'Salario')

# [transaction.date_transaction.strftime("%m/%d/%Y"),transaction.title,transaction.amount,transaction.category_name,transaction.transaction_type]
# transaction_list = []
# list_transaction_w_color()