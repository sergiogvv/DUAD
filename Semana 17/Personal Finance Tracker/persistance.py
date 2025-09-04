import csv
from json import (load as jsonload, dump as jsondump, loads as jsonloads)


def save_data(data_file_path, data):
    with open(data_file_path, 'w') as f:
        f.write(data)

def load_data(data_file_path):
    try:
        with open(data_file_path, 'r') as f:
            reader = f.read()
        return reader
    except:
        return ''


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
        if date_from and date_to.strip() == '':
            writer.writerow([f'Filtered from {date_from}'])
            writer.writerow([])
        if date_to and date_from.strip() == '':
            writer.writerow([f'Filtered up to {date_to}'])
            writer.writerow([])
        if date_from and date_to:
            writer.writerow([f'Filtered from {date_from} to {date_to}'])
            writer.writerow([])             
        writer.writerow(['Date', 'Title', 'Amount', 'Category', 'Type'])  # encabezados
        writer.writerows(data_list)
        writer.writerow([])
        writer.writerow(['Totals'])
        writer.writerow([f'Income: {total_income}'])
        writer.writerow([f'Expense: {total_expenses}'])
        writer.writerow([f'Net Balance: {total_income-total_expenses}'])

