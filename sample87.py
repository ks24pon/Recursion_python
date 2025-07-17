import math

# 素数判定関数
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 素数の総和を求める関数
def sumOfAllPrimes(n):
    return sum(i for i in range(2, n + 1) if isPrime(i))