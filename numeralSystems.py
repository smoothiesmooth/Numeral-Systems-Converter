def toInt(num, base='s'):
    out = 0
    if base == 's':
        out = int(num)
    elif base == 2:
        if 'b' in str(num) or 'o' in str(num) or 'x' in str(num):
            num = num[2::]
        num = [int(i) for i in str(num)][::-1]
        for i in range(0, len(num)):
            if num[i] == 1:
                out += 2**i
    elif base == 8:
        if 'b' in str(num) or 'o' in str(num) or 'x' in str(num):
            num = num[2::]
        num = [int(i) for i in str(num)][::-1]
        for i in range(0, len(num)):
            out += num[i] * 8**i
    elif base == 16:
        if '0x' in str(num):
            num = num[2::]
        num = [i for i in str(num)][::-1]
        hex_digit = {'a': 10,  'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
        for i in range(0, len(num)):
            if num[i] in list(hex_digit):
                out += int(hex_digit[num[i]]) * 16**i
            else:
                out += int(num[i]) * 16**i
    return out

def toBin(dec_num):
    out = ''
    while dec_num != 0:
        out = str(dec_num % 2) + out
        dec_num //= 2
    return '0b' + out

def toOct(dec_num):
    out = ''
    while dec_num >= 8:
        remainder = dec_num % 8
        dec_num //= 8
        out += str(remainder)
    out += str(dec_num)
    return '0o' + out[::-1]

def toHex(dec_num):
    hex_digit = {10: 'a',  11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    out = ''
    while dec_num >= 16:
        remainder = dec_num % 16
        dec_num //= 16
        if remainder in list(hex_digit):
            remainder = hex_digit[remainder]
        out += str(remainder)
    if dec_num in list(hex_digit):
        out += str(hex_digit[dec_num])
    else:
        out += str(dec_num)
    return '0x' + out[::-1]

def binToText(bin_code_string):
    input_list = bin_code_string.split(' ')
    output = ''
    for bin in input_list:
        output += chr(toInt(bin, 2))
    return output

def octToText(oct_code_string):
    input_list = oct_code_string.split(' ')
    output = ''
    for oct in input_list:
        output += chr(toInt(oct, 8))
    return output

def hexToText(hex_code_string):
    input_list = hex_code_string.split(' ')
    output = ''
    for hex in input_list:
        output += chr(toInt(hex, 16))
    return output

def textToBin(text):
    list = [i for i in text]
    output = ''
    for l in list:
        output += toBin(ord(l)) + ' '
    return output

def textToOct(text):
    list = [i for i in text]
    output = ''
    for l in list:
        output += toOct(ord(l)) + ' '
    return output

def textToHex(text):
    list = [i for i in text]
    output = ''
    for l in list:
        output += toHex(ord(l)) + ' '
    return output
