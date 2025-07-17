def notDivisibleNumbers(x,y):
    # 関数を完成させてください
    # x == 1 かつ y == 1 はあまりないので除外
    if x == 1 and y == 1:
        return ""

    # 結果を格納するリストを初期化
    result = []

    # 1からxまでループ
    for num in range(1, x+1):
        # yで割り切れない場合
        if num % y != 0:
            # リストに追加
            result.append(str(num))

    # リストを"-"で連結して1つの文字列にして返す
    return "-".join(result)



