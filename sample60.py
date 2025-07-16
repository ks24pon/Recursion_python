def recursiveAddition(m,n):
    # 関数を完成させてください
    if n >= 0:
        return m + n
    return recursiveAddition(m,n-1) + m

