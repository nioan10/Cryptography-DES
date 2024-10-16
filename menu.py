import tkinter as tk
from tkinter import ttk

# Функция для перехода на главное меню
def show_main_menu():
    clear_screen()
    
    ttk.Label(root, text="Главное меню", style="TLabel").pack(pady=60)
    ttk.Button(root, text="Перейти к работе", command=show_work_menu, style="TButton").pack(pady=10)
    
    ttk.Button(root, text="Создатели", command=show_creators, style="TButton").pack(pady=10)
    ttk.Button(root, text="О программе", command=show_about, style="TButton").pack(pady=10)
    ttk.Button(root, text="Выход", command=root.quit, style="TButton").pack(pady=10)

# Функция для отображения раздела "Создатели"
def show_creators():
    clear_screen()
    ttk.Label(root, text="Создатели: (пока тихо мирно)", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_main_menu, style="TButton").pack(pady=10)

# Функция для отображения раздела "О программе"
def show_about():
    clear_screen()
    ttk.Label(root, text="Программа для работы с шифрованием DES.", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_main_menu, style="TButton").pack(pady=10)

# Функция для перехода к разделу "Перейти к работе"
def show_work_menu():
    clear_screen()
    
    ttk.Label(root, text="Установка и просмотр данных", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Задать данные", command=set_data, style="TButton").pack(pady=5)
    ttk.Button(root, text="Отобразить текущие данные", command=show_current_data, style="TButton").pack(pady=5)
    ttk.Label(root, text="Процессы шифрования и дешифровки", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Шифровка", command=show_encrypt, style="TButton").pack(pady=5)
    ttk.Button(root, text="Дешифровка", command=show_decrypt, style="TButton").pack(pady=5)
    ttk.Label(root, text="Характеризация лавинного эффекта", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Анализ лавинного эффекта", command=show_avalanche_effect, style="TButton").pack(pady=5)
    ttk.Button(root, text="Назад", command=show_main_menu, style="TButton").pack(pady=5)

# Функция для раздела "Шифровка"
def show_encrypt():
    clear_screen()
    ttk.Label(root, text="Раздел Шифрования данных", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

# Функция для раздела "Дешифровка"
def show_decrypt():
    clear_screen()
    ttk.Label(root, text="Раздел Дешифрования данных", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

# Функция для раздела "Анализ лавинного эффекта"
def show_avalanche_effect():
    clear_screen()
    ttk.Label(root, text="Раздел Анализ лавинного эффекта", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

# Функция для отображения текущих данных
def show_current_data():
    clear_screen()
    ttk.Label(root, text="Текущие данные: (здесь будут данные)", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

# Функция для задания данных
def set_data():
    clear_screen()
    ttk.Label(root, text="Введите новые данные", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

# Функция для очистки экрана
def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Основное окно
root = tk.Tk()
root.title("Программа анализа и шифрования по алгоритму DES")
root.geometry("800x500")
root.configure(bg="#ADD8E6")  # Устанавливаем темный фон

# Настройка темной темы с использованием ttk стилей
style = ttk.Style()

# Настройка стилей для кнопок и меток
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#444444", foreground="black")
style.configure("TLabel", font=("Helvetica", 12), background="#ADD8E6", foreground="black")



# Запуск приложения
show_main_menu()
root.mainloop()
