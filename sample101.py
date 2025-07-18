def charInBagOfWordsCount(bagOfWords,keyCharacter):
    # 関数を完成させてください
    # 初期値
    total = 0

    # ループ処理
    for word in bagOfWords:
        for char in word:
            if char == keyCharacter:
                total += 1
    return total