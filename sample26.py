def interestsPaid(initialLoan,didPayOnTime):
    # 支払われなかった場合
    percentLate = 1.15
    # 支払われた場合
    percentDefault = 1.02
    # ローンの利子
    serviceFee = 2.5
    # 月々のローン
    total = initialLoan
    # 支払い間に合った場合
    if didPayOnTime:
       total = total * percentDefault
    # 遅れた場合利子
    else:
       total = total * percentLate
    # 合計にプラス請求
    return total + serviceFee

