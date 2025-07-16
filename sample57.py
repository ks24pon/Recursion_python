def checkCardType(creditCardType):
    return creditCardType in ["Visa", "MasterCard"]

def askForTip(cost):
    if cost % 3 == 0:
        return cost * 0.03
    elif cost % 5 == 0:
        return cost * 0.05
    elif cost % 7 == 0:
        return cost * 0.07
    else:
        return cost * 0.10

def processPayment(creditCardType, cost):
    # クレジットカードが使用可能か確認
    if not checkCardType(creditCardType):
        return -1.0

    tax = cost * 0.10
    tip = askForTip(cost)
    totalPayment = cost + tax + tip

    # 残高オーバー
    if totalPayment > 300:
        return -1.0

    return round(totalPayment, 2)
