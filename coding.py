#########################################################################
#   Функции перевода и вычислений (служебные)
#########################################################################
def xor(a,b):
    store = ''
    for i in range(len(a)):
        store += str((int(a[i]) + int(b[i])) % 2)
    return store

def bin_to_int(binary_string):
    length = len(binary_string) - 1
    number = 0
    for bin in range(length + 1):
        number += int(binary_string[bin]) * (2 ** (length - bin))
    return number

def int_to_bin(integer):
    return bin(integer)[2:]

def shifted(bits, shift):
    return bits[shift:] + bits[:shift]

def bin_to_hex(binary, length):
    bin_to_hex = {"0000" : '0',"0001" : '1',"0010" : '2',"0011" : '3',"0100" : '4',"0101" : '5',"0110" : '6',"0111" : '7',
                  "1000" : '8',"1001" : '9',"1010" : 'A',"1011" : 'B',"1100" : 'C',"1101" : 'D',"1110" : 'E',"1111" : 'F'}
    store = ''
    for i in range(0,length,4):
        store += bin_to_hex[str(binary[i:(i+4)])]
    return store
    
def hex_to_binary(binary, length):
    hex_to_bin = {'0' : "0000", '1' : "0001",'2' : "0010",'3' : "0011",'4' : "0100",'5' : "0101",'6' : "0110",'7' : "0111",
                '8' : "1000",'9' : "1001",'A' : "1010",'B' : "1011",'C' : "1100",'D' : "1101",'E' : "1110",'F' : "1111" }
    store = ''
    for i in range(0,length):
        store += hex_to_bin[str(binary[i])]
    return store


#######################################################################################
#   Функции и таблицы перестановок
#######################################################################################
def permute(data, permutation_table, length_of_output):
    permutation = ''
    for i in range(length_of_output):
        permutation += data[permutation_table[i] - 1]
    return permutation

####################################################################
# Фукнции инициальных перестановок и обратная ей
####################################################################
def IP(data):
    initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    return permute(data, initial_perm, 64)
def IP_Inverse(data):
    inverse_perm = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25 ]
    return permute(data, inverse_perm, 64)


########################################################################
#  Функции, являющиеся частью функции фейстеля
########################################################################
def f_expansion(bits):
    # Отвечает за расширение ключа с 32 до 48 бит
    expansion_perm = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
                      16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1 ]
    return permute(bits, expansion_perm, 48)

def f_key_mixing(bits, key):
    # Реализация XOR
    return xor(bits, key)

####################################################################
# Функция s-перестановок   
####################################################################
def s_boxes(bits):
    #Данные функции отвечают за перестановку в S_BOX в раундах, определяя позиции перестановки бита
    sboxes =   [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],       
                [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
                [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
                [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]],
                [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
                [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]],
                [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]],
                [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 ]]]

    substituted_string = ''
    for i in range(0,48,6):
        substring = (bits[0:48][i:i+6])
        row = bin_to_int(substring[0] + substring[5])
        column = bin_to_int(substring[1] + substring[2] + substring[3] + substring[4])
        lookup = int_to_bin(sboxes[int(i/6)][row][column])
        if len(lookup) < 4:
            lookup = ((4 - len(lookup)) * '0') + lookup
        substituted_string += lookup

    return substituted_string
#Финальная перестановка в функции Фейстеля 
def f_permute(bits):
    p_box = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    return permute(bits, p_box, 32)


###################################################################
# Функция Фейстеля
###################################################################
def f(bytes, key):
    expanded = f_expansion(bytes)
    mixed = f_key_mixing(expanded, key)
    substituted = s_boxes(mixed)
    permutation = f_permute(substituted)
    return permutation


##############################################################################################
# Функция раундов
###############################################################################################
def round(left_half, right_half, key):
    new_left_half = xor(left_half, f(right_half, key))
    return (right_half, new_left_half)


#############################################################
# Функция генерации ключей
#############################################################
def generate_keys(intitial_state):

    if len(intitial_state) != 64:
        if len(intitial_state) == 16:
            intitial_state = hex_to_binary(intitial_state, 16)
        else:
            return 'ERROR MESSAGE NOT PROPER SIZE'

    pc_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    pc_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 
            52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]
    permuted = permute(intitial_state, pc_1, 56)
    
    key_schedule = []
    left_half, right_half = permuted[0:28], permuted[28:56]
    for loop in range(16):
        if {0,1,8,15}.__contains__(loop):
            left_half, right_half = shifted(left_half, 1), shifted(right_half, 1)
        else:
            left_half, right_half = shifted(left_half, 2), shifted(right_half, 2)
        key_schedule.append(permute((left_half + right_half), pc_2, 48))
    return key_schedule


