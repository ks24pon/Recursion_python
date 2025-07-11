def whoIsWinner(hisCard):
    # 負け
    if hisCard == 2 or hisCard == 1:
        return "you lose"
    elif hisCard == 13 or hisCard == 12 or hisCard == 11:
        return "you lose"
    # 引き分け
    elif hisCard == 10:
        return "draw"
    # 勝利
    return "you win"