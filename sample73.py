def hammingDistanceInString(string1,string2):
    # 関数を完成させてください
    count = 0

    # 文字比較
    for i in range(len(string1)):
        # 違う文字だったらカウントする
        if string1[i] != string2[i]:
          count += 1
    return count