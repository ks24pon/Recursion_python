def decimalToHexadecimal(number):
    if number == 0:
        return "0"

    HEX_DIGITS = "0123456789ABCDEF"
    hex_str = []

    while number > 0:
        number, remainder = divmod(number, 16)
        hex_str.append(HEX_DIGITS[remainder])

    return ''.join(reversed(hex_str))
