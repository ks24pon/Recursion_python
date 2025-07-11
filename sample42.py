import math # mathモジュールをインポート

def vacationRental(people, day):
    perDay = 0 # 1日あたりの宿泊費 初期値
    CLEANFEE = 1.12 # 清掃費
    TAX = 1.08 #税金

    if day <= 3: perDay = 80 # 3泊以下のとき
    elif day < 10: perDay = 60 # 4泊以上10泊未満の時
    else: perDay = 50 # それ以外の時
# math モジュールの floor() で小数点以下を切り捨てます
# return 文に式をいれて返します
    return math.floor(perDay * day * people * CLEANFEE * TAX)