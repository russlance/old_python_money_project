import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from Utility_User_Interface import are_you_sure


# use listbox widget to display all expense names so user can remove or edit the one they want
def edit_expense_interaction():
    filename = 'Expenses'
    from Main_Program import MainProgram

    # Asks for confirmation to delete expense
    def confirm_request():
        are_you_sure(delete_function)

    # Removes expense from dictionary and from the listbox
    def delete_function():
        temp = lb.get(ANCHOR)
        print('here')
        MainProgram().delete_dictionary_item(temp, filename)
        print('there')
        lb.delete(ANCHOR)
        print('again')

    popup = tk.Tk()
    popup.title('Remove Bill')
    temp_dict = MainProgram().open_file(filename)

    Label(popup, text='Select an Expense').grid(row=0, columnspan=2, padx=5, pady=5)

    # Creates a listbox with names of the expenses (uses keys from 'Expenses.json')
    lb = Listbox(popup, selectmode=SINGLE)
    lb.grid(row=1, columnspan=2, padx=5, pady=5)
    for key in temp_dict:
        lb.insert(END, key)

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

    add_bill = tk.Tk()
    add_bill.title('Add/Edit Bills')

    dd_variable = StringVar(add_bill)

    # Converts input from Entry widgets into variables and arranges into dictionary entry to update the dictionary
    def return_variables():
        bill_name = bill_name_entry.get()
        amount_due = float(amount_due_entry.get())
        due_date = int(due_date_entry.get())
        interest = float(interest_entry.get())
        total = float(total_entry.get())

        new_bill = {bill_name: [amount_due, due_date, interest, total]}
        MainProgram().update_dictionary(new_bill, filename)

    # In txt file:
        # 1st item is Bill Name,
        # 2nd item - Amount Due
        # 3rd item = Due Date
        # 4th item = Interest Rate
        # 5th item = Total Due
    Label(add_bill, text='Bill Name:').grid(row=0, column=0, sticky=E, padx=10, pady=5)
    bill_name_entry = Entry(add_bill)
    bill_name_entry.grid(row=0, column=1, padx=10)

    Label(add_bill, text='Amount Due:').grid(row=1, column=0, sticky=E, padx=10, pady=5)
    amount_due_entry = Entry(add_bill)
    amount_due_entry.grid(row=1, column=1)

    # Dropdown for selecting week of the month the bill is due
    Label(add_bill, text='What week do you pay this bill?').grid(row=2, column=0, sticky=E, padx=10, pady=5)
    choices = ['1', '2', '3', '4']
    # set the default option
    #dd_variable.set('1')
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