##########################################################################################################
# 
# # Шаблон комментария раздела
#                   
##########################################################################################################

import tkinter as tk
from tkinter import ttk
import os
import tkinter.messagebox as messagebox
import coding
import time


##########################################################################################################
# 
# # Главная функция главного меню - сюрприз - сюриприз
#                   
##########################################################################################################
def show_main_menu():
    clear_screen()
    
    ttk.Label(root, text="Главное меню", style="TLabel").pack(pady=60)
    ttk.Button(root, text="Перейти к работе", command=show_work_menu, style="TButton").pack(pady=10)
    
    ttk.Button(root, text="Создатели", command=show_creators, style="TButton").pack(pady=10)
    ttk.Button(root, text="О программе", command=show_about, style="TButton").pack(pady=10)
    ttk.Button(root, text="Выход", command=root.quit, style="TButton").pack(pady=10)

##########################################################################################################
# 
# # Функции отображения информации о программе.
#                   Реализация основална на методе messagebox библиотеки tkinter
##########################################################################################################
# Функция для отображения раздела Создатели"
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
    ttk.Button(root, text="Шифрование и дешифровка", command=show_encrypt_decrypt, style="TButton").pack(pady=5)
    ttk.Label(root, text="Характеризация лавинного эффекта", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Анализ лавинного эффекта", command=show_avalanche_effect, style="TButton").pack(pady=5)
    ttk.Button(root, text="Назад", command=show_main_menu, style="TButton").pack(pady=5)

##########################################################################################################
# 
# # Реализация меню шифрования и дешифровки
#                   
##########################################################################################################

def get_current_data():
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка, где находится скрипт
    project_files_folder = os.path.join(project_folder, "project_files")
    
    text_filename = os.path.join(project_files_folder, "text_data.txt")
    key_filename = os.path.join(project_files_folder, "key_data.txt")
    
    # Проверяем, существуют ли файлы с данными
    if not os.path.exists(text_filename) or not os.path.exists(key_filename):
        messagebox.showerror("Ошибка", "Данные не найдены.")
        return None, None, None, None

    # Чтение текстового файла
    with open(text_filename, 'r') as text_file:
        text_format = text_file.readline().strip().split(": ")[1]  # Формат текста
        text_data = text_file.readline().strip().split(": ")[1]     # Данные текста

    # Чтение ключевого файла
    with open(key_filename, 'r') as key_file:
        key_format = key_file.readline().strip().split(": ")[1]  # Формат ключа
        key_data = key_file.readline().strip().split(": ")[1]     # Данные ключа

    return text_format, text_data, key_format, key_data

def show_encrypt_decrypt():
    clear_screen()  # Очищаем текущее содержимое экрана

    # Всплывающее окно для выбора действия
    window = tk.Toplevel(root)
    window.title("Выберите действие")
    
    ttk.Label(window, text="Выберите действие", style="TLabel").pack(pady=10)
    

    style.configure("Small.TLabel", font=("Helvetica", 8))  # Установили шрифт и размер 8

    def on_encrypt():
        # Загружаем данные из файлов
        text_format, text, key_format, key = get_current_data()
        if text is None or key is None:
            return  # Если данные не найдены, завершить выполнение

        # Преобразуем текст и ключ в бинарный и шестнадцатеричный форматы
        if text_format == "Обычный":
            text_binary = text_to_binary(text)
            text_hex = text_to_hex(text)
        elif text_format == "Шестнадцатиричный":
            text_binary = hex_to_binary(text)  # Преобразуем из hex в binary
            text_hex = text  # Уже в hex
        elif text_format == "Бинарный":
            text_binary = text  # Уже в бинарном виде
            text_hex = binary_to_hex(text)

        if key_format == "Обычный":
            key_binary = text_to_binary(key)
            key_hex = text_to_hex(key)
        elif key_format == "Шестнадцатиричный":
            key_binary = hex_to_binary(key)  # Преобразуем из hex в binary
            key_hex = key  # Уже в hex
        elif key_format == "Бинарный":
            key_binary = key  # Уже в бинарном виде
            key_hex = binary_to_hex(key)

    
        # Отображаем текущий текст в бинарном и шестнадцатеричном форматах
        ttk.Label(root, text=f"Текущий текст (bin): {text_binary}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Текущий текст (hex): {text_hex}", style="Small.TLabel").pack(pady=5)

        # Отображаем текущий ключ в бинарном и шестнадцатеричном форматах
        ttk.Label(root, text=f"Текущий ключ (bin): {key_binary}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Текущий ключ (hex): {key_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"_____________________________________________________________", style="Small.TLabel").pack(pady=5)


        print(key_binary, len(key_binary))
        try:
            expanded_key = coding.add_parity_bits(key_binary)  # Функция расширения ключа
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при расширении ключа: {str(e)}")
            return

        start_time = time.time()
        # Шифруем данные с помощью функции из файла coding.py
        try:
            encrypted_data = coding.encrypt(text_binary, expanded_key)  # Используем расширенный ключ

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при шифровании: {str(e)}")
            return

        end_time = time.time()  # Конец отсчета времени
        encryption_time = end_time - start_time  # Время выполнения шифрования

        # Отображаем результат шифрования
        ttk.Label(root, text=f"Зашифрованный текст: {encrypted_data}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Время шифрования: {encryption_time:.6f} секунд", style="Small.TLabel").pack(pady=5)
        # Записываем зашифрованный текст в файл
        save_encrypted_data(encrypted_data)
        # Записываем расширенный ключ в файл
        save_expanded_key(expanded_key)
        ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)


    def on_decrypt():
        # Загружаем информацию из файлов
        encrypted_data, expanded_key = load_encrypted_data_and_key()
        if encrypted_data is None or expanded_key is None:
            return  # Если данные не найдены, возвращаемся в главное меню

        # Отображаем шифрованный текст в бинарном и шестнадцатеричном форматах
        ttk.Label(root, text=f"Шифрованный текст (bin): {encrypted_data}", style="Small.TLabel").pack(pady=5)
        encrypted_hex = binary_to_hex(encrypted_data)  # Преобразуем в hex
        ttk.Label(root, text=f"Шифрованный текст (hex): {encrypted_hex}", style="Small.TLabel").pack(pady=5)

        # Отображаем расширенный ключ в бинарном и шестнадцатеричном форматах
        ttk.Label(root, text=f"Расширенный ключ (bin): {expanded_key}", style="Small.TLabel").pack(pady=5)
        key_hex = binary_to_hex(expanded_key)  # Преобразуем в hex
        ttk.Label(root, text=f"Расширенный ключ (hex): {key_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"_____________________________________________________________", style="Small.TLabel").pack(pady=5)
        # Дешифруем данные с помощью функции из файла coding.py

        try:
            decrypted_binary = coding.decrypt(encrypted_data, expanded_key)  # Используем расширенный ключ
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при дешифровке: {str(e)}")
            return

        # Преобразуем дешифрованный текст в различные форматы
        decrypted_text = binary_to_text(decrypted_binary)  # Обычный текст
        decrypted_hex = binary_to_hex(decrypted_binary)  # Шестнадцатеричный формат

        # Отображаем результаты дешифровки
        ttk.Label(root, text=f"Дешифрованный текст (обычный): {decrypted_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Дешифрованный текст (hex): {decrypted_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Дешифрованный текст (bin): {decrypted_binary}", style="Small.TLabel").pack(pady=5)

        # Отображаем ключ в бинарном и шестнадцатеричном форматах
        key_hex = binary_to_hex(expanded_key)
        ttk.Label(root, text=f"Ключ (hex): {key_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Ключ (bin): {expanded_key}", style="Small.TLabel").pack(pady=5)
        ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)


    

        
    # Кнопки для выбора действий
    ttk.Button(window, text="Шифрование", command=lambda: [on_encrypt(), window.destroy()]).pack(pady=5)
    ttk.Button(window, text="Дешифровка", command=lambda: [on_decrypt(), window.destroy()]).pack(pady=5)

def load_encrypted_data_and_key():
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")

    # Файлы с зашифрованным текстом и расширенным ключом
    encrypted_filename = os.path.join(project_files_folder, "encrypted_text.txt")
    key_filename = os.path.join(project_files_folder, "expanded_key.txt")
        
    # Проверка существования файлов
    if not os.path.exists(encrypted_filename) or not os.path.exists(key_filename):
        messagebox.showerror("Ошибка", "Файлы с зашифрованным текстом или ключом не найдены.")
        show_work_menu()  # Возвращаемся в главное меню
        return None, None

    # Загрузка зашифрованного текста
    with open(encrypted_filename, 'r') as file:
        encrypted_data = file.readlines()[1].strip().split(": ")[1]

        # Загрузка расширенного ключа
    with open(key_filename, 'r') as file:
        expanded_key = file.readlines()[1].strip().split(": ")[1]

    return encrypted_data, expanded_key

def save_encrypted_data(encrypted_data):
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")  # Папка project_files
    encrypted_filename = os.path.join(project_files_folder, "encrypted_text.txt")
    
    # Открываем файл и записываем зашифрованный текст
    with open(encrypted_filename, 'w') as file:
        file.write("Формат: Бинарный\n")
        file.write(f"Данные: {encrypted_data}\n")
    messagebox.showinfo("Результат шифрования", f"Шифрованный файл записан в файл {encrypted_filename}")

def save_expanded_key(expanded_key):
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")  # Папка project_files
    key_filename = os.path.join(project_files_folder, "expanded_key.txt")

    # Открываем файл и записываем расширенный ключ
    with open(key_filename, 'w') as file:
        file.write("Формат: Бинарный\n")
        file.write(f"Данные: {expanded_key}\n")
    
    messagebox.showinfo("Результат шифрования", f"Шифрованный ключ записан в файл {key_filename}")


##########################################################################################################
# 
# # Функция для раздела "Анализ лавинного эффекта"
#                   
##########################################################################################################

def show_avalanche_effect():
    clear_screen()
    ttk.Label(root, text="Раздел Анализ лавинного эффекта", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

##########################################################################################################
# # Отображение данных
# #         Данные хранятся в соответствующем файле. Раздел содержит дополнительные функции дешифровки
#               данных для отображения информации во всех доступных форматах  
##########################################################################################################

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def text_to_hex(text):
    return ''.join(format(ord(c), '02x') for c in text).upper()

def binary_to_text(binary_data):
    return ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

def hex_to_text(hex_data):
    return ''.join(chr(int(hex_data[i:i+2], 16)) for i in range(0, len(hex_data), 2))

def binary_to_hex(binary_data):
    return ''.join(format(int(binary_data[i:i+4], 2), 'x') for i in range(0, len(binary_data), 4)).upper()

def hex_to_binary(hex_data):
    return ''.join(format(int(c, 16), '04b') for c in hex_data)



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
        else:
            original_key = key_data
            hex_key = text_to_hex(key_data)
            binary_key = text_to_binary(key_data)

        # Отображаем результат конвертации для текста
        ttk.Label(root, text="Текущий текст:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный: {original_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатиричный: {hex_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {binary_text}", style="Small.TLabel").pack(pady=5)

        # Отображаем результат конвертации для ключа
        ttk.Label(root, text="Текущий ключ:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный: {original_key}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатиричный: {hex_key}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {binary_key}", style="Small.TLabel").pack(pady=5)
    convert_and_show_all_formats()

    def convert_encrypt():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        encrypted_data_file = os.path.join(current_directory, "project_files", "encrypted_text.txt")
        expanded_key_file = os.path.join(current_directory, "project_files", "expanded_key.txt")

        if not os.path.exists(encrypted_data_file) or not os.path.exists(expanded_key_file):
            messagebox.showerror("Ошибка", "Файлы с зашифрованной информацией или ключом не найдены.")
            return

        # Чтение шифрованной информации и расширенного ключа
        with open(encrypted_data_file, 'r') as file:
            encrypted_data = file.readlines()[1].strip().split(": ")[1]

        with open(expanded_key_file, 'r') as file:
            expanded_key = file.readlines()[1].strip().split(": ")[1]

        # Преобразуем зашифрованные данные во все форматы
        encrypted_text = binary_to_text(encrypted_data)
        encrypted_hex = binary_to_hex(encrypted_data)
            
        key_text = binary_to_text(expanded_key)
        key_hex = binary_to_hex(expanded_key)

        # Отображаем текущие данные в разных форматах перед полями для редактирования
        ttk.Label(root, text="Текущие зашифрованные данные:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный текст: {encrypted_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатеричный: {encrypted_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {encrypted_data}", style="Small.TLabel").pack(pady=5)

        ttk.Label(root, text="Текущий ключ:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный текст: {key_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатеричный: {key_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {expanded_key}", style="Small.TLabel").pack(pady=5) 
    convert_encrypt()   
    # Кнопка для возврата в главное меню
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

    note = ("Примечание: Данные могут не совпадать, если они были изменены.")
    ttk.Label(root, text=note, style="Small.TLabel", anchor="center").pack(side="bottom", pady=20)


##########################################################################################################
# # Раздел задачи данных
# #         В данном разделе предусмотрены функции задачи данных для шифрования блока текста алгоритмом DES
#               Условия: Блок текста - строго 64 бита, ключ - строго 56 бит
#               Включена: Запись данных в файл, включая информацию о формате заданных данных
##########################################################################################################

def set_data():
    clear_screen()
    
    # Всплывающее окно для выбора типа данных
    window = tk.Toplevel(root)
    window.title("Выберите тип данных")
    
    ttk.Label(window, text="Выберите тип данных", style="TLabel").pack(pady=10)
    
    # Функция для обработки обычных данных
    def handle_regular_data():
        window.destroy()  # Закрываем окно выбора
        
        # Выпадающий список для выбора формата текста
        ttk.Label(root, text="Выберите формат блока текста:", style="TLabel", anchor="center").pack(pady=5)
        text_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
        text_format.pack(pady=5)
        text_format.current(2)  # По умолчанию "Обычный"

        # Поле для ввода текста
        ttk.Label(root, text="Введите блок текста:", style="TLabel", anchor="center").pack(pady=5)
        text_entry = ttk.Entry(root, width=100)
        text_entry.pack(pady=5)

        # Выпадающий список для выбора формата ключа
        ttk.Label(root, text="Выберите формат ключа:", style="TLabel", anchor="center").pack(pady=5)
        key_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
        key_format.pack(pady=5)
        key_format.current(1)  # По умолчанию "Шестнадцатиричный"

        # Поле для ввода ключа
        ttk.Label(root, text="Введите ключ:", style="TLabel", anchor="center").pack(pady=5)
        key_entry = ttk.Entry(root, width=100)
        key_entry.pack(pady=5)

        # Кнопка для сохранения данных
        ttk.Button(root, text="Сохранить данные", style="TButton", command=lambda: save_data(text_entry, text_format, key_entry, key_format)).pack(pady=10)

        # Кнопка для возврата к рабочему меню
        ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)
        note = ("Текст должен содержать ровно 8 символов, 16 символов в шестнадцатиричном формате, или 64 бита в бинарном формате.\n"
        "Ключ: ровно 7 символов, 14 символов в шестнадцатиричном формате, или 56 бит в бинарном формате.")
        ttk.Label(root, text=note, style="Small.TLabel", anchor="center").pack(side="bottom", pady=20)


    # Функция для обработки шифрованных данных
    def handle_encrypted_data():
        window.destroy()

        current_directory = os.path.dirname(os.path.abspath(__file__))
        encrypted_data_file = os.path.join(current_directory, "project_files", "encrypted_text.txt")
        expanded_key_file = os.path.join(current_directory, "project_files", "expanded_key.txt")

        if not os.path.exists(encrypted_data_file) or not os.path.exists(expanded_key_file):
            messagebox.showerror("Ошибка", "Файлы с зашифрованной информацией или ключом не найдены.")
            return

        # Чтение шифрованной информации и расширенного ключа
        with open(encrypted_data_file, 'r') as file:
            encrypted_data = file.readlines()[1].strip().split(": ")[1]

        with open(expanded_key_file, 'r') as file:
            expanded_key = file.readlines()[1].strip().split(": ")[1]

        # Преобразуем зашифрованные данные во все форматы
        encrypted_text = binary_to_text(encrypted_data)
        encrypted_hex = binary_to_hex(encrypted_data)
        
        key_text = binary_to_text(expanded_key)
        key_hex = binary_to_hex(expanded_key)

        # Отображаем текущие данные в разных форматах перед полями для редактирования
        ttk.Label(root, text="Текущие зашифрованные данные:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный текст: {encrypted_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатеричный: {encrypted_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {encrypted_data}", style="Small.TLabel").pack(pady=5)

        ttk.Label(root, text="Текущий ключ:", style="TLabel").pack(pady=5)
        ttk.Label(root, text=f"Обычный текст: {key_text}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Шестнадцатеричный: {key_hex}", style="Small.TLabel").pack(pady=5)
        ttk.Label(root, text=f"Бинарный: {expanded_key}", style="Small.TLabel").pack(pady=5)


        # Отображение полей для редактирования
        ttk.Label(root, text="Шифрованные данные (для редактирования):", style="TLabel").pack(pady=5)
        encrypted_entry = ttk.Entry(root, width=100)
        encrypted_entry.insert(0, encrypted_data)
        encrypted_entry.pack(pady=5)

        ttk.Label(root, text="Расширенный ключ (для редактирования):", style="TLabel").pack(pady=5)
        key_entry = ttk.Entry(root, width=100)
        key_entry.insert(0, expanded_key)
        key_entry.pack(pady=5)

        # Выпадающий список для формата данных
        ttk.Label(root, text="Выберите формат данных:", style="TLabel").pack(pady=5)
        text_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
        text_format.pack(pady=5)
        text_format.current(0)  # По умолчанию "Бинарный"

        # Выпадающий список для формата ключа
        ttk.Label(root, text="Выберите формат ключа:", style="TLabel").pack(pady=5)
        key_format = ttk.Combobox(root, values=["Бинарный", "Шестнадцатиричный", "Обычный"], state="readonly")
        key_format.pack(pady=5)
        key_format.current(0)  # По умолчанию "Бинарный"

        # Кнопка для сохранения данных
        ttk.Button(root, text="Сохранить", command=lambda: save_encrypted_dataset(encrypted_entry, key_entry, text_format, key_format), style="TButton").pack(pady=10)

        # Кнопка для возврата в рабочее меню
        ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

        note = ("Шифрованный текст должен содержать ровно 8 символов, 16 символов в шестнадцатиричном формате, или 64 бита в бинарном формате.\n"
        "Ключ: ровно 8 символов, 16 символов в шестнадцатиричном формате, или 64 бита в бинарном формате.")
        ttk.Label(root, text=note, style="Small.TLabel", anchor="center").pack(side="bottom", pady=20)
    
        # Кнопки для выбора действий
    ttk.Button(window, text="Обычные", command=lambda: [handle_regular_data(), window.destroy()]).pack(pady=5)
    ttk.Button(window, text="Шифрованные", command=lambda: [handle_encrypted_data(), window.destroy()]).pack(pady=5)


# Функция для сохранения отредактированных зашифрованных данных
def save_encrypted_dataset(encrypted_entry, key_entry, text_format, key_format):
    # Получаем путь к папке проекта
    current_directory = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(current_directory, "project_files")  # Папка project_files
    encrypted_filename = os.path.join(project_files_folder, "encrypted_text.txt")
    key_filename = os.path.join(project_files_folder, "expanded_key.txt")
    
    # Получаем данные из полей ввода
    encrypted_data = encrypted_entry.get()
    expanded_key = key_entry.get()

    # Преобразуем зашифрованные данные и ключ в бинарный формат на основе выбранного формата
    if text_format.get() == "Обычный":
        encrypted_binary = text_to_binary(encrypted_data)
    elif text_format.get() == "Шестнадцатиричный":
        encrypted_binary = hex_to_binary(encrypted_data)
    elif text_format.get() == "Бинарный":
        encrypted_binary = encrypted_data

    if key_format.get() == "Обычный":
        key_binary = text_to_binary(expanded_key)
    elif key_format.get() == "Шестнадцатиричный":
        key_binary = hex_to_binary(expanded_key)
    elif key_format.get() == "Бинарный":
        key_binary = expanded_key

    # Открываем файл и записываем зашифрованный текст в бинарном формате
    with open(encrypted_filename, 'w') as file:
        file.write("Формат: Бинарный\n")
        file.write(f"Данные: {encrypted_binary}\n")
    
    # Открываем файл и записываем расширенный ключ в бинарном формате
    with open(key_filename, 'w') as file:
        file.write("Формат: Бинарный\n")
        file.write(f"Данные: {key_binary}\n")
    
    # Сообщаем об успешном сохранении
    messagebox.showinfo("Результат", f"Зашифрованные данные и ключ сохранены в файлы:\n{encrypted_filename} и {key_filename}")

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
        
        # Проверка ключа
    if key_format_selected == "Бинарный":
        if len(key) != 56:
            messagebox.showerror("Ошибка", "Ключ в бинарном формате должен содержать ровно 64 бита.")
            return
    elif key_format_selected == "Шестнадцатиричный":
        if len(key) != 14:
            messagebox.showerror("Ошибка", "Ключ в шестнадцатиричном формате должен содержать ровно 16 символов.")
            return
    elif key_format_selected == "Обычный":
        if len(key) != 7:
            messagebox.showerror("Ошибка", "Ключ должен содержать ровно 7 символов.")
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
root.geometry("800x700")
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
