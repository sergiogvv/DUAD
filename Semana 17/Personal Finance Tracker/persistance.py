import csv
from json import (load as jsonload, dump as jsondump, loads as jsonloads)




def save_data(data_file, data_json):
    with open(data_file, 'w') as f:
        f.write(data_json)


def load_categories_data(categories_file):
    try:
        with open(categories_file, 'r') as f:
                data = jsonload(f)
        return data
    except:
         return {}


def load_transactions_data(transactions_file):
    try:
        with open(transactions_file, 'r') as f:
                data = jsonload(f)
        return data
    except:
         return []


def export_to_csv(data_file, data_list, total_income, total_expenses, date_from, date_to):
    with open(data_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([f'Filtered from {date_from} to {date_to}'])
        writer.writerow([])
        writer.writerow(['Date', 'Title', 'Amount', 'Category', 'Type'])  # encabezados
        writer.writerows(data_list)
        writer.writerow([])
        writer.writerow(['Totals'])
        writer.writerow([f'Income: {total_income}'])
        writer.writerow([f'Expense: {total_expenses}'])
        writer.writerow([f'Net Balance: {total_income-total_expenses}'])

