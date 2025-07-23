def selectionSort(arr):
    # 関数を完成させてください
    n = len(arr)
    for i in range(n):
        min_index = i
        # i番目以降の最小値を探す
        for j in range(i + 1, n):
            if arr[j] < arr [min_index]:
                min_index = j
        # 最小値をi番目と交換
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr