import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import json


# This class works with the dictionary information
class MainProgram:
    # Opens .json file based on which is needed (expenses or income)
    def open_file(self, filename):
        try:
            with open(filename + '.json', 'r') as read_file:
                self.dictionary = json.load(read_file)
                return self.dictionary

        except:
            self.dictionary = {}
            return self.dictionary

    # Saves the dictionary to the .json file, then displays the "save successful" popup
    def save_file(self, filename, dictionary):
        with open(filename + '.json', 'w') as write_file:
            json.dump(dictionary, write_file)
            from Utility_User_Interface import save_popup
            save_popup()

    # deletes the listbox item from bill_dictionary, then removes it from the listbox, then saves the file
    def delete_dictionary_item(self, temp, filename):
        self.open_file(filename)
        self.dictionary.pop(temp)
        self.save_file(filename, self.dictionary)
        from Utility_User_Interface import save_popup
        save_popup()

    # Opens the file, updates the dictionary with new information, save it again
    def update_dictionary(self, new_bill, filename):
        dictionary = self.open_file(filename)
        dictionary.update(new_bill)
        self.save_file(filename, self.dictionary)

