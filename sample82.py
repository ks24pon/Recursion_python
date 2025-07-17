def doYouFail(string):
    # 関数を完成させてください
    # Aの出現回数をカウントするための変数を初期化
    count = 0
    # 文字列の長さ分ループして、1文字ずつチェック
    for i in range(len(string)):
        # 文字列i番目の文字がAの場合、カウントを増やす
        if string[i] == "A":
            count += 1
        # Aが3回以上出現したら、その時点で"fail"を返して終了
        if count >= 3:
            return "fail"
    # 最後までAが3回未満なら"pass"を返す
    return "pass"

