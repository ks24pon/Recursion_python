def checkLastDigits(x,y,z):
    xy_last_digit = (x * y) % 10
    z_last_digit = z % 10
    return xy_last_digit == z_last_digit