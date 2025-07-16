def totalSquareArea(x):
    # 関数を完成させてください
    if x == 1:
        return 1
    return totalSquareArea(x - 1) + x ** 3