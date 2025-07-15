def isNorthOrSouth(latitude):
    if latitude > 0: return "north"
    if latitude < 0: return "south"
    return "equator"

def isEastOrWest(longitude):
    if longitude > 0: return "east"
    if longitude < 0: return "west"
    return "prime meridian"

def calculateLocation(latitude, longitude):
    latPosition = isNorthOrSouth(latitude)
    longPosition = isEastOrWest(longitude)
    return latPosition + "/" + longPosition