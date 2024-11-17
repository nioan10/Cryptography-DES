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
import avalanche_key 
import avalanche
import avalanche_all
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import hashlib

##########################################################################################################
# 
# # Главная функция главного меню - сюрприз - сюриприз
#                   
##########################################################################################################
def show_main_menu():
    clear_screen()
    
    ttk.Label(root, text="Главное меню", style="TLabel").pack(pady=60)
    ttk.Button(root, text="Лабораторная 5", command=show_work_menu, style="TButton").pack(pady=10)
    ttk.Button(root, text="Лабораторная 6", command=show_lab6_menu, style="TButton").pack(pady=10)
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
        "Разработка программы: Тузов Алексей [nioan7]\n"
        "Комплектация отчета: [Данные удалены]\n"
        "Помощь: [Данные удалены]\n"
        "Моральная поддержка: Чистякова Полина\n\n"
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
        "Автор программы: Тузов Алексей [nioan7]\n"
        "Версия: 1.001\n"
        "Дата создания: 2024"
    )
    
    show_main_menu()   
    messagebox.showinfo("О программе", about_message)


##########################################################################################################
# 
# # Главное меню
#                   
##########################################################################################################
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

# Получение текста для шифрования
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

# Главная функция шифрования и дешифровки
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

        save_decrypted_data(decrypted_text)


    

        
    # Кнопки для выбора действий
    ttk.Button(window, text="Шифрование", command=lambda: [on_encrypt(), window.destroy()]).pack(pady=5)
    ttk.Button(window, text="Дешифровка", command=lambda: [on_decrypt(), window.destroy()]).pack(pady=5)

# Функция для подгрузки шифрованной информации
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

# Функция для сохранения информации о шифротексте
def save_encrypted_data(encrypted_data):
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")  # Папка project_files
    encrypted_filename = os.path.join(project_files_folder, "encrypted_text.txt")
    
    # Открываем файл и записываем зашифрованный текст
    with open(encrypted_filename, 'w') as file:
        file.write("Формат: Бинарный\n")
        file.write(f"Данные: {encrypted_data}\n")
    messagebox.showinfo("Результат шифрования", f"Шифрованный файл записан в файл {encrypted_filename}")

def save_decrypted_data(decrypted_text):
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")  # Папка project_files
    decrypted_filename = os.path.join(project_files_folder, "decrypted_text.txt")
    
    # Открываем файл и записываем дешифрованный текст
    with open(decrypted_filename, 'w') as file:
        file.write("Формат: Обычный\n")
        file.write(f"Данные: {decrypted_text}\n")
    messagebox.showinfo("Результат шифрования", f"Шифрованный файл записан в файл {decrypted_filename}")

# Функция для сохранения расширенного ключа шифрования
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
    ttk.Label(root, text="Анализ Лавинного Эффекта", style="TLabel").pack(pady=10)

    # Всплывающее окно для выбора типа лавинного эффекта (по ключу или сообщению)
    window = tk.Toplevel(root)
    window.title("Выберите тип анализа лавинного эффекта")

    ttk.Label(window, text="Выберите тип анализа лавинного эффекта", style="TLabel").pack(pady=10)

    def handle_avalanche_key():
        window.destroy()  # Закрываем окно выбора
        show_key_avalanche_analysis()

    def handle_avalanche_message():
        window.destroy()  # Закрываем окно выбора
        show_message_avalanche_analysis()

    def handle_avalanche_key_and_message():
        window.destroy()  # Закрываем окно выбора
        show_key_and_message_avalanche_analysis()

    # Кнопки для выбора
    ttk.Button(window, text="Анализ по ключу", command=handle_avalanche_key).pack(pady=5)
    ttk.Button(window, text="Анализ по сообщению", command=handle_avalanche_message).pack(pady=5)
    ttk.Button(window, text="Анализ по ключу и сообщению", command=handle_avalanche_key_and_message).pack(pady=5)


    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=10)

##########################################################################################################
# # Анализ лавинного эффекта по сообщению
##########################################################################################################

def show_message_avalanche_analysis():
    clear_screen()

    # Поле для ввода текста
    ttk.Label(root, text="Введите текст для анализа (кратно 8 символам):", style="TLabel").pack(pady=5)
    text_entry = ttk.Entry(root, width=100)
    text_entry.pack(pady=5)

    # Поле для ввода ключа
    ttk.Label(root, text="Введите ключ для анализа:", style="TLabel").pack(pady=5)
    key_entry = ttk.Entry(root, width=100)
    key_entry.pack(pady=5)

    # Поле для ввода позиции бита
    ttk.Label(root, text="Введите позицию изменяемого бита в сообщении (0-N):", style="TLabel").pack(pady=5)
    bit_position_entry = ttk.Entry(root, width=10)
    bit_position_entry.pack(pady=5)

    def run_message_avalanche_analysis():
        text = text_entry.get()
        key = key_entry.get()
        bit_position = bit_position_entry.get()

        # Проверки: длина текста и ключа
        if len(text) % 8 != 0:
            messagebox.showerror("Ошибка", "Текст должен быть кратен 8 символам (64 бита).")
            return
        print(key,len(key))
        # Преобразование ключа в хэш
        full_hashed_key = hashlib.sha256(key.encode()).hexdigest()  # Полный хэш в 16-ричном формате
        # Обрезка хэша до первых 7 символов
        key = full_hashed_key[:7]
        if not bit_position.isdigit() or not (0 <= int(bit_position) < len(text) * 8):
            messagebox.showerror("Ошибка", "Позиция изменяемого бита должна быть числом в пределах текста.")
            return

        # Запуск анализа лавинного эффекта по сообщению
        try:
            new_key = text_to_binary(key)
            new_text = text_to_binary(text)
            print(len(new_key))
            new_key = coding.add_parity_bits(new_key)
            print(new_key, len(new_key))
            comparison_table, matr = avalanche.analyze_avalanche_effect_message(new_text, new_key, int(bit_position))
            print("Результат анализа лавинного эффекта по сообщению:\n", comparison_table)
            messagebox.showinfo("Результат", "Анализ лавинного эффекта по сообщению выполнен. Проверьте консоль для деталей.")
            
            # Вычисляем параметры d1 и d3
            d1, d3 = calculate_d1_d3(comparison_table, len(new_text))
            d2 = calculate_d2(matr)
            d4 = calculate_d4(matr)
            ttk.Label(root, text=f"Коэффициенты", style="TLabel").pack(pady=5)
            ttk.Label(root, text=f"Среднее число бит выхода - {d1}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень полноты преобразования - {d2}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень лавинного эффекта - {d3}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень соответствия строгому лавинному критерию - {d4}", style="Small.TLabel").pack(pady=5)
            print(matr)
            
            show_graph(comparison_table)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    # Кнопка для запуска анализа
    ttk.Button(root, text="Запустить анализ", command=run_message_avalanche_analysis).pack(pady=10)
    ttk.Button(root, text="Назад", command=show_avalanche_effect).pack(pady=10)

