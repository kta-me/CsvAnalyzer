import os
import pandas as pd
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
    df = pd.read_csv(file_name, header = None, sep = ';')
    rows_count = df.shape[0]
    column_count = df.shape[1]
    rows_count_label['text'] = rows_count
    columns_count_label['text'] = column_count

# Выборка столбца в список
def get_column(df, column_ix):
    rows_count = df.shape[0]
    output = []
    for i in range(rows_count):
        output.append(df.iat[i, column_ix])
    return output

