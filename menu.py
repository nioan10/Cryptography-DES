import tkinter as tk
from tkinter import ttk
import os
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
    creators_message = (
        "Создатели программы:\n\n"
        "Разработка программы: Тузов Алексей\n"
        "Комплектация отчета: Шомполов Максим\n"
        "Помощь: Чистякова Полина\n"
        "Моральная поддержка: Завывающий ветер в 9 часов вечера\n\n"
        "Особая благодарность нейронной сети, которая рассказала о нужных библиотеках и научила ими пользоваться\n"
        "И, конечно, тем, кто принес вкусняшки в самый нужный момент 😄"
    )
        # Показать информационное сообщение с информацией о создателях
    messagebox.showinfo("Создатели программы", creators_message)
        # Возвращаемся в главное меню после закрытия окна
    show_main_menu()


# Функция для отображения раздела "О программе"
def show_about():
    clear_screen()
    about_message = (
        "Эта программа создана для шифрования блоков текста с использованием алгоритма DES.\n"
        "Программа позволяет зашифровать и расшифровать текст, а также проводить анализ лавинного эффекта.\n\n"
        "Основные возможности программы:\n"
        "1. Шифрование и дешифрование данных с использованием алгоритма DES.\n"
        "2. Возможность задания текста и ключа в различных форматах (бинарный, шестнадцатиричный, обычный).\n"
        "3. Анализ лавинного эффекта для проверки устойчивости алгоритма к небольшим изменениям данных.\n\n"
        "Программа предоставляет простой и удобный графический интерфейс для работы с шифрованием.\n"
        "Автор программы: Тузов Алексей\n"
        "Версия: 0.999\n"
        "Дата создания: 2024"
    )
    
    show_main_menu()   
    messagebox.showinfo("О программе", about_message)


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

# Функции для преобразования данных
def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def text_to_hex(text):
    return ''.join(format(ord(c), '02x') for c in text).upper()

def binary_to_text(binary_data):
    return ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

def hex_to_text(hex_data):
    return ''.join(chr(int(hex_data[i:i+2], 16)) for i in range(0, len(hex_data), 2))

# Функция для отображения текущих данных (текст и ключ)
def show_current_data():
    clear_screen()

    # Получаем путь к папке проекта
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка, где находится скрипт
    project_files_folder = os.path.join(project_folder, "project_files")
    
    text_data = ""
    key_data = ""
    text_format = ""
    key_format = ""

    # Проверка наличия файла с текстом
    text_filename = os.path.join(project_files_folder, "text_data.txt")
    if os.path.exists(text_filename):
        with open(text_filename, 'r') as file:
            lines = file.readlines()
            text_format = lines[0].strip().split(": ")[1]
            text_data = lines[1].strip().split(": ")[1]
    else:
        messagebox.showerror("Ошибка", "Файл с текстом не найден. Данные еще не были сохранены.")
        return

    # Проверка наличия файла с ключом
    key_filename = os.path.join(project_files_folder, "key_data.txt")
    if os.path.exists(key_filename):
        with open(key_filename, 'r') as file:
            lines = file.readlines()
            key_format = lines[0].strip().split(": ")[1]
            key_data = lines[1].strip().split(": ")[1]
    else:
        messagebox.showerror("Ошибка", "Файл с ключом не найден. Данные еще не были сохранены.")
        return

    # Функция для конвертации данных во все форматы
    def convert_and_show_all_formats():
        # Конвертируем текст
        if text_format == "Бинарный":
            original_text = binary_to_text(text_data)
            hex_text = hex(int(text_data, 2))[2:].upper()
            binary_text = text_data
        elif text_format == "Шестнадцатиричный":
            original_text = hex_to_text(text_data)
            hex_text = text_data
            binary_text = bin(int(text_data, 16))[2:].zfill(64)
        else:
            original_text = text_data
            hex_text = text_to_hex(text_data)
            binary_text = text_to_binary(text_data)

        # Конвертируем ключ
        if key_format == "Бинарный":
            original_key = binary_to_text(key_data)
            hex_key = hex(int(key_data, 2))[2:].upper()
            binary_key = key_data
        elif key_format == "Шестнадцатиричный":
            original_key = hex_to_text(key_data)
            hex_key = key_data
            binary_key = bin(int(key_data, 16))[2:].zfill(56)

        # Отображаем результат конвертации для текста
        ttk.Label(root, text="Текущий текст:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный: {original_text}", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатиричный: {hex_text}", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {binary_text}", style="TLabel").pack(pady=5)

        # Отображаем результат конвертации для ключа
        ttk.Label(root, text="Текущий ключ:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатиричный: {hex_key}", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {binary_key}", style="TLabel").pack(pady=5)

    # Отображаем конвертированные данные сразу во всех форматах
    convert_and_show_all_formats()

    # Кнопка для возврата в главное меню
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)




def set_data():
    clear_screen()
    
    # Функция для задания данных
    # Выпадающий список для выбора формата текста
    ttk.Label(root, text="Выберите формат блока текста:", style="TLabel", anchor="center").pack(pady=5)
    text_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
    text_format.pack(pady=5)
    text_format.current(2)  # По умолчанию "Обычный"

    # Поле для ввода текста
    ttk.Label(root, text="Введите блок текста:", style="TLabel", anchor="center").pack(pady=5)
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

# Функция для сохранения данных с проверками и выводом ошибок в виде всплывающих окон
def save_data(text_entry, text_format, key_entry, key_format):
    text = text_entry.get()
    text_format_selected = text_format.get()
    key = key_entry.get()
    key_format_selected = key_format.get()

    # Проверка текста
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

    # Получаем путь к папке проекта
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка, где находится скрипт
    project_files_folder = os.path.join(project_folder, "project_files")

    # Создаем папку для файлов, если она не существует
    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    # Если все проверки пройдены, сохраняем текст и ключ в файлы в папке проекта
    try:
        # Сохраняем текст в файл
        text_filename = os.path.join(project_files_folder, "text_data.txt")
        with open(text_filename, 'w') as file:
            file.write(f"Формат текста: {text_format_selected}\n")
            file.write(f"Данные текста: {text}\n")
            messagebox.showinfo("Успех", f"Текст успешно записан/перезаписан в файл {text_filename}.")
        
        # Сохраняем ключ в файл
        key_filename = os.path.join(project_files_folder, "key_data.txt")
        with open(key_filename, 'w') as file:
            file.write(f"Формат ключа: {key_format_selected}\n")
            file.write(f"Данные ключа: {key}\n")
            messagebox.showinfo("Успех", f"Ключ успешно записан/перезаписан в файл {key_filename}.")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении: {str(e)}")
        return


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
