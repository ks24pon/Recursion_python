def numberOfDots(x):
    # 関数を完成させてください
    if x == 1:
        return 1
    return numberOfDots(x-1) + x