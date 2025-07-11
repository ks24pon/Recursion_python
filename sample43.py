# ライブラリの読み込み
import math

def howMuchIsYourDebt(year):
    # 関数を完成させてください
    interest = 0.2 #　年利 20%
    initialDebt = 10000 # 元金 10000ドル

    # floorで小数点以下を切り捨て
    return math.floor(initialDebt * math.pow((1 + interest),year))