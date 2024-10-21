##########################################################################################################
# 
# # Шаблон комментария раздела
#                   
##########################################################################################################

import pandas as pd
import numpy as np
import coding

####################################################################
# Флип указанного бита, если оный 1 меняем на 0, в ином случае на единицу  
####################################################################
def flip_bit(binary_string, bit_position):
    bit_list = list(binary_string)
    # Меняем выбранный бит (0 на 1, 1 на 0)
    bit_list[bit_position] = '1' if bit_list[bit_position] == '0' else '0'
    return ''.join(bit_list)

# Функция для проверки кратности 64 битам
def check_message_length(text_binary):
    if len(text_binary) % 64 != 0:
        raise ValueError("Сообщение должно быть кратно 64 битам (8 символам).")

# Функция для разбиения сообщения на блоки по 64 бита
def split_message_to_blocks(text_binary):
    return [text_binary[i:i + 64] for i in range(0, len(text_binary), 64)]

# Основная функция для анализа лавинного эффекта по сообщению с матрицей отслеживания битов
def analyze_avalanche_effect_message(text, key, bit_position):
    key_binary = key
    text_binary = text

    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 64 битов после расширения.")

    # Проверяем кратность длины текста 64 битам
    check_message_length(text_binary)

    # Разбиваем текст на блоки по 64 бита
    blocks = split_message_to_blocks(text_binary)

    # Изменяем указанный бит в тексте
    modified_text_binary = flip_bit(text_binary, bit_position)

    # Генерация ключей для шифрования
    round_keys = coding.generate_keys(key_binary)

    # Инициализация матрицы отслеживания изменений битов
    total_bits = len(blocks) * 64  # Общее количество битов
    a_ij_matrix = np.zeros((16, total_bits), dtype=int)  # Матрица a_{ij} для всех блоков

    comparison_table = []

    for block_num, block in enumerate(blocks):
        # Выполним начальную перестановку для обоих текстов (оригинального и измененного)
        original_block = block
        modified_block = modified_text_binary[block_num * 64:(block_num + 1) * 64]
        initial_text_perm = coding.IP(original_block)
        initial_modified_perm = coding.IP(modified_block)
        
        # Левые и правые части для обоих текстов
        original_left, original_right = initial_text_perm[:32], initial_text_perm[32:]
        modified_left, modified_right = initial_modified_perm[:32], initial_modified_perm[32:]

        # Основной процесс раундов
        for round_number in range(16):
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

            # Заполняем матрицу a_ij для текущего раунда и текущего блока
            for i in range(32):
                a_ij_matrix[round_number, i + block_num * 64] = 1 if original_left[i] != modified_left[i] else 0
                a_ij_matrix[round_number, i + 32 + block_num * 64] = 1 if original_right[i] != modified_right[i] else 0

            # Записываем результаты сравнения битов
            comparison_table.append({
                'Блок': block_num + 1,
                'Раунд': round_number + 1,
                'Отличия в левой части (биты)': bit_diff_left,
                'Отличия в правой части (биты)': bit_diff_right,
                'Всего отличий': bit_diff_left + bit_diff_right
            })

    # Создаем таблицу с результатами
    comparison_df = pd.DataFrame(comparison_table)

    return comparison_df, a_ij_matrix





