from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import json

def open_file(filename):
    dictionary = {}

    try:
        with open(filename + '.json', 'r') as read_file:
            dictionary = json.load(read_file)
            #return dictionary

    except:
        return dictionary


def save_file(filename, dictionary):
    with open(filename + '.json', 'w') as write_file:
        json.dump(dictionary, write_file)


filename = "expenses"
open_file(filename)
print(open_file(filename))

save_file(filename, open_file(filename))