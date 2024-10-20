import coding
import pandas as pd

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

# Основная функция для анализа лавинного эффекта по ключу
def analyze_avalanche_effect_key(text, key, bit_position):
    # Преобразуем текст и ключ в двоичный формат
    text_binary = coding.text_to_binary(text)
    key_binary = coding.text_to_binary(key)

    # Проверяем длину ключа
    if len(key_binary) != 64:
        raise ValueError("Ключ должен быть длиной 56 бит (7 символов)")

    # Проверяем длину сообщения (должно быть кратно 64 битам)
    check_message_length(text_binary)

    # Разбиваем текст на блоки по 64 бита
    blocks = [text_binary[i:i + 64] for i in range(0, len(text_binary), 64)]

    # Изменяем указанный бит в ключе
    modified_key_binary = flip_bit(key_binary, bit_position)

    # Генерация ключей для обоих ключей
    round_keys_original = coding.generate_keys(key_binary)
    round_keys_modified = coding.generate_keys(modified_key_binary)

    # Таблица для сравнения битов на каждом раунде
    comparison_table = []

    # Шифруем каждый блок по отдельности
    for block_number, block in enumerate(blocks):
        # Выполним начальную перестановку для блока
        original_left, original_right = coding.IP(block)[:32], coding.IP(block)[32:]
        modified_left, modified_right = original_left, original_right

        # Основной процесс раундов для данного блока
        for round_number in range(16):
            # Сохраняем текущее состояние битов перед раундом
            previous_left = original_left
            previous_right = original_right
            modified_previous_left = modified_left
            modified_previous_right = modified_right

            # Выполняем раунд шифрования для оригинального ключа и измененного ключа
            original_left, original_right = coding.round(original_left, original_right, round_keys_original[round_number])
            modified_left, modified_right = coding.round(modified_left, modified_right, round_keys_modified[round_number])

            # Сравниваем биты для каждого раунда
            bit_diff_left = sum(1 for i in range(32) if original_left[i] != modified_left[i])
            bit_diff_right = sum(1 for i in range(32) if original_right[i] != modified_right[i])

            # Если этот раунд уже записан в таблицу, добавляем отличия битов
            if len(comparison_table) > round_number:
                comparison_table[round_number]['Отличия в левой части (блок {}):'.format(block_number + 1)] = bit_diff_left
                comparison_table[round_number]['Отличия в правой части (блок {}):'.format(block_number + 1)] = bit_diff_right
                comparison_table[round_number]['Всего отличий'] += (bit_diff_left + bit_diff_right)
            else:
                # Иначе создаем новую запись для этого раунда
                comparison_table.append({
                    'Раунд': round_number + 1,
                    'Отличия в левой части (блок {}):'.format(block_number + 1): bit_diff_left,
                    'Отличия в правой части (блок {}):'.format(block_number + 1): bit_diff_right,
                    'Всего отличий': bit_diff_left + bit_diff_right
                })

    # Создаем таблицу с результатами
    comparison_df = pd.DataFrame(comparison_table)

    return comparison_df

# Пример использования
text = "EXAMPLEEEXAMPLEE"  # Сообщение длиной 128 бит
key = "KEY12345"         # Исходный ключ длиной 56 бит
bit_position = 10        # Бит, который изменим в ключе (например, 10-й бит)

# Выполняем анализ лавинного эффекта при изменении одного бита в ключе
comparison_table = analyze_avalanche_effect_key(text, key, bit_position)

# Выводим таблицу
print("Сравнение отличий битов на каждом раунде:")
print(comparison_table)
