import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import json
import datetime


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

        from Utility_User_Interface import save_pop
        #save_pop()

    # deletes the listbox item from bill_dictionary, then removes it from the listbox, then saves the file
    def delete_dictionary_item(self, temp, filename):
        self.open_file(filename)
        self.dictionary.pop(temp)
        self.save_file(filename, self.dictionary)

    # Opens the file, updates the dictionary with new information, save it again
    def update_dictionary(self, new_item, filename):
        dictionary = self.open_file(filename)
        dictionary.update(new_item)
        self.save_file(filename, self.dictionary)

    def expenses_due_this_week(self):
        filename = "Expenses"
        due_this_week = []
        date_value = datetime.datetime.today().date()
        current = date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1
        temp_dict = MainProgram().open_file(filename)
        for key, value in temp_dict.items():
            if value[1] == current:
                due_this_week.append(key)
        return due_this_week

    def income_for_this_week(self):
        filename = "Income"
        income_this_week = []
        date_value = datetime.datetime.today().date()
        current = date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1
        temp_dict = MainProgram().open_file(filename)
        for key, value in temp_dict.items():
            if value[1] == current:
                income_this_week.append(key)
        return income_this_week
