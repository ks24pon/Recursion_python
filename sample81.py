def isPrime(number):
    # 関数を完成させてください
    # 1は素数ではないのでFalse
    if number == 1:
        return False
    # 2は最初の素数なのでTrue
    elif number == 2:
        return True
    # 2からnumber1までの数で割り切れるかを調べる
    for i in range(2,number):
        # 割り切れたら素数ではないのでFalse
        if number % i == 0:
            return False
    # どちらでも割り切れなければ素数でTrue
    return True