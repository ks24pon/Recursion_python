def countBetweenNumbers(digit,idStart,idEnd):
    # 関数を完成させてください
    count = 0
    digit_str = str(digit)

    for i in range(idStart, idEnd + 1):
        count += str(i).count(digit_str)
    return count