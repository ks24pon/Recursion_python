def quadraticEquation(a,b,c):
    quadratic_equation = b**2-4*a*c
    if a == 0:
        return 0
    if quadratic_equation == 0:
        return 1
    elif quadratic_equation > 0:
        return 2
    elif quadratic_equation < 0:
        return - 2