##########################################################################################################
# # Анализ лавинного эффекта по ключу
##########################################################################################################
def show_key_avalanche_analysis():
    clear_screen()

    # Поле для ввода текста
    ttk.Label(root, text="Введите текст для анализа (кратно 8 символам):", style="TLabel").pack(pady=5)
    text_entry = ttk.Entry(root, width=100)
    text_entry.pack(pady=5)

    # Поле для ввода ключа
    ttk.Label(root, text="Введите ключ для анализа (ровно 7 символов):", style="TLabel").pack(pady=5)
    key_entry = ttk.Entry(root, width=100)
    key_entry.pack(pady=5)

    # Поле для ввода позиции бита
    ttk.Label(root, text="Введите позицию изменяемого бита в ключе (0-63):", style="TLabel").pack(pady=5)
    bit_position_entry = ttk.Entry(root, width=10)
    bit_position_entry.pack(pady=5)

    def run_key_avalanche_analysis():
        text = text_entry.get()
        key = key_entry.get()
        bit_position = bit_position_entry.get()

        # Запуск анализа лавинного эффекта по ключу
        try:
            new_key = text_to_binary(key)
            new_text = text_to_binary(text)
            print(new_key, len(new_key))
            new_key = coding.add_parity_bits(new_key)
            print(new_key, len(new_key))

            comparison_table, matr = avalanche_key.analyze_avalanche_effect_key(new_text, new_key, int(bit_position))
  
            print("Результат анализа лавинного эффекта по ключу:\n", comparison_table)

            messagebox.showinfo("Результат", "Анализ лавинного эффекта по ключу выполнен. Проверьте консоль для деталей.")
            
            # Вычисляем параметры d1 и d3
            d1, d3 = calculate_d1_d3(comparison_table, len(new_text))
            d2 = calculate_d2(matr)
            d4 = calculate_d4(matr)
            ttk.Label(root, text=f"Коэффициенты", style="TLabel").pack(pady=5)
            ttk.Label(root, text=f"Среднее число бит выхода - {d1}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень полноты преобразования - {d2}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень лавинного эффекта - {d3}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень соответствия строгому лавинному критерию - {d4}", style="Small.TLabel").pack(pady=5)
            print(matr)
            
            show_graph(comparison_table)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    # Кнопка для запуска анализа
    ttk.Button(root, text="Запустить анализ", command=run_key_avalanche_analysis).pack(pady=10)
    ttk.Button(root, text="Назад", command=show_avalanche_effect).pack(pady=10)

##########################################################################################################
# # Анализ лавинного эффекта по ключу и сообщению
##########################################################################################################

def show_key_and_message_avalanche_analysis():
    clear_screen()

    # Поле для ввода текста
    ttk.Label(root, text="Введите текст для анализа (кратно 8 символам):", style="TLabel").pack(pady=5)
    text_entry = ttk.Entry(root, width=100)
    text_entry.pack(pady=5)

    # Поле для ввода ключа
    ttk.Label(root, text="Введите ключ для анализа (ровно 7 символов):", style="TLabel").pack(pady=5)
    key_entry = ttk.Entry(root, width=100)
    key_entry.pack(pady=5)

    # Поле для ввода позиции изменяемого бита в сообщении
    ttk.Label(root, text="Введите позицию изменяемого бита в сообщении (0-N):", style="TLabel").pack(pady=5)
    bit_position_message_entry = ttk.Entry(root, width=10)
    bit_position_message_entry.pack(pady=5)

    # Поле для ввода позиции изменяемого бита в ключе
    ttk.Label(root, text="Введите позицию изменяемого бита в ключе (0-63):", style="TLabel").pack(pady=5)
    bit_position_key_entry = ttk.Entry(root, width=10)
    bit_position_key_entry.pack(pady=5)

    def run_key_and_message_avalanche_analysis():
        text = text_entry.get()
        key = key_entry.get()
        bit_position_message = bit_position_message_entry.get()
        bit_position_key = bit_position_key_entry.get()

        # Проверки: длина текста и ключа
        if len(text) % 8 != 0:
            messagebox.showerror("Ошибка", "Текст должен быть кратен 8 символам (64 бита).")
            return
        if len(key) != 7:
            messagebox.showerror("Ошибка", "Ключ должен быть длиной ровно 7 символов (56 бит).")
            return
        if not bit_position_message.isdigit() or not (0 <= int(bit_position_message) < len(text) * 8):
            messagebox.showerror("Ошибка", "Позиция изменяемого бита в сообщении должна быть числом в пределах текста.")
            return
        if not bit_position_key.isdigit() or not (0 <= int(bit_position_key) < 64):
            messagebox.showerror("Ошибка", "Позиция изменяемого бита в ключе должна быть числом от 0 до 63.")
            return

        # Запуск анализа лавинного эффекта по ключу и сообщению
        try:
            new_key = text_to_binary(key)
            new_text = text_to_binary(text)
            new_key = coding.add_parity_bits(new_key)
            comparison_table_message, matr_message, comparison_table_key, matr_key = avalanche_all.analyze_avalanche_effect_key_and_message(new_text, new_key, int(bit_position_message), int(bit_position_key))

            print("Результат анализа лавинного эффекта по сообщению и ключу:\n", comparison_table_message, comparison_table_key)
            messagebox.showinfo("Результат", "Анализ лавинного эффекта выполнен по сообщению и ключу. Проверьте консоль для деталей.")
            
            # Вычисляем параметры d1 и d3 для обоих случаев
            d1_message, d3_message = calculate_d1_d3(comparison_table_message, len(new_text))
            d2_message = calculate_d2(matr_message)
            d4_message = calculate_d4(matr_message)

            d1_key, d3_key = calculate_d1_d3(comparison_table_key, len(new_text))
            d2_key = calculate_d2(matr_key)
            d4_key = calculate_d4(matr_key)

            # Отображаем результаты
            ttk.Label(root, text=f"Коэффициенты для Сообщения:", style="TLabel").pack(pady=5)
            ttk.Label(root, text=f"Среднее число бит выхода - {d1_message}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень полноты преобразования - {d2_message}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень лавинного эффекта - {d3_message}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень соответствия строгому лавинному критерию - {d4_message}", style="Small.TLabel").pack(pady=5)

            ttk.Label(root, text=f"Коэффициенты для Ключа:", style="TLabel").pack(pady=5)
            ttk.Label(root, text=f"Среднее число бит выхода - {d1_key}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень полноты преобразования - {d2_key}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень лавинного эффекта - {d3_key}", style="Small.TLabel").pack(pady=5)
            ttk.Label(root, text=f"Степень соответствия строгому лавинному критерию - {d4_key}", style="Small.TLabel").pack(pady=5)

            show_graph(comparison_table_message)  # График для сообщения
            show_graph(comparison_table_key)      # График для ключа

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    # Кнопка для запуска анализа
    ttk.Button(root, text="Запустить анализ", command=run_key_and_message_avalanche_analysis).pack(pady=10)
    ttk.Button(root, text="Назад", command=show_avalanche_effect).pack(pady=10)

