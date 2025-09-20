from datetime import date, datetime
from json import (load as jsonload, dump as jsondump, dumps as jsondumps)


def ISO_date(date_m_d_Y):
    return datetime.strptime(date_m_d_Y,"%m/%d/%Y").date()


def validate_from_to_dates(date_from,date_to):
    try:
        if date_from.strip() == '' or date_to.strip() == '':
            return True
        elif ISO_date(date_to) < ISO_date(date_from):
            raise ValueError('"Date from" field must be less than "Date to" field')
        else:
            return True
    except Exception as e:
        return e


def validate_date_format(date_transaction):
    try:
        if ISO_date(date_transaction):
            return True
    except:
        return 'Invalid date format (use mm/dd/yyyy)'


def validate_path(folder_path,file_name):
    try:
        if folder_path.strip() == '':
            raise ValueError('Invalid path: Please enter a valid folder path to export csv file')
        if file_name.strip() == '':
            raise ValueError('Invalid path: Please enter a valid file name')
        if not file_name.strip().endswith('.csv'):
            raise ValueError('Invalid path: Please add ".csv" extension to file name')
        else:
            return True
    except Exception as e:
        return e

def validate_amount_is_not_string(amount):
        try:
            if isinstance(float(amount),float):
                return True
        except:
            return 'Amount can only have numeric values'


def validate_transaction_fields(date_transaction, title, amount,category_name): 
    try:
        if title.strip() == '':
            raise ValueError('Transaction Name can not be empty')
        if amount == '': 
            raise ValueError('Amount can not be empty')
        if category_name =='':
            raise ValueError('Category can not be empty.')
        if ISO_date(date_transaction) > date.today():
            raise ValueError('Date cannot be a future date')
        else:
            return True
    except Exception as e:
        return e


def validate_category_fields(category_name,color): 
    try:
        if category_name.strip() == '':
            raise ValueError('Category Name can not be empty')
        if color == '':
            raise ValueError('Color can not be empty')
        else:
            return True
    except Exception as e:
        return e


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


class Transaction(): 
    date_transaction: str
    title: str
    amount: float
    category_name: str
    transaction_type: str

    def __init__(self, date_transaction, title, amount, category_name, transaction_type):
        self.date_transaction = date_transaction                        
        self.title  = title
        self.amount = -abs(float(amount)) if transaction_type == 'Expense' else abs(float(amount))
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
        return Transaction(**dict)


class FinanceTracker(): #base de datos de transacciones
    def __init__(self):
        self.transactions = []

    def add_transaction(self,transaction):
        self.transactions.append(transaction)

    @property
    def transactions_list(self):
        return [transaction.to_list() for transaction in self.transactions]
    
    def transactions_json(self):
        return jsondumps([transaction.to_dict() for transaction  in self.transactions], indent=2) 
    
    def transactions_from_list_of_dict(self, data):
        for dict in data:
            self.add_transaction(Transaction(**dict))

    def total_income(self):
        transaction_sum = 0
        for transaction in self.transactions_list:
            if transaction[4] == 'Income':
                transaction_sum += transaction[2]
        return transaction_sum
        
    def total_expenses(self):
        transaction_sum = 0
        for transaction in self.transactions_list:
            if transaction[4] == 'Expense':
                transaction_sum += abs(transaction[2])
        return transaction_sum
    
    def date_filtered_transactions(self,date_from,date_to):
        filtered_transactions_list = []
        if date_from.strip() == '' and date_to.strip() == '':
            return self.transactions_list
        if date_from and date_to.strip() == '':
            for transaction in self.transactions:
                if ISO_date(date_from) <= ISO_date(transaction.date_transaction):
                    filtered_transactions_list.append(transaction.to_list())
            return filtered_transactions_list
        if date_to and date_from.strip() == '':
            for transaction in self.transactions:
                if ISO_date(transaction.date_transaction) <= ISO_date(date_to):
                    filtered_transactions_list.append(transaction.to_list())
            return filtered_transactions_list
        if  ISO_date(date_from) < ISO_date(date_to):
            for transaction in self.transactions:
                if ISO_date(date_from) <= ISO_date(transaction.date_transaction) <= ISO_date(date_to):
                    filtered_transactions_list.append(transaction.to_list())
            return filtered_transactions_list


def row_color_lookup(transaction_list,category_collection): #producir lista de fila y color
    rows_colors = []
    for i in range(len(transaction_list)):
        category_name = transaction_list[i][3]
        rows_colors.append((i, category_collection.category_dict[category_name]) )
    return rows_colors


#validate_transaction_fields('34','1era quincena',750000.0,'Salario')

# [transaction.date_transaction.strftime("%m/%d/%Y"),transaction.title,transaction.amount,transaction.category_name,transaction.transaction_type]
# transaction_list = []
# list_transaction_w_color()