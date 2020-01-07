import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import datetime
from Utility_User_Interface import are_you_sure


# use listbox widget to display all expense names so user can remove or edit the one they want
def edit_income_interaction():
    filename = 'Income'
    from Main_Program import MainProgram
    temp_dict = MainProgram().open_file(filename)

    # Asks for confirmation to delete expense
    def confirm_request():
        are_you_sure(delete_function)

    # Removes expense from dictionary and from the listbox
    def delete_function():
        temp = lb.get(ANCHOR)
        MainProgram().delete_dictionary_item(temp, filename)
        lb.delete(ANCHOR)

    popup = tk.Tk()
    popup.title('Remove Income')

    # Gets the requested values of the height and width.
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(position_right, position_down))

    Label(popup, text='Select an Income').grid(row=0, columnspan=2, padx=5, pady=5)

    # Creates a listbox with names of the expenses (uses keys from 'Expenses.json')
    lb = Listbox(popup, selectmode=SINGLE)
    lb.grid(row=1, columnspan=2, padx=5, pady=5)
    for key in temp_dict:
        print('accessing the dictionary for the listbox')
        lb.insert(END, key)

    eb = Button(popup, text="Edit")
    eb.grid(row=2, column=0, padx=5, pady=5)

    rb = Button(popup, text='Remove', command=confirm_request)
    rb.grid(row=2, column=1, padx=5, pady=5)

    fb = Button(popup, text='Finish', command=popup.destroy)
    fb.grid(row=3, columnspan=2, padx=5, pady=5)

    popup.mainloop()


# Opens window to add new expense informaiton
def income_add_interaction():
    filename = 'Income'
    monthly_income_week = 1
    income_date_entry = tk.IntVar()
    bwi_date_entry = tk.IntVar()
    from Main_Program import MainProgram

    # Converts input from Entry widgets into variables and arranges into dictionary entry to update the dictionary
    def return_variables():
        questions()
        income_name = income_name_entry.get()
        income_amount = float(income_amount_entry.get())
        income_date = int(income_date_entry.get())
        bwi_date = int(bwi_date_entry.get())
        income_date_details = [income_date, bwi_date, monthly_income_week]
        new_item = {income_name: [income_amount, income_date, income_date_details]}
        MainProgram().update_dictionary(new_item, filename)

    def questions():
        if income_date == 2:
            popup = Toplevel()
            popup.title('Bi-Weekly Income Clarification')

            # Gets the requested values of the height and width.
            window_width = popup.winfo_reqwidth()
            window_height = popup.winfo_reqheight()

            # Gets both half the screen width/height and window width/height
            position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
            position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

            # Positions the window in the center of the page.
            popup.geometry("+{}+{}".format(position_right, position_down))

            label = Label(add_income, text='Did you receive this income this week?')
            label.grid(row=0, columnspan=2, sticky=E, padx=10, pady=5)
            rb1 = Radiobutton(add_income, text="Yes", variable=bwi_date_entry, value=1)
            rb1.grid(row=1, column=0, sticky=W, padx=10)
            rb2 = Radiobutton(add_income, text="No", variable=bwi_date_entry, value=2)
            rb2.grid(row=1, column=1, sticky=W, padx=10)
            Button(popup, text='Finish', command=quit).grid(row=2, columnspan=2, padx=20, pady=20)

            popup.mainloop()

        if income_date == 3:
            popup = Toplevel()
            popup.title('Monthly Income Clarification')

            # Gets the requested values of the height and width.
            window_width = popup.winfo_reqwidth()
            window_height = popup.winfo_reqheight()

            # Gets both half the screen width/height and window width/height
            position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
            position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

            # Positions the window in the center of the page.
            popup.geometry("+{}+{}".format(position_right, position_down))

            miw_variable = StringVar(add_income)
            label = Label(add_income, text='What week of the month do you receive this income?')
            label.grid(row=6, column=0, sticky=E, padx=10, pady=5)
            choices = ['0', '1', '2', '3', '4']
            monthly_income_week_entry = OptionMenu(add_income, miw_variable, *choices)
            monthly_income_week_entry.grid(row=2, column=1)
            monthly_income_week = miw_variable
            Button(popup, text='Finish', command=quit).grid(row=2, columnspan=2, padx=20, pady=20)

            popup.mainloop()

        else:
            bwi_date_entry = 0
            monthly_income_week = 0

    add_income = tk.Tk()
    add_income.title('Add/Edit Income')

    # Gets the requested values of the height and width.
    window_width = add_income.winfo_reqwidth()
    window_height = add_income.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(add_income.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(add_income.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    add_income.geometry("+{}+{}".format(position_right, position_down))

    dd_variable = StringVar(add_income)

    # In txt file:
        # 1st item is Income Name,
        # 2nd item - Amount Earned
        # 3rd item = Date Paid
        # 4th item = Check-box for
    Label(add_income, text='Income Name:').grid(row=0, column=0, sticky=E, padx=10, pady=5)
    income_name_entry = Entry(add_income)
    income_name_entry.grid(row=0, column=3, padx=10)

    Label(add_income, text='Amount:').grid(row=1, column=0, sticky=E, padx=10, pady=5)
    income_amount_entry = Entry(add_income)
    income_amount_entry.grid(row=1, column=3)

    # Radiobutton for selecting week of the month the bill is due
    # Further clarifies for bi-weekly income when was received to determine week of month received
    # Gathers week of month monthly income is received
    Label(add_income, text='How often do you receive this?').grid(row=3, columnspan=3, sticky=E, padx=10, pady=5)
    Radiobutton(add_income, text="Weekly", variable=income_date_entry, value=1).grid(row=3, column=3, sticky=W, padx=10)
    Radiobutton(add_income, text="Biweekly", variable=income_date_entry, value=2).grid(row=4, column=3, sticky=W, padx=10)



    save_button = Button(add_income, text='Save', command=return_variables)
    save_button.grid(row=6, column=0, padx=10, pady=10)
    finish_button = Button(add_income, text='Finish', command=add_income.destroy)
    finish_button.grid(row=6, column=1, padx=10, pady=10)

    add_income.mainloop()