import pandas as pd
import numpy as np
import coding

# Функция для изменения одного бита в бинарной строке
def flip_bit(binary_string, bit_position):
    bit_list = list(binary_string)
    # Меняем выбранный бит (0 на 1, 1 на 0)
    bit_list[bit_position] = '1' if bit_list[bit_position] == '0' else '0'
    return ''.join(bit_list)

# Функция для проверки кратности 64 битам
def check_message_length(text_binary):
    if len(text_binary) % 64 != 0:
        raise ValueError("Сообщение должно быть кратно 64 битам (8 символам).")

# Основная функция для анализа лавинного эффекта по сообщению с матрицей отслеживания битов
def analyze_avalanche_effect_message(text, key, bit_position):
    key_binary = key
    text_binary = text

    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 64 битов после расширения.")

    # Проверяем кратность длины текста 64 битам
    check_message_length(text_binary)

    # Изменяем указанный бит в тексте
    modified_text_binary = flip_bit(text_binary, bit_position)

    # Генерация ключей для шифрования
    round_keys = coding.generate_keys(key_binary)

    # Выполним начальную перестановку для обоих текстов (оригинального и измененного)
    initial_text_perm = coding.IP(text_binary)
    initial_modified_perm = coding.IP(modified_text_binary)
    
    # Левые и правые части для обоих текстов
    original_left, original_right = initial_text_perm[:32], initial_text_perm[32:]
    modified_left, modified_right = initial_modified_perm[:32], initial_modified_perm[32:]

    # Инициализация матрицы отслеживания изменений битов
    n = 16  # Количество раундов
    m = 64  # Количество битов (32 бита в левой части + 32 бита в правой части)
    a_ij_matrix = np.zeros((n, m), dtype=int)  # Матрица a_{ij}, изначально заполнена нулями

    # Таблица для сравнения битов на каждом раунде
    comparison_table = []

    # Основной процесс раундов
    for round_number in range(n):
        # Сохраняем текущее состояние битов перед раундом
        previous_left = original_left
        previous_right = original_right
        modified_previous_left = modified_left
        modified_previous_right = modified_right

        # Выполняем раунд шифрования для обоих сообщений
        original_left, original_right = coding.round(original_left, original_right, round_keys[round_number])
        modified_left, modified_right = coding.round(modified_left, modified_right, round_keys[round_number])

        # Сравниваем биты для каждого раунда и обновляем матрицу a_{ij}
        bit_diff_left = sum(1 for i in range(32) if original_left[i] != modified_left[i])
        bit_diff_right = sum(1 for i in range(32) if original_right[i] != modified_right[i])

        # Заполняем матрицу a_ij для текущего раунда
        for i in range(32):
            a_ij_matrix[round_number, i] = 1 if original_left[i] != modified_left[i] else 0
            a_ij_matrix[round_number, i + 32] = 1 if original_right[i] != modified_right[i] else 0

        # Записываем результаты сравнения битов
        comparison_table.append({
            'Раунд': round_number + 1,
            'Отличия в левой части (биты)': bit_diff_left,
            'Отличия в правой части (биты)': bit_diff_right,
            'Всего отличий': bit_diff_left + bit_diff_right
        })

    # Создаем таблицу с результатами
    comparison_df = pd.DataFrame(comparison_table)

    return comparison_df, a_ij_matrix




