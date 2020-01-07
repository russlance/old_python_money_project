import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import time


def main_program():
    # Need to build main page layout
    # display graph
    # choose colors
    from Income_User_Interface import edit_income_interaction, income_add_interaction
    from Expenses_User_Interface import bill_add_interaction, edit_expense_interaction
    from Utility_User_Interface import quit_program
    from Main_Program import MainProgram

    # Updates the listbox at 1.5 second intervals
    # This allows for newly added expenses to be added if they are due during the current week
    def update():
        expense_lb.delete(0, END)
        income_lb.delete(0, END)
        for item in MainProgram().expenses_due_this_week():
            expense_lb.insert(END, item)
        for item in MainProgram().income_for_this_week():
            income_lb.insert(END, item)
        root.after(1500, update)

    root = tk.Tk()
    root.title('Money Manager')
    time()

    # Gets the requested values of the height and width.
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(position_right, position_down))

    menubar = Menu(root)
    # create a pulldown menu, and add it to the top of the window(in Windows OS), or top of the screen (Mac)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Add Expense", command=bill_add_interaction)
    filemenu.add_command(label="Edit Expense", command=edit_expense_interaction)
    filemenu.add_command(label="Add Income", command=income_add_interaction)
    filemenu.add_command(label="Edit Income", command=edit_income_interaction)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quit_program)
    menubar.add_cascade(label="File", menu=filemenu)
    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Options")
    editmenu.add_command(label="More Options")
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About")
    menubar.add_cascade(label="Help", menu=helpmenu)
    # display the menu
    root.config(menu=menubar)

    # Displays primary buttons, also accessable through menu
    Button(root, text='Add Expense', command=bill_add_interaction).grid(row=1, column=0, padx=5, pady=5)
    Button(root, text='Remove Expense', command=edit_expense_interaction).grid(row=2, column=0, padx=5, pady=5)
    Button(root, text='Add Income', command=income_add_interaction).grid(row=1, column=1, padx=5, pady=5)
    Button(root, text='Remove Income', command=edit_income_interaction).grid(row=2, column=1, padx=5, pady=5)
    Button(root, text='Quit', command=quit_program).grid(row=1, column=4, padx=5, pady=5)

    # Creates a listbox with names of the expenses (uses keys from 'Expenses.json') due for current week
    Label(root, text='Expenses Due This Week').grid(row=4, column=0, padx=5, pady=5)
    expense_lb = Listbox(root, selectmode=SINGLE)
    expense_lb.grid(row=5, column=0, padx=20, pady=10)

    # Creates a listbox with income sources (uses keys from 'Expenses.json')  for current week
    Label(root, text='Expected Income This Week').grid(row=4, column=1, padx=5, pady=5)
    income_lb = Listbox(root, selectmode=SINGLE)
    income_lb.grid(row=5, column=1, padx=20, pady=10)

    update()

    root.update()
    root.mainloop()

main_program()

