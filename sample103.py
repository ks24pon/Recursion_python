def missingItems(listA, listB):
    # Whalumのリストを集合（set）に変換して高速検索可能にする
    b_set = set(listB)
    # 兄のリストのうち、Whalumが買っていないものだけを返す
    result = [item for item in listA if item not in b_set]
    return result
