import FreeSimpleGUI as sg
from logic import Transaction, Category, FinanceTracker, validate_transaction_fields, validate_category_fields, Category_Collection, list_transaction_row_w_color
from datetime import date, datetime

def name(name):
        return sg.Text(name + '    ', justification='r',size= (20,1),pad=(10,10))

sg.theme('Default1') 



def main_window(finance_tracker):
        category_collection = Category_Collection()
        
        layout = [
                [sg.T('PERSONAL FINANCE TRACKER', font='_ 14', justification='c', expand_x=True)],
                [sg.Text()],
                [sg.Text("TRANSACTIONS")],
                [sg.Text()],
                [sg.CalendarButton('From',target='-FROM-',tooltip=' Select date ',format= '%m/%d/%Y'), sg.Input(key='-FROM-', s=10),sg.CalendarButton('To',target='-TO-',tooltip=' Select date ',format= '%m/%d/%Y' ),sg.Input(key='-TO-',s=10),sg.Push(),sg.Button('Apply Filter',key='-FILTER-')],
                [sg.Table(finance_tracker.return_transactions(), ['Date', 'Title', 'Amount', 'Category', 'Type'],visible_column_map = ['Date', 'Title', 'Amount', 'Category', 'Type'],
                        def_col_width = 15,
                        starting_row_number = 0,
                        max_col_width = 100,
                        col_widths = [10, 25, 15, 25, 10],
                        vertical_scroll_only = False,
                        auto_size_columns = False,
                        display_row_numbers = True,
                        justification='right',
                        num_rows=20,
                        #alternating_row_color='lightblue',
                        key='-TABLE-',
                        tooltip='This is a table')],
                [sg.Push(),sg.Button("Input Expense",key='-EXPENSE-'), sg.Button("Input Income", key='-INCOME-'), sg.Button('Add Category', key='-CATEGORY-'), sg. Button('Export to CSV', key='-CSV-'),sg.Push()],
                [sg.Text()],
                [sg.T('Developed by SGVV ©2025 ', font='_ 8', justification='r', expand_x=True)]
                ]

        window = sg.Window('PERSONAL FINANCE TRACKER', layout)

        while True:
                event, values = window.read()
                print(event,values)
                if event == sg.WIN_CLOSED:
                        break
                if event == '-EXPENSE-':
                        if  category_collection.category_dict == {}:
                                sg.popup_error('Please enter a category first before entering a transaction') 
                                continue                       
                        expense = transaction_window('Expense', category_collection.return_list_of_category_names())
                        if expense is not None:
                                finance_tracker.add_transaction(expense)
                                window['-TABLE-'].update(values=finance_tracker.return_transactions(),row_colors = list_transaction_row_w_color(finance_tracker.return_transactions(),category_collection))
                if event == '-INCOME-':
                        if  category_collection.category_dict == {}:
                                sg.popup_error('Please enter a category first before entering a transaction')
                                continue
                        income = transaction_window('Income', category_collection.return_list_of_category_names())
                        if income is not None:
                                finance_tracker.add_transaction(income)
                                window['-TABLE-'].update(values=finance_tracker.return_transactions(),row_colors = list_transaction_row_w_color(finance_tracker.return_transactions(),category_collection))
                if event == '-CATEGORY-':
                        category = category_window()
                        if category is not None:
                                category_collection.add_category(category)
                if event == '-CSV-' :
                        export_to_CSV_window()

        window.close()    

def transaction_window(type_title,category_list):
        layout = [
                [name('Transaction Name'),sg.Input(key='-NAME-', s=15)],
                [name('Amount'), sg.Input(key='-AMOUNT-', enable_events=True, s=15)],
                [name('Category'), sg.Combo(category_list, s=(15,22), readonly=True, k='-CATEGORY-')],
                [name('Date (mm/dd/yyyy)'), sg.Input(key='-DATE-', s=15, default_text=date.today().strftime("%m/%d/%Y")),sg.Text(), sg.CalendarButton('Select date',target='-DATE-',format= '%m/%d/%Y' )],
                [sg.Text()],
                [sg.Push(), sg.Button("Save Transaction"),sg.Button("Clear All"), sg.Button("Cancel"),sg.Push()]
                ] 

        window = sg.Window('Add '+type_title, layout, disable_close = True, disable_minimize = True, modal = True )

        while True:
                event, values = window.read()
                print(event,values)
                if event == 'Cancel':
                        window.close()
                        return None
                if event == '-AMOUNT-' and values['-AMOUNT-']:
                        try:
                                in_as_float = float(values['-AMOUNT-'])
                        except:
                                if len(values['-AMOUNT-']) == 1 and values['-AMOUNT-'][0] == '-':
                                        continue
                                window['-AMOUNT-'].update(values['-AMOUNT-'][:-1])
                if event == "Save Transaction":
                        valid_fields = validate_transaction_fields(values['-DATE-'], values['-NAME-'], values['-AMOUNT-'], values['-CATEGORY-'])
                        if  valid_fields == True:
                                transaction = Transaction(values['-DATE-'], values['-NAME-'], values['-AMOUNT-'], values['-CATEGORY-'], type_title)
                                window.close()
                                return transaction
                        else:
                                sg.popup_error(valid_fields)
                if event == 'Clear All':
                        window['-NAME-'].update('')
                        window['-AMOUNT-'].update('')
                        window['-DATE-'].update('')
        window.close()

def category_window():
        layout = [
                [name('Category Name'),sg.Input(key='-NAME-', s=15)],
                [name('Color'),sg.Input(key='-COLOR-', tooltip=' Use "Select Color" button to select category color ',disabled_readonly_background_color = "#ffffff", readonly =True, s=15), sg.ColorChooserButton('Select Color', target='-COLOR-')],
                [sg.Text()],
                [sg.Push(), sg.Button("Save Category"),sg.Button("Clear All"), sg.Button("Cancel"),sg.Push()]
                ] 
        
        window = sg.Window('Add category', layout, disable_close = True, disable_minimize = True, modal = True )

        while True:
                event, values = window.read()
                print(event,values)
                if event == 'Cancel':
                        break
                if event == "Save Category":
                        valid_fields = validate_category_fields(values['-NAME-'], values['-COLOR-'])
                        if valid_fields == True:
                                category = Category(values['-NAME-'], values['-COLOR-'])
                                window.close()
                                return category
                        else:
                                sg.popup_error(valid_fields)
                if event == 'Clear All':
                        window['-NAME-'].update('')
                        window['-COLOR-'].update('')
        window.close()               

def export_to_CSV_window():
        layout = [
                [name('Export Path'), sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
                [sg.Text()],
                [sg.Push(), sg.Button("OK"),sg.Button("Clear All"), sg.Button("Cancel"),sg.Push()]                
                ]
        
        window = sg.Window('Export to CSV', layout, disable_close = True, disable_minimize = True, modal = True )

        while True:
                event, values = window.read()
                print(event,values)
                if event == 'Cancel':
                        break
                if event == "OK":
                        pass
                if event == 'Clear All':
                        window['-USER FOLDER-'].update('')
        window.close()  









#transaction_window('Expense')
#transaction_window('Income')
#main_window()