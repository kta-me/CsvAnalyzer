# Программа анализа .csv файлов

import os
import tkinter as tk
import pandas as pd
import dialog

from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd

window = dialog.create_dialog()

def show_label(label, rowNumber):
    third_label = tk.Label(text = label)
    third_label.grid(row = rowNumber, column = 0, padx = 10, pady = 10, sticky = "e")

# Создание меток вывода
show_label("Файл:", 0)
first_label = tk.Label(text = "")
first_label.grid(row = 0, column = 1, sticky = "w")

show_label("Строк:", 1)
second_label = tk.Label(text = "")
second_label.grid(row = 1, column = 1, sticky = "w")

show_label("Столбцов:", 2)
third_label = tk.Label(text = "")
third_label.grid(row = 2, column = 1, sticky = "w")

output_text = st(height = 22, width = 50)
output_text.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = "w")

# Диалог открытия файла
def show_dialog():
    directory = os.getcwd()
    name = fd.askopenfilename(initialdir = directory)
    return name

def read_csv(file_name):
    df = pd.read_csv(file_name, header=None, sep=';')
    rows_count = df.shape[0]
    column_count = df.shape[1]
    second_label['text'] = rows_count
    third_label['text'] = column_count

# Выборка столбца в список
def get_column(df, column_ix):
    rows_count = df.shape[0]
    output = []
    for i in range(rows_count):
        output.append(df.iat[i, column_ix])
    return output

# Обработчик нажатия кнопки
def process_button():
    file_name = show_dialog()
    first_label['text'] = file_name
    df = read_csv(file_name)
    content = get_column(df, 0)

    for item in content:
        output_text.insert(tk.END, str(item) + os.linesep)

    mb.showinfo(title = None, message = "Готово")#####################

# Создание кнопки
button = tk.Button(window, text = "Прочитать файл", command = process_button)
button.grid(row = 4, column = 1)

dialog.show_dialog(window)

