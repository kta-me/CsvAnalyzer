import tkinter as tk

# Создание главного окна
def create_dialog():
    window = tk.Tk()
    window.geometry("550x550")
    window.title("Программа анализа .csv файлов")

    return window

def show_dialog(window):
    window.mainloop()

def show_label(label, rowNumber):
    third_label = tk.Label(text = label)
    third_label.grid(row = rowNumber, column = 0, padx = 10, pady = 10, sticky = "e")

def show_button(window, on_click):
    button = tk.Button(window, text = "Прочитать файл", command = on_click)
    button.grid(row = 4, column = 1)