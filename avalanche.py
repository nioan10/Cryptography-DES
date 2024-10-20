import coding
import pandas as pd

# Функция для изменения одного бита в бинарной строке
def flip_bit(binary_string, bit_position):
    bit_list = list(binary_string)
    # Меняем выбранный бит (0 на 1, 1 на 0)
    bit_list[bit_position] = '1' if bit_list[bit_position] == '0' else '0'
    return ''.join(bit_list)

# Функция для проверки, что текст кратен 64 битам
def check_message_length(text_binary):
    if len(text_binary) % 64 != 0:
        raise ValueError("Сообщение должно быть кратно 64 битам (8 символам, 64 бита).")

# Основная функция для анализа
def compare_encrypted_messages(text, key, bit_position):
    # Преобразуем текст и ключ в двоичный формат
    text_binary = coding.text_to_binary(text)
    key_binary = coding.text_to_binary(key)

    # Проверяем, что ключ состоит из 56 бит (7 символов)
    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 56 бит (7 символов)")
    # Проверяем длину сообщения (кратно 64 битам)
    check_message_length(text_binary)

    # Разбиваем текст на блоки по 64 бита
    blocks = [text_binary[i:i + 64] for i in range(0, len(text_binary), 64)]

    # Модифицируем указанный бит в выбранном блоке
    block_index = bit_position // 64  # Узнаем индекс блока, где находится изменяемый бит
    bit_in_block = bit_position % 64  # Узнаем позицию бита в блоке
    modified_blocks = blocks.copy()
    modified_blocks[block_index] = flip_bit(blocks[block_index], bit_in_block)

    # Генерация ключей для обоих сообщений
    round_keys = coding.generate_keys(key_binary)

    # Таблица для сравнения битов на каждом раунде
    comparison_table = []

    # Шифруем каждый блок по отдельности
    for block_number, (original_block, modified_block) in enumerate(zip(blocks, modified_blocks)):
        # Выполним начальную перестановку для обоих блоков
        original_left, original_right = coding.IP(original_block)[:32], coding.IP(original_block)[32:]
        modified_left, modified_right = coding.IP(modified_block)[:32], coding.IP(modified_block)[32:]

        # Основной процесс раундов для данного блока
        for round_number in range(16):
            # Сохраняем текущее состояние битов перед раундом
            previous_left = original_left
            previous_right = original_right
            modified_previous_left = modified_left
            modified_previous_right = modified_right

            # Выполняем раунд шифрования для обоих блоков
            original_left, original_right = coding.round(original_left, original_right, round_keys[round_number])
            modified_left, modified_right = coding.round(modified_left, modified_right, round_keys[round_number])

            # Сравниваем биты для каждого раунда
            bit_diff_left = sum(1 for i in range(32) if original_left[i] != modified_left[i])
            bit_diff_right = sum(1 for i in range(32) if original_right[i] != modified_right[i])

            # Записываем результаты сравнения битов для текущего блока
            comparison_table.append({
                'Блок': block_number + 1,
                'Раунд': round_number + 1,
                'Отличия в левой части (биты)': bit_diff_left,
                'Отличия в правой части (биты)': bit_diff_right,
                'Всего отличий': bit_diff_left + bit_diff_right
            })

    # Создаем таблицу с результатами
    comparison_df = pd.DataFrame(comparison_table)

    return comparison_df

# Пример использования
text = "EXAMPLEEEXAMPLEE"  # Исходный текст (16 символов = 128 бит, кратно 64)
key = "KEY12345"         # Исходный ключ
bit_position = 65        # Бит, который изменим (например, 65-й бит — это 2-й блок, 1-й бит блока)

# Сравниваем шифрованные сообщения
comparison_table = compare_encrypted_messages(text, key, bit_position)

# Выводим таблицу
print("Сравнение отличий битов на каждом раунде:")
print(comparison_table)
