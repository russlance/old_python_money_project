import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from Utility_User_Interface import are_you_sure


# use listbox widget to display all expense names so user can remove or edit the one they want
def edit_expense_interaction():
    print('opened edit_expense_interaction')
    from Main_Program import MainProgram
    filename = 'Expenses'
    #temp_dict = MainProgram().open_file(filename)
    print('opened the file')

    # Asks for confirmation to delete expense
    def confirm_request():
        are_you_sure(delete_function)

    # Removes expense from dictionary and from the listbox
    def delete_function():
        temp = lb.get(ANCHOR)
        print('got the item from the listbox')
        MainProgram().delete_dictionary_item(temp, filename)
        print('sent to delete_dictionary_item function')
        lb.delete(ANCHOR)
        print('removed the item from the listbox')

    popup = tk.Tk()
    popup.title('Remove Expense')

    # Gets the requested values of the height and width.
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(position_right, position_down))

    Label(popup, text='Select an Expense').grid(row=0, columnspan=2, padx=5, pady=5)

    # Creates a listbox with names of the expenses (uses keys from 'Expenses.json')
    lb = Listbox(popup, selectmode=SINGLE)
    lb.grid(row=1, columnspan=2, padx=5, pady=5)
    for key in MainProgram().open_file(filename):
        lb.insert(END, key)
        print('looked in the dictionary to populate the listbox')

    eb = Button(popup, text="Edit")
    eb.grid(row=2, column=0, padx=5, pady=5)

    rb = Button(popup, text='Remove', command=confirm_request)
    rb.grid(row=2, column=1, padx=5, pady=5)

    fb = Button(popup, text='Finish', command=popup.destroy)
    fb.grid(row=3, columnspan=2, padx=5, pady=5)

    popup.mainloop()


# Opens window to add new expense informaiton
def bill_add_interaction():
    filename = 'Expenses'
    from Main_Program import MainProgram

    # Converts input from Entry widgets into variables and arranges into dictionary entry to update the dictionary
    def return_variables():
        bill_name = bill_name_entry.get()
        amount_due = float(amount_due_entry.get())
        due_date = int(due_date_entry.get())
        interest = float(interest_entry.get())
        total = float(total_entry.get())

        new_item = {bill_name: [amount_due, due_date, interest, total]}
        MainProgram().update_dictionary(new_item, filename)

    add_bill = tk.Tk()
    add_bill.title('Add/Edit Expenses')

    # Gets the requested values of the height and width.
    window_width = add_bill.winfo_reqwidth()
    window_height = add_bill.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(add_bill.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(add_bill.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    add_bill.geometry("+{}+{}".format(position_right, position_down))

    dd_variable = StringVar(add_bill)

    # In txt file:
        # 1st item is Bill Name,
        # 2nd item - Amount Due
        # 3rd item = Due Date
        # 4th item = Interest Rate
        # 5th item = Total Due
    Label(add_bill, text='Expense Name:').grid(row=0, column=0, sticky=E, padx=10, pady=5)
    bill_name_entry = Entry(add_bill)
    bill_name_entry.grid(row=0, column=1, padx=10)

    Label(add_bill, text='Amount Due:').grid(row=1, column=0, sticky=E, padx=10, pady=5)
    amount_due_entry = Entry(add_bill)
    amount_due_entry.grid(row=1, column=1)

    # Dropdown for selecting week of the month the bill is due
    Label(add_bill, text='What week do you pay this expense?').grid(row=2, column=0, sticky=E, padx=10, pady=5)
    choices = ['0', '1', '2', '3', '4']

    due_date_entry = OptionMenu(add_bill, dd_variable, *choices)

    due_date_entry.grid(row=2, column=1)
    due_date_entry = dd_variable

    Label(add_bill, text='Interest Rate:').grid(row=3, column=0, sticky=E, padx=10, pady=5)
    interest_entry = Entry(add_bill)
    interest_entry.grid(row=3, column=1)

    Label(add_bill, text='Total Due:').grid(row=4, column=0, sticky=E, padx=10, pady=5)
    total_entry = Entry(add_bill)
    total_entry.grid(row=4, column=1)

    save_button = Button(add_bill, text='Save', command=return_variables)
    save_button.grid(row=5, column=0, padx=10, pady=10)
    finish_button = Button(add_bill, text='Finish', command=add_bill.destroy)
    finish_button.grid(row=5, column=1, padx=10, pady=10)

    add_bill.mainloop()