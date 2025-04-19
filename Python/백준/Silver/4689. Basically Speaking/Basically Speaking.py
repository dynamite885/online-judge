def convert_base(num, from_base, to_base):
    decimal_num = int(num, from_base)
    if decimal_num == 0:
        return '0'
    digits= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while decimal_num > 0:
        result = digits[decimal_num % to_base] + result
        decimal_num //= to_base
    if len(result) > 7:
        return 'ERROR'
    return result

for i in open(0):
    a,b,c= i.split()
    print("% 7s"%convert_base(a, int(b), int(c)))