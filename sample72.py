def reverseString(s):
    # 関数を完成させてください
    if s == "":
        return ""
    return  s[len(s)-1] + reverseString(s[:len(s)-1])