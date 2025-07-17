import math
def isPalindromeInteger(n):
    s = str(n)
    length = len(s)
    mid = math.floor(length/2)

    for i in range(mid +1):
        # i番目と反対側が等しいかどうかをチェック
        if s[i] != s[length - 1 - i]:
          return False

    return True