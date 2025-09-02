import pytest
import sys
import os
from datetime import date, datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic import validate_amount_is_not_string, validate_transaction_fields, validate_category_fields, Category_Collection, row_color_lookup, validate_path, validate_date_format, validate_from_to_dates

import pytest

@pytest.mark.parametrize("date_transaction, title, amount, category_name, expected_message", [
    ("08/30/2025", '    ', -20000.0, "Entretenimiento", "Transaction Name can not be empty"),
    ("08/30/2025", "Cena", '', "Entretenimiento", "Amount can not be empty"),
    ("08/30/2025", "Cena", -20000.0, '', "Category can not be empty."),
    (datetime.strftime(date.today()+timedelta(days=30),"%m/%d/%Y"), "Cena", -20000.0, "Entretenimiento", 'Date cannot be a future date') #future date
])
def test_validate_transaction_fields_invalid_inputs(date_transaction, title, amount, category_name, expected_message):
    result = validate_transaction_fields(date_transaction, title, amount, category_name)
    assert isinstance(result, ValueError) or isinstance(result, TypeError)
    assert str(result) == expected_message

def test_validate_amount_is_not_string_valid_input():
    amount = '15000'
    result = validate_amount_is_not_string(amount)
    assert result == True

def test_validate_amount_is_not_string_invalid_input():
    amount = '55-5'
    result = validate_amount_is_not_string(amount)
    assert result == 'Amount can only have numeric values'


@pytest.mark.parametrize('category_name,color,expected_message', [
    ('     ',"#80ffff",'Category Name can not be empty'),
    ('Transporte','','Color can not be empty')
])
def test_validate_category_fields_invalid_inputs(category_name,color,expected_message):
    result = validate_category_fields(category_name,color)
    assert isinstance(result, ValueError)
    assert str(result) == expected_message


@pytest.mark.parametrize('folder_path,file_name,expected_message',[
    ('     ','export.csv','Invalid path: Please enter a valid folder path to export csv file'),
    ('C:/Users/sergio','     ','Invalid path: Please enter a valid file name'),
    ('C:/Users/sergi','export','Invalid path: Please add ".csv" extension to file name')
])
def test_validate_path_invalid_inputs(folder_path,file_name,expected_message):
    result = validate_path(folder_path,file_name)
    assert isinstance(result, ValueError)
    assert str(result) == expected_message


@pytest.mark.parametrize('date_transaction,expected_message',[
    ('15/12/2025','Invalid date format (use mm/dd/yyyy)'),
    ('04/31/1985','Invalid date format (use mm/dd/yyyy)'),
    ('3/20/85','Invalid date format (use mm/dd/yyyy)'),
    ('','Invalid date format (use mm/dd/yyyy)')
])
def test_validate_date_format_invalid_date_formats(date_transaction,expected_message): 
    result = validate_date_format(date_transaction)
    assert str(result) == expected_message


def test_validate_from_to_dates_when_date_to_less_than_date_from():
    test_tuple = ('12/15/2025','9/2/2025')
    result = validate_from_to_dates(*test_tuple)
    assert isinstance(result, ValueError)
    assert str(result) == '"Date from" field must be less than "Date to" field'