####################################################################
# Главная функция шифрования    
####################################################################
def encrypt(message, key):

    ####################################################################
    # Проверка длины сообщения    
    ####################################################################
    if len(message) != 64:
        if len(message) == 16:
            message = hex_to_binary(message, 16)
        else:
            return 'Размер сообщения не совпадает с требуемым'

    key_schedule = generate_keys(key)

    #print('Шифрованная информация (16-ричная система): ', bin_to_hex(message, 64))
    perm = IP(message)
    #print('После инициальной перестановки: ', bin_to_hex(perm, 64))
    left_half, right_half = perm[0:32], perm[32:64]
    
    #print(' ' * 10, 'Левая часть', 'Правая часть', 'Сабключ')
    for loop in range(16):
        left_half, right_half = round(left_half, right_half, key_schedule[loop])
        if loop == 15: 
            buffer = left_half
            left_half = right_half
            right_half = buffer
        #print('Раунд: ', loop + 1, ' ', bin_to_hex(left_half, 32), ' ', bin_to_hex(right_half, 32), ' ', bin_to_hex(key_schedule[loop], 48))
    cyphertext = IP_Inverse(left_half + right_half)
    return cyphertext

####################################################################
# Главная функция дешифровки   
####################################################################
def decrypt(message, key):

    if len(message) != 64:
        if len(message) == 16:
            message = hex_to_binary(message, 16)
        else:
            return 'ERROR MESSAGE NOT PROPER SIZE'

    key_schedule = generate_keys(key)

    print('Информация после шифровки:      ', bin_to_hex(message, 64))
    perm = IP(message)
    print('После инициальной перестановки: ', bin_to_hex(perm, 64))
    left_half, right_half = perm[0:32], perm[32:64]

    #print(' ' * 10, 'Левая часть ', 'Правая часть ', 'Сабключ  ')
    for loop in range(16):
        left_half, right_half = round(left_half, right_half, key_schedule[15 - loop])
        if loop == 15: 
            buffer = left_half
            left_half = right_half
            right_half = buffer
        #print('Раунд: ', loop + 1, ' ', bin_to_hex(left_half, 32), ' ', bin_to_hex(right_half, 32), ' ', bin_to_hex(key_schedule[loop], 48))
    cyphertext = IP_Inverse(left_half + right_half)
    return cyphertext

####################################################################
# Функции инициального расширения ключа
####################################################################

def add_parity_bits(binary_key):
    if len(binary_key) != 56:
        raise ValueError("Ключ должен быть длинной 7 символов/14 в 16ти ричной системе/56 битов")
    
    # Позиции проверочных битов
    parity_positions = [8, 16, 24, 32, 40, 48, 56, 64]
    final_key = ""
    bit_index = 0
    ####################################################################
    #Реализуем функцию добавления бита. Если нечётное - добавляем единицу делая количество единиц чётным
    #Если оно уже четное, то просто добавляем ноль. Таким образом мы расширяем ключ с 56 изначальных битов до 64
    ####################################################################
    for i in range(1, 65):
        if i in parity_positions:
            byte = final_key[-7:]
            ones_count = byte.count('1')
            if ones_count % 2 == 0:
                final_key += '1'
            else:
                final_key += '0'
        else:
            final_key += binary_key[bit_index]
            bit_index += 1
    
    return final_key


####################################################################
# Функции конвертации текста в бинарный формат и обратно
####################################################################
def text_to_binary(text):
    binary_representation = ''.join(format(ord(c), '08b') for c in text)
    return binary_representation

def binary_to_text(binary_data):
    text = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))
    return text

####################################################################
# Тестовый полигон
####################################################################
#test_text = "LALALALA"
#binary_output = text_to_binary(test_text)
#print(binary_output)
#print(binary_to_text(binary_output))

#b = encrypt(binary_output, test2)
#print('Шифрованный результат: ', b)
#decr = decrypt(b, test2)
#print('Расшифрованная информция: ', bin_to_hex(decr, 64))
#print(binary_to_text(decr))
#print(binary_to_text(decrypt(b, test2)))
#for key in generate_keys(binary_output):
#    print(bin_to_hex(key, 48))

#b = encrypt(test1, test2)
#print('Encrypted Result: ', len(b))
#print('Decrypted Result: ', bin_to_hex(decrypt(b, test2), 64))
#for key in generate_keys(test1):
#    print(bin_to_hex(key, 48))

def flip_bit(binary_string, bit_position):
    bit_list = list(binary_string)
    # Меняем выбранный бит (0 на 1, 1 на 0)
    bit_list[bit_position] = '1' if bit_list[bit_position] == '0' else '0'
    return ''.join(bit_list)