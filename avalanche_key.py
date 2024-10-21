##########################################################################################################
# 
# # Шаблон комментария раздела
#                   
##########################################################################################################

import coding
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

def split_message_to_blocks(text_binary):
    # Разбиваем текст на блоки по 64 бита
    blocks = [text_binary[i:i + 64] for i in range(0, len(text_binary), 64)]
    return blocks

# Основная функция для анализа лавинного эффекта по ключу
def analyze_avalanche_effect_key(text, key, bit_position):
    # Преобразуем текст и ключ в двоичный формат
    key_binary = key
    text_binary = text
    
    # Проверяем длину ключа
    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 64 бит после расширения")

    # Проверяем кратность сообщения 64 битам
    check_message_length(text_binary)

    # Разбиваем текст на блоки по 64 бита
    blocks = split_message_to_blocks(text_binary)

    # Изменяем указанный бит в ключе
    modified_key_binary = flip_bit(key_binary, bit_position)

    # Генерация ключей для обоих ключей
    round_keys_original = coding.generate_keys(key_binary)
    round_keys_modified = coding.generate_keys(modified_key_binary)

    total_comparison_table = []
    total_a_ij_matrix = np.zeros((16, 64 * len(blocks)), dtype=int)  # Матрица a_{ij} для всех блоков

    for block_num, block in enumerate(blocks):
        # Выполним начальную перестановку для текущего блока текста
        initial_text_perm = coding.IP(block)
        
        # Левые и правые части для блока
        original_left, original_right = initial_text_perm[:32], initial_text_perm[32:]
        modified_left, modified_right = original_left, original_right

        comparison_table = []
        # Основной процесс раундов
        for round_number in range(16):
            # Сохраняем текущее состояние битов перед раундом
            previous_left = original_left
            previous_right = original_right
            modified_previous_left = modified_left
            modified_previous_right = modified_right

            # Выполняем раунд шифрования для оригинального и измененного ключей
            original_left, original_right = coding.round(original_left, original_right, round_keys_original[round_number])
            modified_left, modified_right = coding.round(modified_left, modified_right, round_keys_modified[round_number])

            # Сравниваем биты для каждого раунда и обновляем матрицу a_{ij}
            bit_diff_left = sum(1 for i in range(32) if original_left[i] != modified_left[i])
            bit_diff_right = sum(1 for i in range(32) if original_right[i] != modified_right[i])

            # Заполняем матрицу a_ij для текущего раунда и текущего блока
            for i in range(32):
                total_a_ij_matrix[round_number, i + block_num * 64] = 1 if original_left[i] != modified_left[i] else 0
                total_a_ij_matrix[round_number, i + 32 + block_num * 64] = 1 if original_right[i] != modified_right[i] else 0

            # Записываем результаты сравнения битов для текущего блока
            comparison_table.append({
                'Блок': block_num + 1,
                'Раунд': round_number + 1,
                'Отличия в левой части (биты)': bit_diff_left,
                'Отличия в правой части (биты)': bit_diff_right,
                'Всего отличий': bit_diff_left + bit_diff_right
            })

        # Добавляем отличия для текущего блока в общие результаты
        total_comparison_table.extend(comparison_table)

    # Создаем таблицу с результатами для всех блоков
    total_comparison_df = pd.DataFrame(total_comparison_table)

    return total_comparison_df, total_a_ij_matrix


