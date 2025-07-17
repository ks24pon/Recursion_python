def isPalindrome(stringInput):
    # スペースを除去して小文字に変換
    cleaned = stringInput.replace(" ", "").lower()

    # 前から読んだものと、後ろから読んだものを比較
    return cleaned == cleaned[::-1]