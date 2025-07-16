import math

def fallingDistance(planet,time):
    # 関数を完成させてください

    # 惑星名を受け取り重力加速度を返す関数
    def planetGravityMpss(planet):
        if planet == "Earth":
            return 9.8
        if planet == "Jupiter":
            return 24.79
        if planet == "Mercury":
            return 3.7
        return 0

    # メートルを受け取りマイルへ変換
    def metersToMiles(meter):
        return math.floor(meter * 0.000621371 )
    meter = 0.5 * planetGravityMpss(planet) * time ** 2
    return math.floor(metersToMiles(meter))

