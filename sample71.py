def sheeps(count):
    # 関数を完成させてください
    if count == 0:
        return ""
    return sheeps(count - 1) + f"{count} sheep ~ "