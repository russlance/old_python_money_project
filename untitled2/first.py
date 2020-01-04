import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import json


class BillInteraction:

    # Populate the bill_dictionary with the information from the billsfile.txt
    # This allows access to saved information for entirety of BillInteraction
    def __init__(self):
        self.answer = bool
        self.answer = False
        self.bill_dictionary = {}

    # deletes the listbox item from bill_dictionary, then removes it from the listbox, then saves the file
    def confirm(self):
        lb = self.lb.get(ANCHOR)
        self.bill_dictionary.pop(lb)
        print(self.bill_dictionary)
        self.lb.delete(ANCHOR)
        self.save_file()
        self.answer = False
        popup.destroy()

    def open_file(self):
        try:
            with open('billsfile.json', 'r') as read_file:
                self.bill_dictionary = json.load(read_file)
        except:
            pass

    def save_file(self):
        with open('billsfile.json', 'w') as write_file:
            json.dump(self.bill_dictionary, write_file)
            save_popup()

    def update_dictionary(self):
        bill_name = self.bill_name_entry.get()
        amount_due = float(self.amount_due_entry.get())
        due_date = int(self.due_date_entry.get())
        interest = float(self.interest_entry.get())
        total = float(self.total_entry.get())

        new_bill = {bill_name: [amount_due, due_date, interest, total]}

        #Open the txt, update the dictionary with new information, save it again,
        # then display popup indicating successful save
        self.open_file()
        self.bill_dictionary.update(new_bill)
        self.save_file()

    def bill_add_interaction(self):
        add_bill = tk.Tk()
        add_bill.title('Add/Edit Bills')

        dd_variable = StringVar(add_bill)

    # In txt file:
        # 1st item is Bill Name,
        # 2nd item - Amount Due
        # 3rd item = Due Date
        # 4th item = Interest Rate
        # 5th item = Total Due
        Label(add_bill, text='Bill Name:').grid(row=0, column=0, sticky=E, padx=10, pady=5)
        self.bill_name_entry = Entry(add_bill)
        self.bill_name_entry.grid(row=0, column=1, padx=10)

        Label(add_bill, text='Amount Due:').grid(row=1, column=0, sticky=E, padx=10, pady=5)
        self.amount_due_entry = Entry(add_bill)
        self.amount_due_entry.grid(row=1, column=1)

        # Dropdown for selecting week of the month the bill is due
        Label(add_bill, text='What week do you pay this bill?').grid(row=2, column=0, sticky=E, padx=10, pady=5)
        choices = ['1', '2', '3', '4']
        # set the default option
        dd_variable.set('1')
        self.due_date_entry = OptionMenu(add_bill, dd_variable, *choices)


        self.due_date_entry.grid(row=2, column=1)
        self.due_date_entry = dd_variable

        Label(add_bill, text='Interest Rate:').grid(row=3, column=0, sticky=E, padx=10, pady=5)
        self.interest_entry = Entry(add_bill)
        self.interest_entry.grid(row=3, column=1)

        Label(add_bill, text='Total Due:').grid(row=4, column=0, sticky=E, padx=10, pady=5)
        self.total_entry = Entry(add_bill)
        self.total_entry.grid(row=4, column=1)

        save_button = Button(add_bill, text='Save', command=lambda: [self.update_dictionary, self.bill_add_interaction])
        save_button.grid(row=5, column=0, padx=10, pady=10)
        finish_button = Button(add_bill, text='Finish', command=add_bill.destroy)
        finish_button.grid(row=5, column=1, padx=10, pady=10)

        add_bill.mainloop()

    # use scroll widget to display all bill names so user can scroll through them to delete the one they way
    # need function to be called from any part of program
    def remove_bill_interaction(self):
        bill_remove = tk.Tk()
        bill_remove.title('Remove Bill')

        Label(bill_remove, text='Select an Expense').grid(row=0, columnspan=2, padx=5, pady=5)

        # Creates a listbox with names of the bills (keys from 'bill_dictionary')
        self.lb = Listbox(bill_remove, selectmode=SINGLE)
        self.lb.grid(row=1, columnspan=2, padx=5, pady=5)
        self.open_file()
        for key in self.bill_dictionary:
            self.lb.insert(END, key)

        eb = Button(bill_remove, text="Edit")
        eb.grid(row=2, column=0, padx=5, pady=5)

        rb = Button(bill_remove, text='Remove', command=self.are_you_sure)
        rb.grid(row=2, column=1, padx=5, pady=5)

        fb = Button(bill_remove, text='Finish', command=bill_remove.destroy)
        fb.grid(row=3, columnspan=2, padx=5, pady=5)

        bill_remove.mainloop()

    # request confirmation from user about specified request returning boolean "answer=true"
    # needs more work
    def are_you_sure(self):

        popup = tk.Tk()
        popup.title('Confirm Request')

        w = 195
        h = 70
        ws = popup.winfo_screenwidth()
        hs = popup.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

        Label(popup, text='Are you sure?').grid(row=0, columnspan=2, padx=5, pady=5)
        Button(popup, text='Yes', command=lambda: self.confirm).grid(row=1, column=0, padx=5, pady=5)
        Button(popup, text='No', command=popup.destroy).grid(row=1, column=1, padx=5, pady=5)

        popup.mainloop()


# Displays a popup confirming quiting the program
def quit_program():
    popup = tk.Tk()
    popup.title('Quit Program')

    w = 255
    h = 60
    ws = popup.winfo_screenwidth()
    hs = popup.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Button(popup, text='Yes', command=quit).grid(row=0, column=0, padx=20, pady=20)
    Button(popup, text='No', command=popup.destroy).grid(row=0, column=1, padx=20, pady=20)

    popup.mainloop()

# Displays a popup to indicate the save was successful
def save_popup():
    save_pop = Toplevel()

    w = 175
    h = 70
    ws = save_pop.winfo_screenwidth()
    hs = save_pop.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    save_pop.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(save_pop, text='Save Successful')
    label.grid(row=0, column=0, padx=30, pady=20)

    save_pop.after(2500, lambda: save_pop.destroy())
    save_pop.mainloop()


# Displays a popup to indicate an invalid request
def cannot_do():
    invalid_request = Toplevel()

    w = 175
    h = 70
    ws = invalid_request.winfo_screenwidth()
    hs = invalid_request.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    invalid_request.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(invalid_request, text='Invalid Request')
    label.grid(row=0, column=0, padx=30, pady=20)

    invalid_request.after(2500, lambda: invalid_request.destroy())
    invalid_request.mainloop()


def open_file(bill_dictionary):
    bill_dictionary = {}
    try:

        with open('billsfile.txt', 'r') as read_file:
            bill_dictionary = json.load(read_file)

    except:
        pass
    return bill_dictionary


# Program starts here
# Need to build main page layout
# display all bills
# display graph
# place buttons for adding/removing/editing/etc.
# create menu bar
# choose colors
root = tk.Tk()
root.title('Money Manager')
root.attributes('-fullscreen', True)

b_i = BillInteraction()

add_button = Button(root, text='Add/Update Bill', command=b_i.bill_add_interaction)
remove_button = Button(root, text='Remove Bill', command=b_i.remove_bill_interaction)
quit_button = Button(root, text='Quit', command=quit_program)

#due_this_week = Button(root, text='View Bills Due This Week', command=pass)
#due_this_week.grid(row=0, column=3, padx=10, pady=10)

add_button.grid(row=0, column=0, padx=10, pady=10)
remove_button.grid(row=0, column=1, padx=10, pady=10)
quit_button.grid(row=0, column=2, padx=10, pady=10)

# MainWindow()
root.mainloop()