##########################################################################################################
# # Служебные функции
##########################################################################################################
def show_graph(comparison_table):
    # Суммируем отличия по блокам для каждого раунда
    total_diffs = comparison_table.groupby('Раунд')['Всего отличий'].sum()

    # Строим график
    rounds = total_diffs.index  # Раунды (1-16)
    total_diffs_values = total_diffs.values  # Значения отличий для каждого раунда

    plt.figure(figsize=(8, 6))
    plt.plot(rounds, total_diffs_values, marker='o', linestyle='-', color='b')
    plt.title('Лавинный эффект: Изменение количества битов по раундам')
    plt.xlabel('Раунд')
    plt.ylabel('Общее количество измененных битов')
    plt.grid(True)
    plt.show()


def calculate_d1_d3(comparison_table, len_text):
    # Получаем данные из таблицы
    rounds = comparison_table['Раунд']
    total_diffs = comparison_table['Всего отличий']

    # Количество раундов
    n = len(rounds)
    # Количество битов (64 для DES)
    m = len_text
    N = len_text/64
    print(m,N)
    # Вычисление d1 (среднее число изменившихся битов)
    d1 = total_diffs.mean()

    # Вычисление d3 (степень лавинного эффекта)
    total_sum = total_diffs.sum()
    d3 = 1 - abs(total_sum) / (n * m)

    return d1, d3

def calculate_d2(a_ij_matrix):
    n, m = a_ij_matrix.shape
    num_zeros = np.sum(a_ij_matrix == 0)
    d2 = 1 - (num_zeros / (n * m))
    return d2

def calculate_d4(a_ij_matrix):
    n, m = a_ij_matrix.shape
    total_sum = np.sum(a_ij_matrix)
    N = n * m
    d4 = 1 - abs(2 * total_sum - N) / N
    return d4

##########################################################################################################
# # Функции перевода
# #         Раздел со всеми основными функция перевода данных в разные форматы
#               
##########################################################################################################

def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def text_to_hex(text):
    return ''.join(format(ord(c), '02x') for c in text).upper()

def binary_to_text(binary_data):
    return ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

def hex_to_text(hex_string):
    # Убираем возможный префикс "0x", если он присутствует
    hex_string = hex_string.replace("0x", "")
    # Преобразуем шестнадцатиричную строку в байты
    bytes_object = bytes.fromhex(hex_string)
    # Преобразуем байты в строку
    text_string = bytes_object.decode("utf-8")
    return text_string

def binary_to_hex(binary_data):
    return ''.join(format(int(binary_data[i:i+4], 2), 'x') for i in range(0, len(binary_data), 4)).upper()

def hex_to_binary(hex_string):
    # Убираем возможный префикс "0x", если он присутствует
    hex_string = hex_string.replace("0x", "")
    # Переводим шестнадцатиричную строку в целое число, а затем в двоичную строку
    binary_string = bin(int(hex_string, 16))[2:]  # [2:] убирает "0b" префикс
    # Добавляем ведущие нули, чтобы длина строки была кратна 4
    padded_binary_string = binary_string.zfill(len(hex_string) * 4)
    return padded_binary_string

##########################################################################################################
# # Отображение данных
# #         Данные хранятся в соответствующем файле. Раздел содержит дополнительные функции дешифровки
#               данных для отображения информации во всех доступных форматах  
##########################################################################################################

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
            hex_text = binary_to_hex(text_data)
            binary_text = text_data
        elif text_format == "Шестнадцатиричный":
            original_text = hex_to_text(text_data)
            hex_text = text_data
            binary_text = hex_to_binary(text_data)
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

# Общее меню определяющее задание шифрованных данных или обычных
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
    ttk.Button(root, text="Назад", command=show_work_menu, style="TButton").pack(pady=5)

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
        
    # Преобразование ключа в хэш
    full_hashed_key = hashlib.sha256(key.encode()).hexdigest()  # Полный хэш в 16-ричном формате
    # Обрезка хэша до первых 7 символов
    shortened_hashed_key = full_hashed_key[:7]

    # Сохранение данных
    project_folder = os.path.dirname(os.path.abspath(__file__))  # Папка проекта
    project_files_folder = os.path.join(project_folder, "project_files")
    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение текста
        text_filename = os.path.join(project_files_folder, "text_data.txt")
        with open(text_filename, 'w') as file:
            file.write(f"Формат текста: {text_format_selected}\n")
            file.write(f"Данные текста: {text}\n")
        
        # Сохраняем ключ в файл
        key_filename = os.path.join(project_files_folder, "key_data.txt")
        with open(key_filename, 'w') as file:
            file.write(f"Формат ключа: Обычный\n")
            file.write(f"Данные ключа: {shortened_hashed_key}\n")
            messagebox.showinfo("Успех", f"Ключ успешно записан/перезаписан в файл {key_filename}.")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении: {str(e)}")
        return

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
# 
# # 6 практическая
#                   
##########################################################################################################
def show_lab6_menu():
    clear_screen()
    
    ttk.Label(root, text="Лабораторная работа 6", style="TLabel").pack(pady=20)

    # Кнопки для указанных вариантов
    ttk.Button(root, text="Задать данные", command=set_lab6_data, style="TButton").pack(pady=10)
    ttk.Button(root, text="Режим шифрования OFB", command=show_ofb_menu, style="TButton").pack(pady=10)
    ttk.Button(root, text="Кратное шифрование тремя ключами", command=show_triple_key_menu, style="TButton").pack(pady=10)
    
    ttk.Button(root, text="Отобразить данные", command=show_lab6_data, style="TButton").pack(pady=10)
    
    # Кнопка возврата в главное меню
    ttk.Button(root, text="Назад", command=show_main_menu, style="TButton").pack(pady=10)

##########################################################################################################
# 
# # Задача данных
#                   
##########################################################################################################

