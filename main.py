import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st

import dialog
import csvFile

def process_button():
    file_name = csvFile.print_filename(file_name_label)
    file = csvFile.read(file_name, rows_count_label, columns_count_label)
    column = csvFile.get_column(file, 0)
    for row in column:
        output_text.insert(tk.END, str(row) + os.linesep)

window = dialog.create_dialog()

dialog.show_label("Файл:", 0)
file_name_label = tk.Label(text = "")
file_name_label.grid(row = 0, column = 1, sticky = "w")

dialog.show_label("Строк:", 1)
rows_count_label = tk.Label(text = "")
rows_count_label.grid(row = 1, column = 1, sticky = "w")

dialog.show_label("Столбцов:", 2)
columns_count_label = tk.Label(text = "")
columns_count_label.grid(row = 2, column = 1, sticky = "w")

output_text = st(height = 22, width = 50)
output_text.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = "w")

dialog.show_button(window, process_button)
dialog.show_dialog(window)
