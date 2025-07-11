def deleteAt(s,i):
    if i ==0:
        return s
    elif i > len(s):
        return s
    else:
        front = s[:i-1]
        back = s[i:]
        return front+back