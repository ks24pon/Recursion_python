import math

# 体重の定数（kg）
WEIGHT = 85.5

# 運動ごとのMET値（運動強度）
MET_KEY_VALUE = {
    "running": 8,
    "walking": 3,
    "tennis": 5,
    "rope jump": 9
}

def calcWeightByExercise(exercise, minutes):
    # 運動ごとのMET（強度）を取得
    met = MET_KEY_VALUE[exercise]

    # 1分間に消費するカロリーを計算
    calorie_one_minute = met * 3.5 * WEIGHT / 200

    # 運動時間合計のカロリー消費量を計算
    total_calories = calorie_one_minute * minutes

    # 減少した体重（1kgあたり約7700kcal消費）
    lost_weight = total_calories / 7700

    # 新しい体重を計算
    current_weight = WEIGHT - lost_weight

    # 小数第2位以下を切り捨てて、小数第1位まで残して返す
    return math.floor(current_weight * 10) / 10.0
