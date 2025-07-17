from math import sqrt

def perfectNumberList(n):
    if n < 6:
        return "none"

    result = []

    for i in range(6, n + 1):
        sum_divisors = 1
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                sum_divisors += j
                if j != i // j:
                    sum_divisors += i // j
        if sum_divisors == i:
            result.append(str(i))

    return "-".join(result) if result else "none"
