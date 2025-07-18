def isFirstStringLarger(s1,s2):
    return asciiSum(s1) > asciiSum(s2)

def asciiSum(string):
    lowerString = string.lower()
    return sum(ord(char) for char in lowerString)