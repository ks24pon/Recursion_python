def simpleSummation(n):
    # 関数を完成させてください
    if n <= 0:
        return 0
    return simpleSummation(n - 1) + n