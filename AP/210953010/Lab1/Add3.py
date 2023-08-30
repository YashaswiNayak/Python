n = input('Enter a number: ')

if n.startswith("0x") or n.startswith("0X"):
    num = n[2:]
    is_hex = all(char in "0123456789abcdefABCDEF" for char in num)
    if is_hex:
        print('Number is hexadecimal')
    else:
        print('Number is not hexadecimal')
else:
    print('Number is not hexadecimal')
