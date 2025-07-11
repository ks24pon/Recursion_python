def lastFourHint(stringInput):
    # 関数を完成させてください
    # 6文字未満の時
    if len(stringInput) < 6:
        return "There is no Hint"
    else:
        hint = stringInput[-4:]
        return "Hint is:" + hint