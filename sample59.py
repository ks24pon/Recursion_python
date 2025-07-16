def infectedPeople(day):
    # 関数を完成させてください
    if day == 0:
        return 1
    return infectedPeople(day - 1) * 2