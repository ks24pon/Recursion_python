import math
def middleSubstring(stringInput):
    # 文字列の長さ
    length = len(stringInput)

    # 切り取るサイズ
    middle = math.floor(length/2)

    # 切り取りを始める前方の位置
    front = math.ceil(middle/2)

    # 文字列の長さが2以下の時は、最初の文字を返す
    if length <= 2: return stringInput[0]

    # 文字列の長さが2以下の時は、最初の文字を返す
    return stringInput[front:front + middle]
