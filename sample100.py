def addEveryOtherElement(intArr):
    # 関数を完成させてください
    totalArr = 0

    # 1つ飛ばしで数字わ足していく
    for i in intArr[::2]:
        totalArr += i

    return totalArr