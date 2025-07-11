def insertUnderscoreAt(s,i):
    # 関数を完成させてください
    if i < len(s):
        return s[:i] + "_" + s[i:]
    else:
        return s