def squareSummation(n):
    # 関数を完成させてください
    if n <= 0:
        return 0
    return squareSummation(n - 1) + n**2