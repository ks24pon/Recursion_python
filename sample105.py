def findXTimes(teams):
    from collections import Counter

    # 文字の出現回数をカウント
    count = Counter(teams)

    # 出現回数だけをリストで取得
    values = list(count.values())

    # 全チームが同じ回数だけ試合していれば max == min
    return max(values) == min(values)