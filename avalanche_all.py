import pandas as pd
import numpy as np
import coding

# Функция для изменения одного бита в бинарной строке
def flip_bit(binary_string, bit_position):
    bit_list = list(binary_string)
    # Меняем выбранный бит (0 на 1, 1 на 0)
    bit_list[bit_position] = '1' if bit_list[bit_position] == '0' else '0'
    return ''.join(bit_list)

# Функция для проверки длины ключа (7 символов = 56 бит)
def check_key_length(key_binary):
    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 56 бит (7 символов)")

# Функция для проверки кратности текста 64 битам
def check_message_length(text_binary):
    if len(text_binary) % 64 != 0:
        raise ValueError("Сообщение должно быть кратно 64 битам (8 символам)")

# Основная функция для анализа лавинного эффекта одновременно по ключу и сообщению
def analyze_avalanche_effect_key_and_message(text, key, bit_position_message, bit_position_key):

    text_binary = text
    key_binary = key
    # Проверяем длину ключа и текста
    check_key_length(key_binary)
    check_message_length(text_binary)

    # Изменяем указанный бит в тексте и ключе
    modified_text_binary = flip_bit(text_binary, bit_position_message)
    modified_key_binary = flip_bit(key_binary, bit_position_key)

    # Генерация ключей для обоих случаев
    round_keys_original = coding.generate_keys(key_binary)
    round_keys_modified = coding.generate_keys(modified_key_binary)

    # Выполним начальную перестановку для всех текстов (оригинального и измененного)
    initial_text_perm = coding.IP(text_binary)
    initial_modified_text_perm = coding.IP(modified_text_binary)

    # Левые и правые части для обоих текстов (оригинального и измененного)
    original_left, original_right = initial_text_perm[:32], initial_text_perm[32:]
    modified_left, modified_right = initial_modified_text_perm[:32], initial_modified_text_perm[32:]

    # Инициализация матрицы отслеживания изменений битов
    n = 16  # Количество раундов
    m = 64  # Количество битов (32 бита в левой части + 32 бита в правой части)
    a_ij_matrix_message = np.zeros((n, m), dtype=int)  # Матрица для сообщения
    a_ij_matrix_key = np.zeros((n, m), dtype=int)      # Матрица для ключа

    # Таблицы для сравнения битов на каждом раунде для сообщения и ключа
    comparison_table_message = []
    comparison_table_key = []

    # Основной процесс для каждого раунда
    for round_number in range(n):
        # Сохраняем текущее состояние битов перед раундом
        previous_left = original_left
        previous_right = original_right
        modified_previous_left = modified_left
        modified_previous_right = modified_right

        # Выполняем раунд шифрования для оригинального и измененного сообщения
        original_left, original_right = coding.round(original_left, original_right, round_keys_original[round_number])
        modified_left, modified_right = coding.round(modified_left, modified_right, round_keys_modified[round_number])

        # Сравниваем биты для сообщения и обновляем матрицу a_ij
        bit_diff_left_message = sum(1 for i in range(32) if original_left[i] != modified_left[i])
        bit_diff_right_message = sum(1 for i in range(32) if original_right[i] != modified_right[i])

        for i in range(32):
            a_ij_matrix_message[round_number, i] = 1 if original_left[i] != modified_left[i] else 0
            a_ij_matrix_message[round_number, i + 32] = 1 if original_right[i] != modified_right[i] else 0

        # Записываем результаты сравнения битов для сообщения
        comparison_table_message.append({
            'Раунд': round_number + 1,
            'Отличия в левой части (биты)': bit_diff_left_message,
            'Отличия в правой части (биты)': bit_diff_right_message,
            'Всего отличий': bit_diff_left_message + bit_diff_right_message
        })

        # Выполняем раунд шифрования для оригинального и измененного ключа
        original_left, original_right = coding.round(original_left, original_right, round_keys_original[round_number])
        modified_left, modified_right = coding.round(modified_left, modified_right, round_keys_modified[round_number])

        # Сравниваем биты для ключа и обновляем матрицу a_ij
        bit_diff_left_key = sum(1 for i in range(32) if original_left[i] != modified_left[i])
        bit_diff_right_key = sum(1 for i in range(32) if original_right[i] != modified_right[i])

        for i in range(32):
            a_ij_matrix_key[round_number, i] = 1 if original_left[i] != modified_left[i] else 0
            a_ij_matrix_key[round_number, i + 32] = 1 if original_right[i] != modified_right[i] else 0

        # Записываем результаты сравнения битов для ключа
        comparison_table_key.append({
            'Раунд': round_number + 1,
            'Отличия в левой части (биты)': bit_diff_left_key,
            'Отличия в правой части (биты)': bit_diff_right_key,
            'Всего отличий': bit_diff_left_key + bit_diff_right_key
        })

    # Создаем таблицы с результатами для сообщения и ключа
    comparison_df_message = pd.DataFrame(comparison_table_message)
    comparison_df_key = pd.DataFrame(comparison_table_key)

    return comparison_df_message, a_ij_matrix_message, comparison_df_key, a_ij_matrix_key
