def oneComplement(bits):
    # 結果を格納するリスト（文字列より効率的）
    result = []

    # 各文字を1つずつ確認し、0なら1、1なら0に変換
    for bit in bits:
        if bit == '0':
            result.append('1')
        elif bit == '1':
            result.append('0')

    # リストを文字列に変換して返す
    return ''.join(result)
