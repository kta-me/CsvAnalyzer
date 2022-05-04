
import tkinter as tk

# Создание главного окна
def create_dialog():
    window = tk.Tk()
    window.geometry("550x550")
    window.title("Программа анализа .csv файлов")

    return window

def show_dialog(window):
    window.mainloop()