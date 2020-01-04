import tkinter as tk
from tkinter import *
from tkinter.ttk import *


def main_program():
    # Need to build main page layout
    # display all bills
    # display graph
    # place buttons for adding/removing/editing/etc.
    # create menu bar
    # choose colors
    from Expenses_User_Interface import bill_add_interaction, edit_expense_interaction
    from Utility_User_Interface import quit_program

    root = tk.Tk()
    root.title('Money Manager')
    root.attributes('-fullscreen', True)

    Button(root, text='Add Expense', command=bill_add_interaction).grid(row=0, column=0, padx=10, pady=10)
    Button(root, text='Remove Expense', command=edit_expense_interaction).grid(row=0, column=1, padx=10, pady=10)
    Button(root, text='Quit', command=quit_program).grid(row=0, column=2, padx=10, pady=10)

    # Create display showing bills due this week
    # due_this_week = Button(root, text='View Bills Due This Week', command=pass)
    # due_this_week.grid(row=0, column=3, padx=10, pady=10)

    root.mainloop()

main_program()