from tkinter import *
from tkinter.ttk import *


# Displays a popup to indicate the save was successful
def save_popup():
    save_popup = Toplevel()

    w = 170
    h = 70
    ws = save_popup.winfo_screenwidth()
    hs = save_popup.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    save_popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(save_popup, text='Save Successful')
    label.grid(row=0, column=0, padx=30, pady=20)

    save_popup.after(2500, lambda: save_popup.destroy())
    save_popup.mainloop()


# Displays a popup confirming quiting the program
def quit_program():
    popup = Toplevel()
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


# Request confirmation from user about specified request
def are_you_sure(answer):

    def confirm():
        popup.destroy()
        answer()

    popup = Toplevel()
    popup.title('Confirm Request')

    w = 195
    h = 70
    ws = popup.winfo_screenwidth()
    hs = popup.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

    Label(popup, text='Are you sure?').grid(row=0, columnspan=2, padx=5, pady=5)
    Button(popup, text='Yes', command=confirm).grid(row=1, column=0, padx=5, pady=5)
    Button(popup, text='No', command=popup.destroy).grid(row=1, column=1, padx=5, pady=5)

    popup.mainloop()
    return answer


# Displays a popup to indicate an invalid request
# Not in use yet
def cannot_do():
    popup = Toplevel()

    w = 175
    h = 70
    ws = popup.winfo_screenwidth()
    hs = popup.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

    label = Label(popup, text='Invalid Request')
    label.grid(row=0, column=0, padx=30, pady=20)

    popup.after(2500, lambda: popup.destroy())
    popup.mainloop()
