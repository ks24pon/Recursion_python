def getAtLocation(email):
    # 関数を完成させてください
    pos = email.find("@")
    if not pos == -1:
        return pos + 1
    return -1
