def int_to_ascii(number):
    valid_chars = int_to_ascii.valid_chars
    radix = int_to_ascii.radix
    str = ''
    while number > 0:
        number, remainder = divmod(number, radix)
        str = valid_chars[remainder] + str
    return str or valid_chars[0]
        
int_to_ascii.valid_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-+=._~'
int_to_ascii.radix = len(int_to_ascii.valid_chars)
