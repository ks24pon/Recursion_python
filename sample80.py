def caesarCipher(message, n):
    result = ""

    for char in message:
        if char == " ":
            continue  # 空白は無視

        shifted = (ord(char) - ord('a') + n) % 26
        result += chr(ord('a') + shifted)

    return result
