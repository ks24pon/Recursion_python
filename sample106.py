def findPairs(numbers):
    from collections import Counter

    # 出現回数をカウント
    count = Counter(numbers)

    # 出現回数がちょうど2回の数字を抽出
    result = [num for num, cnt in count.items() if cnt == 2]

    # 昇順にソートして返す
    return sorted(result)
