from tkinter import *
from tkinter.ttk import *


# Displays a popup to indicate the save was successful
def save_pop():
    window_name = 'save_popup'
    save_popup = Toplevel()

    # Gets the requested values of the height and width.
    window_width = save_popup.winfo_reqwidth()
    window_height = save_popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(save_popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(save_popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    save_popup.geometry("+{}+{}".format(position_right, position_down))

    label = Label(save_popup, text='Save Successful')
    label.grid(row=0, column=0, padx=20, pady=20)

    save_popup.after(1500, lambda: save_popup.destroy())
    save_popup.mainloop()


# Displays a popup confirming quiting the program
def quit_program():
    popup = Toplevel()
    popup.title('Quit Program')

    # Gets the requested values of the height and width.
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(position_right, position_down))

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

    # Gets the requested values of the height and width.
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(position_right, position_down))

    Label(popup, text='Are you sure?').grid(row=0, columnspan=2, padx=5, pady=5)
    Button(popup, text='Yes', command=confirm).grid(row=1, column=0, padx=5, pady=5)
    Button(popup, text='No', command=popup.destroy).grid(row=1, column=1, padx=5, pady=5)

    popup.mainloop()
    #return answer


# Displays a popup to indicate an invalid request
# Not in use yet
def cannot_do():
    popup = Toplevel()

    # Gets the requested values of the height and width.
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()

    # Gets both half the screen width/height and window width/height
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)

    # Positions the window in the center of the page.
    popup.geometry("+{}+{}".format(position_right, position_down))

    label = Label(popup, text='Invalid Request')
    label.grid(row=0, column=0, padx=30, pady=20)

    popup.after(1500, lambda: popup.destroy())
    popup.mainloop()
