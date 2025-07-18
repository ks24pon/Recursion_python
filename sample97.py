def countCharactersAfterN(arr):
    # 関数を完成させてください
    count = 0
    for str in arr:
        for chr in str:
            if ord('n') <= ord(chr):
                count += 1
    return count