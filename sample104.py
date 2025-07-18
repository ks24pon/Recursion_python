def intersectionOfArraysRepeats(intList1, intList2):
    from collections import defaultdict

    count_map = defaultdict(int)
    result = []

    # intList1 の値をカウント
    for num in intList1:
        count_map[num] += 1

    # intList2 で確認し、重複考慮しながら追加
    for num in intList2:
        if count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1

    # 小さい順に並べて返す
    return sorted(result)
