from interfaces import main_window
from logic import Transaction, Category, FinanceTracker
from os import path


def main():

    transactions_file = path.join(path.dirname(__file__), r'transactions.dat')
    categories_file = path.join(path.dirname(__file__), r'categories.dat')

    main_window(transactions_file,categories_file)




if __name__ == "__main__":
    main()