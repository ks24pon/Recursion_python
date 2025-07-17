# 1からnまでの総和を計算する関数
def summation(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# 1からnまでの総和の総和を計算する関数
def summationOfSummation(n):
    total = 0
    for i in range(1, n + 1):
        total += summation(i)
    return total
