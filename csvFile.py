import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog as fd

def get_file():
    directory = os.getcwd()
    name = fd.askopenfilename(initialdir = directory)
    return name

def print_filename(file_name_label):
    file_name = get_file()
    file_name_label['text'] = file_name
    return file_name

def read(file_name, rows_count_label, columns_count_label):
    file = pd.read_csv(file_name, sep = ';', header = None)
    rows_count = file.shape[0]
    column_count = file.shape[1]
    rows_count_label['text'] = rows_count
    columns_count_label['text'] = column_count
    return file

def get_column(file, column_position):
    output = []
    rows_count = file.shape[0]
    cols_count = file.shape[1]
    for row in range(rows_count):
        output.append(file.iat[row, column_position])
    return output
