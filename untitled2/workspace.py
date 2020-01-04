import json
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
import re

def update_dictionary(bill_name_entry, amount_due_entry, due_date_entry, interest_entry, total_entry, dictionary):
    from Expenses_User_Interface import bill_add_interaction
    import Main_Program
    bill_name = bill_name_entry.get()
    amount_due = float(amount_due_entry.get())
    due_date = int(due_date_entry.get())
    interest = float(interest_entry.get())
    total = float(total_entry.get())

    new_bill = {bill_name: [amount_due, due_date, interest, total]}

    # Open the file, update the dictionary with new information, save it again,
    # then display popup indicating successful save
    # reuses "dictionary" variable name
    Main_Program.open_file()
    dictionary.update(new_bill)
    Main_Program.save_file()