def set_lab6_data():
    clear_screen()

    # Заголовок окна
    ttk.Label(root, text="Задать данные для Лабораторной 6", style="TLabel").pack(pady=10)

    # Выпадающий список для формата текста
    ttk.Label(root, text="Выберите формат текста:", style="TLabel").pack(pady=5)
    text_format = ttk.Combobox(root, values=["Обычный", "Шестнадцатиричный", "Бинарный"], state="readonly")
    text_format.pack(pady=5)
    text_format.current(0)  # По умолчанию "Обычный"

    # Поле ввода текста
    ttk.Label(root, text="Введите текст:", style="TLabel").pack(pady=5)
    text_entry = ttk.Entry(root, width=100)
    text_entry.pack(pady=5)

    # Поля для трех ключей
    key_entries = []
    key_formats = []
    for i in range(3):
        ttk.Label(root, text=f"Выберите формат ключа {i + 1}:", style="TLabel").pack(pady=5)
        key_format = ttk.Combobox(root, values=["Обычный", "Шестнадцатиричный", "Бинарный"], state="readonly")
        key_format.pack(pady=5)
        key_format.current(0)  # По умолчанию "Обычный"
        key_formats.append(key_format)

        ttk.Label(root, text=f"Введите ключ {i + 1}:", style="TLabel").pack(pady=5)
        key_entry = ttk.Entry(root, width=100)
        key_entry.pack(pady=5)
        key_entries.append(key_entry)

    # Поле ввода вектора инициализации
    ttk.Label(root, text="Выберите формат вектора инициализации:", style="TLabel").pack(pady=5)
    iv_format = ttk.Combobox(root, values=["Обычный", "Шестнадцатиричный", "Бинарный"], state="readonly")
    iv_format.pack(pady=5)
    iv_format.current(0)

    ttk.Label(root, text="Введите вектор инициализации (IV):", style="TLabel").pack(pady=5)
    iv_entry = ttk.Entry(root, width=100)
    iv_entry.pack(pady=5)

    # Кнопка для сохранения данных
    ttk.Button(root, text="Сохранить данные", style="TButton", command=lambda: save_lab6_data_with_keys(text_entry, text_format, key_entries, key_formats, iv_entry, iv_format)).pack(pady=10)

    # Кнопка для возврата к меню Лабораторной 6
    ttk.Button(root, text="Назад", command=show_lab6_menu, style="TButton").pack(pady=10)

    # Примечание для пользователя
    note = (
        "Примечание: Текст должен быть ровно 8 символов, 16 символов в шестнадцатиричном формате или 64 бита в бинарном формате.\n"
        "Каждый ключ может быть задан в любом формате, но будет преобразован в шестнадцатиричный формат и хэширован."
    )
    ttk.Label(root, text=note, style="Small.TLabel", wraplength=700).pack(side="bottom", pady=20)

def save_lab6_data_with_keys(text_entry, text_format, key_entries, key_formats, iv_entry, iv_format):
    text = text_entry.get()
    text_format_selected = text_format.get()
    iv = iv_entry.get()
    iv_format_selected = iv_format.get()

    # Преобразование и дополнение текста
    try:
        padded_text = pad_to_64_bits(text, text_format_selected)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
        return

    # Обработка каждого ключа
    keys_hashed = []
    for i in range(3):
        key = key_entries[i].get()
        key_format_selected = key_formats[i].get()

        # Преобразование ключа в 16-ричный формат
        if key_format_selected == "Обычный":
            key_hex = text_to_hex(key)
        elif key_format_selected == "Бинарный":
            key_hex = binary_to_hex(key)
        elif key_format_selected == "Шестнадцатиричный":
            key_hex = key.upper()
        else:
            messagebox.showerror("Ошибка", f"Неверный формат ключа {i + 1}.")
            return

        # Хэширование ключа (SHA-256) и обрезка до 14 символов
        key_hashed = hashlib.sha256(key_hex.encode()).hexdigest()[:14].upper()
        keys_hashed.append(key_hashed)

        # Преобразование вектора инициализации в 16-ричный формат и обрезка до 16 байт
    if iv_format_selected == "Обычный":
        iv_hex = ''.join(format(ord(c), '02x') for c in iv).upper()
    elif iv_format_selected == "Бинарный":
        iv_hex = ''.join(format(int(iv[j:j+4], 2), 'x') for j in range(0, len(iv), 4)).upper()
    elif iv_format_selected == "Шестнадцатиричный":
        iv_hex = iv.upper()
    else:
        messagebox.showerror("Ошибка", "Неверный формат вектора инициализации.")
        return

    iv_trimmed = iv_hex[:16] 

    # Сохранение данных
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    # Создаем папку для данных, если она не существует
    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение текста
        text_filename = os.path.join(project_files_folder, "lab6_text_data.txt")
        with open(text_filename, 'w') as file:
            file.write(f"Формат текста: Бинарный\n")
            file.write(f"Данные текста: {padded_text}\n")

        # Сохранение ключей
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'w') as file:
            for i, key_hashed in enumerate(keys_hashed, start=1):
                file.write(f"Формат ключа ({i}): Шестнадцатиричный\n")
                file.write(f"Данные ключа ({i}): {key_hashed}\n")
        
        # Сохранение вектора инициализации
        iv_filename = os.path.join(project_files_folder, "lab6_iv_data.txt")
        with open(iv_filename, 'w') as file:
            file.write(f"Формат вектора инициализации: Шестнадцатиричный\n")
            file.write(f"Данные вектора инициализации: {iv_trimmed}\n")

        messagebox.showinfo("Успех", "Данные успешно сохранены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при сохранении данных: {str(e)}")

