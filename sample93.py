import math

# 満タンで何マイル走れるかを計算
def miles_without_stop(fuel_economy, tank_capacity):
    return fuel_economy * tank_capacity

# 速度（マイル/秒）を時速（マイル/時）に変換
def get_distance(velocity):
    return velocity * 3600

# メイン関数：走れる時間（満タンで空になるまで）
def hoursToEmpty(velocity, fuel_economy, tank_capacity):
    # 満タンで走れる距離（マイル）
    full_tank = miles_without_stop(fuel_economy, tank_capacity)

    # 1時間あたりの移動距離（時速に変換）
    distance = get_distance(velocity)

    # 走れる時間 = 走れる距離 ÷ 時速
    hours = full_tank / distance

    # 小数第2位以下を切り捨てて、小数第1位まで返す
    return math.floor(hours * 10) / 10.0
