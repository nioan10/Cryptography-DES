import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

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

def set_data():
    clear_screen()
    
    # Функция для задания данных
    # Выпадающий список для выбора формата текста
    ttk.Label(root, text="Выберите формат текста:", style="TLabel", anchor="center").pack(pady=5)
    text_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
    text_format.pack(pady=5)
    text_format.current(2)  # По умолчанию "Обычный"

    # Поле для ввода текста
    ttk.Label(root, text="Введите текст:", style="TLabel", anchor="center").pack(pady=5)
    text_entry = ttk.Entry(root, width=50)
    text_entry.pack(pady=5)

    # Выпадающий список для выбора формата ключа
    ttk.Label(root, text="Выберите формат ключа:", style="TLabel", anchor="center").pack(pady=5)
    key_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный"], state="readonly")
    key_format.pack(pady=5)
    key_format.current(1)  # По умолчанию "Шестнадцатиричный"

    # Поле для ввода ключа
    ttk.Label(root, text="Введите ключ:", style="TLabel", anchor="center").pack(pady=5)
    key_entry = ttk.Entry(root, width=50)
    key_entry.pack(pady=5)

    # Кнопка для сохранения введенных данных с проверкой
    ttk.Button(root, text="Сохранить данные", style="TButton", command=lambda: save_data(text_entry, text_format, key_entry, key_format)).pack(pady=10)

    # Кнопка для возврата к рабочему меню
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)
    
    # Пояснительный текст внизу с выравниванием по центру
    note = ("Текст должен содержать ровно 64 бита в бинарном формате, 8 символов текста, или 16 символов в шестнадцатиричном формате.\n"
            "Ключ: строго 56 бит в бинарном, 7 символов в текстовом или 14 в шестнадцатиричном формате.")
    ttk.Label(root, text=note, style="Small.TLabel", anchor="center").pack(side="bottom", pady=20)



# Функция для сохранения данных с проверками
def save_data(text_entry, text_format, key_entry, key_format):
    text = text_entry.get()
    text_format_selected = text_format.get()
    key = key_entry.get()
    key_format_selected = key_format.get()

    if text_format_selected == "Бинарный":
        if len(text) != 64:
            messagebox.showerror("Ошибка", "Текст в бинарном формате должен содержать ровно 64 бита.")
            return
    elif text_format_selected == "Шестнадцатиричный":
        if len(text) != 16:
            messagebox.showerror("Ошибка", "Текст в шестнадцатиричном формате должен содержать ровно 16 символов.")
            return
    elif text_format_selected == "Обычный":
        if len(text) != 8:
            messagebox.showerror("Ошибка", "Текст должен содержать ровно 8 символов.")
            return

    # Проверка ключа
    if key_format_selected == "Бинарный":
        if len(key) != 56:
            messagebox.showerror("Ошибка", "Ключ должен содержать ровно 56 бит.")
            return
    elif key_format_selected == "Шестнадцатиричный":
        if len(key) != 14:
            messagebox.showerror("Ошибка", "Ключ должен содержать ровно 14 шестнадцатиричных символов.")
            return

    # Если все проверки пройдены
    print("Текст и ключ успешно сохранены.")
    print(f"Текст: {text}")
    print(f"Формат текста: {text_format_selected}")
    print(f"Ключ: {key}")
    print(f"Формат ключа: {key_format_selected}")





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
style.configure("Small.TLabel", font=("Helvetica", 8), background="#ADD8E6", foreground="black")



# Запуск приложения
show_main_menu()
root.mainloop()
