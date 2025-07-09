def isSwapBigger(n):
    # 10の位
    tens_place = n // 10
    # 1の位
    one_place = n % 10
    # 値が大きくなるか等しくなるか判定
    return n <= one_place * 10 + tens_place