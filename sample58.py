import math

def planetGravityMpss(planet):
    gravity_dict = {
        "Earth": 9.8,
        "Jupiter": 24.79,
        "Mars": 3.71,
        "Pluto": 0.58,
        "Moon": 1.62
    }
    return gravity_dict.get(planet, 0)

def getVelocity(g, h):
    return math.sqrt(2 * g * h)

def emotionLevel(v):
    if v >= 80:
        return "terrified"
    elif v >= 60:
        return "frighten"
    elif v >= 40:
        return "scared"
    else:
        return "afraid"

def getEmotion(height, planet):
    g = planetGravityMpss(planet)
    if g == 0:
        return "no data"
    v = getVelocity(g, height)
    return emotionLevel(v)
