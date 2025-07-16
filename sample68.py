def commonPrefix(s1,s2):
    # 関数を完成させてください
    if s1 == "" or s2 == "" or s1[0] != s2[0]:
        return ""
    return s1[0]+commonPrefix(s1[1:],s2[1:])