def lenString(string):
    return lenStringHelper(string, 0, '')

def lenStringHelper(string, count, res):
    if string == res:
      return count
    return lenStringHelper(string, count+1, res + string[count])