def octal_to_binary(oct_num):
    string = ''
    temp = oct_num
    dic = {
        '0' : '000', 
        '1' :'001', 
        '2': '010',
        '3' : '011', 
        '4' : '100', 
        '5' : '101',
        '6' : '110', 
        '7' : '111'
        }
    while temp > 0 :
        digit = int(temp % 10)
        string = string + dic[f'{str(digit)}']
        temp = int(temp / 10)
    return string

def octalToDecimal(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while (temp):
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 8
 
    return dec_value    

def hexadecimal(octnum, dec):
    decnum = dec
    hexadecimal = hex(decnum).replace("0x", "")
    return hexadecimal

oct = int(input(print("Enter the Octal Number: ")))
binary = int(octal_to_binary(oct))
print(f'Binary : {binary}')

decimal = octalToDecimal(oct)
print(f'Decimal : {decimal}')

hexa = hexadecimal(oct,decimal)
print(f'Hexadecimal : {hexa}')
