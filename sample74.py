def fibonacci(n):
    # 関数を完成させてください
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 再帰
    return fibonacci(n - 1) + fibonacci(n - 2)