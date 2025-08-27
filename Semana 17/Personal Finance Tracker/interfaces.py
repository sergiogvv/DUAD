import FreeSimpleGUI as sg
from logic import Transaction, Category, FinanceTracker
from datetime import date

def name(name):
        return sg.Text(name + '    ', justification='r',size= (20,1),pad=(10,10))

sg.theme('Default1') 



def main_window(finance_tracker):
        layout = [
                [sg.T('PERSONAL FINANCE TRACKER', font='_ 14', justification='c', expand_x=True)],
                [sg.Text()],
                [sg.Text("TRANSACTIONS")],
                [sg.Text()],
                [sg.CalendarButton('From',target='-FROM-',tooltip=' Select date ',format= '%Y-%m-%d ' ), sg.Input(key='-FROM-', s=10),sg.CalendarButton('To',target='-TO-',tooltip=' Select date ',format= '%Y-%m-%d ' ),sg.Input(key='-TO-',s=10),sg.Push(),sg.Button('Apply Filter',key='-FILTER-')],
                [sg.Table(finance_tracker.return_transactions(), ['Date', 'Title', 'Amount', 'Category', 'Type'],
                        def_col_width = 15,
                        starting_row_number = 1,
                        max_col_width = 100,
                        col_widths = [10, 25, 15, 25, 10],
                        vertical_scroll_only = False,
                        auto_size_columns = False,
                        display_row_numbers = True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightblue',
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
                        expense = transaction_window('Expense')
                        if expense is not None:
                                finance_tracker.add_transaction(expense)
                                window['-TABLE-'].update(values=finance_tracker.return_transactions())
                if event == '-INCOME-':
                        income = transaction_window('Income')
                        if income is not None:
                                finance_tracker.add_transaction(income)
                                window['-TABLE-'].update(values=finance_tracker.return_transactions())
                if event == '-CATEGORY-':
                        category = category_window()
                if event == '-CSV-' :
                        pass

        window.close()    

def transaction_window(type_title):
        layout = [
                [name('Transaction Name'),sg.Input(key='-NAME-', s=15)],
                [name('Amount'), sg.Input(key='-AMOUNT-', enable_events=True, s=15)],
                [name('Category'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), readonly=True, k='-CATEGORY-')],
                [name('Date (mm/dd/yyyy)'), sg.Input(key='-DATE-', s=15, default_text='08/25/2025'),sg.Text(), sg.CalendarButton('Select date',target='-DATE-',format= '%m/%d/%Y' )],
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

                # 
                if event == '-AMOUNT-' and values['-AMOUNT-']:
                        try:
                                in_as_float = float(values['-AMOUNT-'])
                        except:
                                if len(values['-AMOUNT-']) == 1 and values['-AMOUNT-'][0] == '-':
                                        continue
                                window['-AMOUNT-'].update(values['-AMOUNT-'][:-1])
                if event == "Save Transaction":
                        window.close()
                        return Transaction(values['-DATE-'], values['-NAME-'], values['-AMOUNT-'], values['-CATEGORY-'], type_title)
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
                if event == sg.WIN_CLOSED or event == 'Cancel':
                        break
                if event == "Save Category":
                        window.close()
                        return Category(values['-NAME-'], values['-COLOR-'])
                if event == 'Clear All':
                        window['-NAME-'].update('')
                        window['-COLOR-'].update('')
        window.close()               

def export_to_CSV_window():
        layout = [
                [name('Export Path:'),sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')]
        ]









#transaction_window('Expense')
#transaction_window('Income')
#main_window()