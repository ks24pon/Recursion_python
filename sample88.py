def decimalToBinary(decNumber):
    # ベースケース：0 のときは "0" を返す
    if decNumber == 0:
        return "0"

    binary = ""

    # dec_number が 0 になるまで 2 で割りながら余りを先頭に追加
    while decNumber > 0:
        remainder = decNumber % 2
        binary = str(remainder) + binary
        decNumber = decNumber // 2

    return binary
