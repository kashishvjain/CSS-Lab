import math
import numpy as np
import string
import random

def substitution(plainText):
    shift = int(input('Enter the no. of Position shift: '))

    # Encryption
    encryptedText = ''
    for char in plainText:
        if(char.isupper()):
            encryptedText += chr((ord(char) + shift-65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + shift-97) % 26 + 97)
    print('Encrypted Text:',encryptedText)

    # Decryption
    decryptedText = ''
    for char in encryptedText:
        if(char.isupper()):
            decryptedText += chr((ord(char) - shift-65) % 26 + 65)
        else:
            decryptedText += chr((ord(char) - shift-97) % 26 + 97)
    print('Decrypted Text:',decryptedText)

def rot13(plainText):
    # 13 is the shift

    # Encryption
    encryptedText = ''
    for char in plainText:
        if(char.isupper()):
            encryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('Encrypted Text:',encryptedText)

    # Decryption
    decryptedText = ''
    for char in encryptedText:
        if(char.isupper()):
            decryptedText += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            decryptedText += chr((ord(char) + 13 - 97) % 26 + 97)
    print('Decrypted Text:',decryptedText)

def transpose(plainText):
    key = input('Enter the key: ')
    key.upper()
    order = sorted(list(key))
    col = len(key)
    # Encryption
    msg_len = len(plainText)
    msg_list = list(plainText)
    row = int(math.ceil(msg_len/col))
    null_values = row*col - msg_len
    msg_list.extend('_'*null_values)
    matrix = np.array(msg_list).reshape(row,col)
    encryptedText = ''
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    
    print('Encrypted Text:',encryptedText)
    
    # Decryption
    encryptedText_lst = list(encryptedText)
    decryptedText = ''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        print(index)
        for j in range(row):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    decryptedText = decryptedText[:-decryptedText.count('_')]
    print('Decrypted Text:',decryptedText)

def double_transposition(plainText):
    key1 = input('\nEnter the first key: ')
    key2 = input('Enter the second key: ')
    key1.upper()
    key2.upper()
    order1 = sorted(list(key1))
    order2 = sorted(list(key2))
    col1 = len(key1)
    col2 = len(key2)

    ## Encryption
    msg_len = len(plainText)
    msg_list = list(plainText)
    row1 = int(math.ceil(msg_len/col1))
    null_values1 = row1*col1 - msg_len
    msg_list.extend('_'*null_values1)
    matrix = np.array(msg_list).reshape(row1,col1)
    middleText,encryptedText = '',''

    for i in range(col1):
        index = key1.index(order1[i])
        middleText += ''.join([row1[index] for row1 in matrix])
    print("Single Encryption:",middleText)

    middle_msg_len = len(middleText)
    middle_msg_list = list(middleText)
    row2 = int(math.ceil(middle_msg_len/col2))
    null_values2 = row2*col2 - middle_msg_len
    middle_msg_list.extend('_'*null_values2)
    matrix = np.array(middle_msg_list).reshape(row2,col2)
    
    for i in range(col2):
        index = key2.index(order2[i])
        encryptedText += ''.join([row2[index] for row2 in matrix])
    print('Double Encryption:',encryptedText)

    ## Decryption
    encryptedText_lst = list(encryptedText)
    middleText,decryptedText = '',''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row2,col2)
    for i in range(col2):
        index = key2.index(order2[i])
        for j in range(row2):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1

    middleText = ''.join(''.join(col for col in row) for row in dec_matrix)
    if null_values2 > 0:
        middleText = middleText[:-null_values2]
    pointer = 0
    print('Single Decryption:',middleText)

    middletxt_lst = list(middleText)
    dec_matrix = np.array([None]*len(middleText)).reshape(row1,col1)
    for i in range(col1):
        index = key1.index(order1[i])
        for j in range(row1):
            dec_matrix[j,index] = middletxt_lst[pointer]
            pointer += 1
    if null_values1 > 0:
        decryptedText = decryptedText[:-decryptedText.count('_')]
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    decryptedText = decryptedText[:-decryptedText.count('_')]
    print('Double Decryption:',decryptedText)
    


def vernam_cipher(plainText):
    key = input('Enter the key(of same length as the message):')
    while(len(key)!=len(plainText)):
        print("Please enter the key of the same")
        key = input('Enter the key(of same length as the message):')

    # key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = len(plainText)))
    

    # Encryption   
    encryptedText = ''
    for i in range(len(plainText)):
        encryptedText += chr(((ord(plainText[i])-65)^(ord(key[i])-65))+65)
    print('Encrypted Text:',encryptedText)

    # Decryption
    decryptedText = ''
    for i in range(len(encryptedText)):
        decryptedText += chr(((ord(encryptedText[i]) - 65)^(ord(key[i]) - 65)) + 65)
    print('Decrypted Text:',decryptedText)

def METHOD(i,plainText):
    switcher = {
        1: substitution,
        2: rot13,
        3: transpose,
        4: double_transposition,
        5: vernam_cipher
    }
    switcher[i](plainText)

options = """1. Substitution
2. ROT 13
3. Transpose
4. Double Transposition
5. Vernam Cipher"""
print(options)
choice = int(input("Enter your choice: "))
plainText = input('\nEnter Plain text to be encrypted: ')
METHOD(choice,plainText)