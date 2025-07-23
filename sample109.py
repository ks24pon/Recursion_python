def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # key より大きい要素を1つ後ろにずらす
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # 挿入すべき位置に key を入れる
        arr[j + 1] = key
    return arr