##########################################################################################################
# 
# # Функция дополнения данных
#                   
##########################################################################################################
def pad_to_64_bits(input_text, text_format):
    """
    Дополняет текст до кратности 64 бит для DES.
    
    :param input_text: Текст в текстовом, шестнадцатиричном или бинарном формате.
    :param text_format: Формат текста ("Обычный", "Шестнадцатиричный", "Бинарный").
    :return: Дополненный текст в бинарном формате.
    """
    # Шаг 1: Преобразование текста в бинарный формат
    if text_format == "Обычный":
        # Преобразуем каждый символ в 8-битный бинарный код
        binary_text = ''.join(format(ord(char), '08b') for char in input_text)
    elif text_format == "Шестнадцатиричный":
        # Преобразуем каждую 16-ричную пару в 8-битный бинарный код
        binary_text = ''.join(format(int(input_text[i:i+2], 16), '08b') for i in range(0, len(input_text), 2))
    elif text_format == "Бинарный":
        # Текст уже в бинарном формате
        binary_text = input_text
    else:
        raise ValueError("Неверный формат текста. Ожидается: 'Обычный', 'Шестнадцатиричный' или 'Бинарный'.")

    # Шаг 2: Рассчитываем недостающий объем для кратности 64
    length = len(binary_text)
    padding_length = 64 - (length % 64) if length % 64 != 0 else 0

    # Шаг 3: Добавляем дополнение
    if padding_length > 0:
        # Дополнение состоит из байтов, равных числу добавленных байтов
        padding_byte = format(padding_length // 8, '08b')  # Значение дополнения в бинарном формате
        padding = padding_byte * (padding_length // 8)    # Генерируем нужное количество байтов дополнения
        binary_text += padding

    return binary_text

##########################################################################################################
# 
# # Функция для режима OFB
#                   
##########################################################################################################
def show_ofb_menu():
    clear_screen()

    # Заголовок меню
    ttk.Label(root, text="Режим шифрования OFB", style="TLabel").pack(pady=10)
    ttk.Button(root, text="Отобразить текущие данные", style="TButton", command=show_lab6_data).pack(pady=10)
    ttk.Button(root, text="Зашифровать", style="TButton", command=perform_ofb_encryption).pack(pady=10)
    ttk.Button(root, text="Расшифровать", style="TButton", command=perform_ofb_decryption).pack(pady=10)
    ttk.Button(root, text="Анализ лавинного эффекта", style="TButton", command=analyze_ofb_avalanche).pack(pady=10)
    ttk.Button(root, text="Назад", style="TButton", command=show_lab6_menu).pack(pady=10)

##########################################################################################################
# 
# # Функция шифровки данных
#                   
##########################################################################################################

def perform_ofb_encryption():
    """
    Выполняет шифрование методом OFB.
    1. Считывает вектор инициализации, ключ и текст из файлов.
    2. Преобразует данные в бинарный вид в зависимости от формата.
    3. Выполняет шифрование методом OFB.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    try:
        # Считывание вектора инициализации
        iv_filename = os.path.join(project_files_folder, "lab6_iv_data.txt")
        with open(iv_filename, 'r') as file:
            iv_lines = file.readlines()
            iv_format = iv_lines[0].strip().split(": ")[1]
            iv_data = iv_lines[1].strip().split(": ")[1]

        # Считывание ключа
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'r') as file:
            key_lines = file.readlines()
            key_format = key_lines[0].strip().split(": ")[1]
            key_data = key_lines[1].strip().split(": ")[1]

        # Считывание текста
        text_filename = os.path.join(project_files_folder, "lab6_text_data.txt")
        with open(text_filename, 'r') as file:
            text_lines = file.readlines()
            text_format = text_lines[0].strip().split(": ")[1]
            text_data = text_lines[1].strip().split(": ")[1]

        # Преобразование данных в бинарный вид
        iv_binary = convert_to_binary(iv_data, iv_format)
        key_binary = convert_to_binary(key_data, key_format)
        text_binary = convert_to_binary(text_data, text_format)

        # Выполнение шифрования
        cipher_text = des_ofb_encryption(text_binary, iv_binary, key_binary)

        # Отображение результата шифрования
        show_encryption_result(cipher_text)

        messagebox.showinfo("Успех", "Шифрование выполнено успешно. Результаты сохранены в файлы.")

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при шифровании: {str(e)}")

def convert_to_binary(data, data_format):
    """
    Преобразует данные в бинарный вид в зависимости от их формата.
    :param data: Исходные данные.
    :param data_format: Формат данных ("Обычный", "Шестнадцатиричный", "Бинарный").
    :return: Данные в бинарном формате.
    """
    if data_format == "Бинарный":
        return data
    elif data_format == "Обычный":
        return ''.join(format(ord(char), '08b') for char in data)
    elif data_format == "Шестнадцатиричный":
        return ''.join(format(int(data[i:i+2], 16), '08b') for i in range(0, len(data), 2))
    else:
        raise ValueError(f"Неизвестный формат данных: {data_format}")

def des_ofb_encryption(binary_text, iv, key):
    """
    Выполняет шифрование текста методом OFB с использованием DES.

    :param binary_text: Текст в бинарном формате (строка из 0 и 1).
    :param iv: Вектор инициализации в бинарном формате (64 бита).
    :param key: Ключ в бинарном формате (56 бит).
    :return: Зашифрованный текст в бинарном формате.
    """
    # Проверка входных данных
    if len(iv) != 64:
        raise ValueError("Вектор инициализации должен быть длиной 64 бита.")
    if len(key) != 56:
        raise ValueError("Ключ должен быть длиной 56 бит.")
    if len(binary_text) % 64 != 0:
        raise ValueError("Текст должен быть кратен 64 битам.")

    # Добавляем биты четности к ключу
    extended_key = coding.add_parity_bits(key)

    # Разделение текста на блоки по 64 бита
    blocks = [binary_text[i:i + 64] for i in range(0, len(binary_text), 64)]

    # Шифрование методом OFB
    cipher_text = ""
    current_iv = iv
    for block in blocks:
        # Генерация псевдослучайного блока (шифрование текущего IV)
        encrypted_iv = coding.encrypt(current_iv, extended_key)

        # Шифрование блока текста (XOR с псевдослучайным блоком)
        encrypted_block = ''.join(
            '1' if bit_text != bit_iv else '0'
            for bit_text, bit_iv in zip(block, encrypted_iv)
        )
        cipher_text += encrypted_block

        # Обновление IV для следующего блока
        current_iv = encrypted_iv

    # Сохранение результата в файл
    save_encrypted_data_OFB(cipher_text, extended_key)

    return cipher_text

def save_encrypted_data_OFB(cipher_text, extended_key):
    """
    Сохраняет зашифрованный текст и расширенный ключ в файл в установленном формате.

    :param cipher_text: Зашифрованный текст в бинарном формате.
    :param extended_key: Расширенный ключ в бинарном формате.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение зашифрованного текста
        cipher_filename = os.path.join(project_files_folder, "lab6_cipher_text.txt")
        with open(cipher_filename, 'w') as file:
            file.write("Формат текста: Бинарный\n")
            file.write(f"Данные текста: {cipher_text}\n")

        # Сохранение расширенного ключа
        key_filename = os.path.join(project_files_folder, "lab6_extended_key.txt")
        with open(key_filename, 'w') as file:
            file.write("Формат ключа: Бинарный\n")
            file.write(f"Данные ключа: {extended_key}\n")

        messagebox.showinfo("Успех", "Результат шифрования успешно сохранен!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

def show_encryption_result(cipher_text):
    """
    Отображает результат шифрования в messagebox.
    :param cipher_text: Зашифрованный текст в бинарном формате.
    """
    # Показываем первые 512 символов, чтобы избежать переполнения окна
    truncated_text = cipher_text[:512] + "..." if len(cipher_text) > 512 else cipher_text
    messagebox.showinfo("Результат шифрования", f"Зашифрованный текст (первые 512 символов):\n{truncated_text}")

##########################################################################################################
# 
# # Функция дешифровки данных
#                   
##########################################################################################################

def perform_ofb_decryption():
    """
    Выполняет дешифровку методом OFB.
    1. Считывает вектор инициализации, ключ и зашифрованный текст из файлов.
    2. Преобразует данные в бинарный вид в зависимости от формата.
    3. Выполняет дешифровку методом OFB.
    4. Отображает результат во всех представлениях (бинарный, обычный, шестнадцатиричный).
    5. Сохраняет результат дешифровки в файл.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    try:
        # Считывание вектора инициализации
        iv_filename = os.path.join(project_files_folder, "lab6_iv_data.txt")
        with open(iv_filename, 'r') as file:
            iv_lines = file.readlines()
            iv_format = iv_lines[0].strip().split(": ")[1]
            iv_data = iv_lines[1].strip().split(": ")[1]

        # Считывание ключа
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'r') as file:
            key_lines = file.readlines()
            key_format = key_lines[0].strip().split(": ")[1]
            key_data = key_lines[1].strip().split(": ")[1]

        # Считывание зашифрованного текста
        cipher_filename = os.path.join(project_files_folder, "lab6_cipher_text.txt")
        with open(cipher_filename, 'r') as file:
            cipher_lines = file.readlines()
            cipher_format = cipher_lines[0].strip().split(": ")[1]
            cipher_data = cipher_lines[1].strip().split(": ")[1]

        # Преобразование данных в бинарный вид
        iv_binary = convert_to_binary(iv_data, iv_format)
        key_binary = convert_to_binary(key_data, key_format)
        cipher_binary = convert_to_binary(cipher_data, cipher_format)

        # Выполнение дешифровки (в OFB дешифровка аналогична шифрованию)
        decrypted_binary = des_ofb_encryption(cipher_binary, iv_binary, key_binary)

        # Убираем padding и преобразуем данные в разные представления
        decrypted_binary_no_padding = remove_padding(decrypted_binary)
        decrypted_text = binary_to_text(decrypted_binary_no_padding)
        decrypted_hex = binary_to_hex(decrypted_binary_no_padding)

        # Сохранение результата в файл
        save_decryption_result(decrypted_binary, decrypted_text, decrypted_hex)

        # Отображение результата в окне
        messagebox.showinfo(
            "Результат дешифровки",
            f"Текст (Бинарный): {decrypted_binary_no_padding}\n\n"
            f"Текст (Обычный): {decrypted_text}\n\n"
            f"Текст (Шестнадцатиричный): {decrypted_hex}"
        )

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при дешифровке: {str(e)}")

def save_decryption_result(binary, text, hex_text):
    """
    Сохраняет результат дешифровки в файл.
    :param binary: Дешифрованный текст в бинарном формате.
    :param text: Дешифрованный текст в обычном формате.
    :param hex_text: Дешифрованный текст в шестнадцатиричном формате.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение результата дешифровки
        decrypted_filename = os.path.join(project_files_folder, "lab6_decrypted_text.txt")
        with open(decrypted_filename, 'w') as file:
            file.write("Формат текста: Обычный\n")
            file.write(f"Данные текста: {text}\n\n")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

##########################################################################################################
# 
# # Функция отображения данных
#                   
##########################################################################################################
def remove_padding(binary_text):
    """
    Удаляет padding из текста в бинарном формате.
    :param binary_text: Текст в бинарном формате (строка из 0 и 1).
    :return: Текст без padding.
    """
    if len(binary_text) % 8 != 0:
        raise ValueError("Длина бинарного текста не кратна 8 битам.")

    # Последний байт определяет количество байтов дополнения
    padding_size = int(binary_text[-8:], 2)
    if padding_size < 1 or padding_size > 8:
        raise ValueError("Неверный padding в тексте.")

    # Убираем padding
    return binary_text[:-padding_size * 8]

def show_lab6_data():
    """
    Отображает данные из файлов, убирает padding для текста и выводит данные во всех представлениях.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    try:
        # Чтение текста
        text_filename = os.path.join(project_files_folder, "lab6_text_data.txt")
        with open(text_filename, 'r') as file:
            lines = file.readlines()
            text_format = lines[0].strip().split(": ")[1]
            binary_text = lines[1].strip().split(": ")[1]

        # Убираем padding из текста
        binary_text_no_padding = remove_padding(binary_text)

        # Преобразуем текст в разные представления
        text = binary_to_text(binary_text_no_padding)
        hex_text = binary_to_hex(binary_text_no_padding)

        # Чтение ключей
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'r') as file:
            keys = file.read()

        # Чтение вектора инициализации
        iv_filename = os.path.join(project_files_folder, "lab6_iv_data.txt")
        with open(iv_filename, 'r') as file:
            iv = file.read()

        # Вывод данных в сообщение
        messagebox.showinfo(
            "Текущие данные",
            f"Текст (Бинарный): {binary_text}\n"
            f"Текст (Без padding): {binary_text_no_padding}\n"
            f"Текст (Обычный): {text}\n"
            f"Текст (Шестнадцатиричный): {hex_text}\n\n"
            f"Ключи (2 и 3 ключи используются только в задании кратного шифрования):\n{keys}\n\n"
            f"Вектор инициализации:\n{iv}"
        )

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при отображении данных: {str(e)}")

##########################################################################################################
# 
# # Анализ лавинного эффекта
#                   
##########################################################################################################

def analyze_ofb_avalanche(): return 0



##########################################################################################################
# 
# # Кратное шифрования с тремя ключами
#                   
##########################################################################################################
def show_triple_key_menu():
    """
    Меню для работы с кратным шифрованием с тремя ключами.
    """
    clear_screen()

    # Заголовок меню
    ttk.Label(root, text="Кратное шифрование с тремя ключами", style="TLabel").pack(pady=10)

    ttk.Button(root, text="Просмотр текущих данных", style="TButton", command=show_lab6_data).pack(pady=10)
    ttk.Button(root, text="Шифрование", style="TButton", command=perform_triple_key_encryption).pack(pady=10)
    ttk.Button(root, text="Дешифровка", style="TButton", command=perform_triple_key_decryption).pack(pady=10)
    ttk.Button(root, text="Анализ лавинного эффекта", style="TButton", command=analyze_triple_key_avalanche).pack(pady=10)
    ttk.Button(root, text="Назад", style="TButton", command=show_lab6_menu).pack(pady=10)

##########################################################################################################
# 
# # Шифрование с тремя ключами
#                   
##########################################################################################################
def perform_triple_key_encryption():
    """
    Выполняет кратное шифрование с тремя ключами.
    1. Считывает данные из файлов.
    2. Преобразует их в бинарный вид.
    3. Выполняет шифрование с помощью трех ключей.
    4. Сохраняет результат шифрования и расширенные ключи в файлы с префиксом 'triple'.
    5. Отображает результат через messagebox.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    try:
        # Считывание ключей
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'r') as file:
            key_lines = file.readlines()

        # Считываем формат и данные для каждого ключа
        keys = []
        for i in range(3):
            key_format = key_lines[i * 2].strip().split(": ")[1]
            key_data = key_lines[i * 2 + 1].strip().split(": ")[1]
            keys.append((key_data, key_format))

        # Считывание текста
        text_filename = os.path.join(project_files_folder, "lab6_text_data.txt")
        with open(text_filename, 'r') as file:
            text_lines = file.readlines()
            if len(text_lines) < 2:
                raise ValueError("Файл текста имеет некорректный формат или недостаточное количество данных (ожидается 2 строки).")
            text_format = text_lines[0].strip().split(": ")[1]
            text_data = text_lines[1].strip().split(": ")[1]

        # Преобразование данных в бинарный вид
        key1_binary = convert_to_binary(keys[0][0], keys[0][1])
        key2_binary = convert_to_binary(keys[1][0], keys[1][1])
        key3_binary = convert_to_binary(keys[2][0], keys[2][1])
        text_binary = convert_to_binary(text_data, text_format)
        # Выполнение шифрования
        cipher_text = triple_key_encryption(text_binary, key1_binary, key2_binary, key3_binary)

        # Добавляем биты четности к каждому ключу
        extended_key1 = coding.add_parity_bits(key1_binary)
        extended_key2 = coding.add_parity_bits(key2_binary)
        extended_key3 = coding.add_parity_bits(key3_binary)

        # Сохранение результата в файлы
        save_triple_encryption_results(cipher_text, extended_key1, extended_key2, extended_key3)

        # Отображение результата
        show_triple_encryption_result(cipher_text)

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при шифровании: {str(e)}")

def save_triple_encryption_results(cipher_text, extended_key1, extended_key2, extended_key3):
    """
    Сохраняет результат шифрования и расширенные ключи в файлы с префиксом 'triple'.
    :param cipher_text: Зашифрованный текст в бинарном формате.
    :param extended_key1: Расширенный ключ 1 в бинарном формате.
    :param extended_key2: Расширенный ключ 2 в бинарном формате.
    :param extended_key3: Расширенный ключ 3 в бинарном формате.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение зашифрованного текста
        cipher_filename = os.path.join(project_files_folder, "triple_cipher_text.txt")
        with open(cipher_filename, 'w') as file:
            file.write("Формат текста: Бинарный\n")
            file.write(f"Данные текста: {cipher_text}\n")

        # Сохранение расширенных ключей
        key_filename = os.path.join(project_files_folder, "triple_extended_keys.txt")
        with open(key_filename, 'w') as file:
            file.write("Формат ключа: Бинарный\n")
            file.write(f"Ключ 1: {extended_key1}\n")
            file.write(f"Ключ 2: {extended_key2}\n")
            file.write(f"Ключ 3: {extended_key3}\n")

        messagebox.showinfo("Успех", "Результаты шифрования успешно сохранены!")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

def save_triple_encryption_results(cipher_text, extended_key1, extended_key2, extended_key3):
    """
    Сохраняет результат шифрования и расширенные ключи в файлы с префиксом 'triple'.
    :param cipher_text: Зашифрованный текст в бинарном формате.
    :param extended_key1: Расширенный ключ 1 в бинарном формате.
    :param extended_key2: Расширенный ключ 2 в бинарном формате.
    :param extended_key3: Расширенный ключ 3 в бинарном формате.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение зашифрованного текста
        cipher_filename = os.path.join(project_files_folder, "triple_cipher_text.txt")
        with open(cipher_filename, 'w') as file:
            file.write("Формат текста: Бинарный\n")
            file.write(f"Данные текста: {cipher_text}\n")

        # Сохранение расширенных ключей
        key_filename = os.path.join(project_files_folder, "triple_extended_keys.txt")
        with open(key_filename, 'w') as file:
            file.write("Формат ключа: Бинарный\n")
            file.write(f"Ключ 1: {extended_key1}\n")
            file.write(f"Ключ 2: {extended_key2}\n")
            file.write(f"Ключ 3: {extended_key3}\n")

        messagebox.showinfo("Успех", "Результаты шифрования успешно сохранены!")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

def show_triple_encryption_result(cipher_text):
    """
    Отображает результат шифрования через messagebox.
    :param cipher_text: Зашифрованный текст в бинарном формате.
    """
    # Показываем первые 512 символов, чтобы избежать переполнения окна
    truncated_text = cipher_text[:512] + "..." if len(cipher_text) > 512 else cipher_text
    messagebox.showinfo("Результат шифрования", f"Зашифрованный текст (первые 512 символов):\n{truncated_text}")

def triple_key_encryption(binary_text, key1, key2, key3):
    """
    Выполняет кратное шифрование с тремя ключами.
    :param binary_text: Текст в бинарном формате (строка из 0 и 1).
    :param key1: Ключ 1 в бинарном формате (56 бит).
    :param key2: Ключ 2 в бинарном формате (56 бит).
    :param key3: Ключ 3 в бинарном формате (56 бит).
    :return: Зашифрованный текст в бинарном формате.
    """
    # Проверка длины ключей
    if len(key1) != 56 or len(key2) != 56 or len(key3) != 56:
        raise ValueError("Каждый ключ должен быть длиной 56 бит.")

    # Добавляем биты четности к каждому ключу
    extended_key1 = coding.add_parity_bits(key1)
    extended_key2 = coding.add_parity_bits(key2)
    extended_key3 = coding.add_parity_bits(key3)

    # Разделение текста на блоки по 64 бита
    blocks = [binary_text[i:i + 64] for i in range(0, len(binary_text), 64)]
    cipher_text = ""

    # Тройное шифрование для каждого блока
    for block in blocks:
        # Первый этап: шифрование с ключом 1
        encrypted_block1 = coding.encrypt(block, extended_key1)
        # Второй этап: шифрование с ключом 2
        encrypted_block2 = coding.encrypt(encrypted_block1, extended_key2)
        # Третий этап: шифрование с ключом 3
        encrypted_block3 = coding.encrypt(encrypted_block2, extended_key3)
        cipher_text += encrypted_block3

    return cipher_text

##########################################################################################################
# 
# # Дешифрование с тремя ключами
#                   
##########################################################################################################

def perform_triple_key_decryption():
    """
    Выполняет кратное дешифрование с тремя ключами.
    1. Считывает данные из файлов.
    2. Преобразует их в бинарный вид.
    3. Выполняет дешифрование.
    4. Удаляет padding.
    5. Сохраняет результат в файл и выводит через messagebox.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    try:
        # Считывание ключей
        key_filename = os.path.join(project_files_folder, "lab6_key_data.txt")
        with open(key_filename, 'r') as file:
            key_lines = file.readlines()

        # Проверяем, чтобы ключи имели ожидаемый формат (6 строк)
        if len(key_lines) < 6:
            raise ValueError("Файл ключей имеет некорректный формат или недостаточное количество данных (ожидается 6 строк).")

        # Считываем формат и данные для каждого ключа
        keys = []
        for i in range(3):
            key_format = key_lines[i * 2].strip().split(": ")[1]
            key_data = key_lines[i * 2 + 1].strip().split(": ")[1]
            keys.append((key_data, key_format))

        # Считывание текста
        cipher_filename = os.path.join(project_files_folder, "triple_cipher_text.txt")
        with open(cipher_filename, 'r') as file:
            cipher_lines = file.readlines()
            if len(cipher_lines) < 2:
                raise ValueError("Файл зашифрованного текста имеет некорректный формат или недостаточное количество данных (ожидается 2 строки).")
            cipher_format = cipher_lines[0].strip().split(": ")[1]
            cipher_data = cipher_lines[1].strip().split(": ")[1]

        # Преобразование данных в бинарный вид
        key1_binary = convert_to_binary(keys[0][0], keys[0][1])
        key2_binary = convert_to_binary(keys[1][0], keys[1][1])
        key3_binary = convert_to_binary(keys[2][0], keys[2][1])
        cipher_binary = convert_to_binary(cipher_data, cipher_format)

        # Выполнение дешифрования
        decrypted_binary = triple_key_decryption(cipher_binary, key1_binary, key2_binary, key3_binary)

        # Удаление padding
        decrypted_binary_no_padding = remove_padding(decrypted_binary)
        decrypted_text = binary_to_text(decrypted_binary_no_padding)
        decrypted_hex = binary_to_hex(decrypted_binary_no_padding)

        # Сохранение результата в файлы
        save_triple_decryption_results(decrypted_binary_no_padding, decrypted_text, decrypted_hex)

        # Отображение результата
        show_triple_decryption_result(decrypted_binary_no_padding, decrypted_text, decrypted_hex)

    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден: {str(e)}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при дешифровании: {str(e)}")

def triple_key_decryption(cipher_text, key1, key2, key3):
    """
    Выполняет кратное дешифрование с тремя ключами.
    :param cipher_text: Зашифрованный текст в бинарном формате (строка из 0 и 1).
    :param key1: Ключ 1 в бинарном формате (56 бит).
    :param key2: Ключ 2 в бинарном формате (56 бит).
    :param key3: Ключ 3 в бинарном формате (56 бит).
    :return: Дешифрованный текст в бинарном формате.
    """
    # Проверка длины ключей
    if len(key1) != 56 or len(key2) != 56 or len(key3) != 56:
        raise ValueError("Каждый ключ должен быть длиной 56 бит.")

    # Добавляем биты четности к каждому ключу
    extended_key1 = coding.add_parity_bits(key1)
    extended_key2 = coding.add_parity_bits(key2)
    extended_key3 = coding.add_parity_bits(key3)

    # Разделение текста на блоки по 64 бита
    blocks = [cipher_text[i:i + 64] for i in range(0, len(cipher_text), 64)]
    plain_text = ""

    # Тройное дешифрование для каждого блока
    for block in blocks:
        # Первый этап: дешифрование с ключом 3
        decrypted_block1 = coding.decrypt(block, extended_key3)
        # Второй этап: дешифрование с ключом 2
        decrypted_block2 = coding.decrypt(decrypted_block1, extended_key2)
        # Третий этап: дешифрование с ключом 1
        decrypted_block3 = coding.decrypt(decrypted_block2, extended_key1)
        plain_text += decrypted_block3

    return plain_text

def save_triple_decryption_results(binary, text, hex_text):
    """
    Сохраняет результат дешифрования в файл.
    :param binary: Дешифрованный текст в бинарном формате.
    :param text: Дешифрованный текст в обычном формате.
    :param hex_text: Дешифрованный текст в шестнадцатиричном формате.
    """
    project_folder = os.path.dirname(os.path.abspath(__file__))
    project_files_folder = os.path.join(project_folder, "lab6_files")

    if not os.path.exists(project_files_folder):
        os.makedirs(project_files_folder)

    try:
        # Сохранение результата дешифрования
        decrypted_filename = os.path.join(project_files_folder, "triple_decrypted_text.txt")
        with open(decrypted_filename, 'w') as file:
            file.write("Формат текста: Бинарный\n")
            file.write(f"Данные текста: {binary}\n\n")
            file.write("Формат текста: Обычный\n")
            file.write(f"Данные текста: {text}\n\n")
            file.write("Формат текста: Шестнадцатиричный\n")
            file.write(f"Данные текста: {hex_text}\n")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении данных: {str(e)}")

def show_triple_decryption_result(binary, text, hex_text):
    """
    Отображает результат дешифрования через messagebox.
    :param binary: Дешифрованный текст в бинарном формате.
    :param text: Дешифрованный текст в обычном формате.
    :param hex_text: Дешифрованный текст в шестнадцатиричном формате.
    """
    messagebox.showinfo(
        "Результат дешифрования",
        f"Текст (Бинарный): {binary}\n\n"
        f"Текст (Обычный): {text}\n\n"
        f"Текст (Шестнадцатиричный): {hex_text}"
    )

##########################################################################################################
# 
# # Анализ лавинного эффекта с тремя ключами
#                   
##########################################################################################################

def analyze_triple_key_avalanche(): return 0

##########################################################################################################
# 
# # Служебные функции и общая инициализация
#                   
##########################################################################################################
# Функция для очистки экрана
def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Основное окно
root = tk.Tk()
root.title("Программа анализа и шифрования по алгоритму DES")
root.geometry("900x800")
root.configure(bg="#ADD8E6")  # Устанавливаем темный фон

# Настройка темной темы с использованием ttk стилей
style = ttk.Style()

# Настройка стилей для кнопок и меток
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#444444", foreground="black")
style.configure("TLabel", font=("Helvetica", 12), background="#ADD8E6", foreground="black")
style.configure("Small.TLabel", font=("Helvetica", 8), background="#ADD8E6", foreground="black")

# Запуск приложения
print(hex_to_text('52455055424C4943'))
show_main_menu()
root.mainloop()
