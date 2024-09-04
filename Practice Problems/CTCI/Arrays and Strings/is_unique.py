def is_unique(s) :
    for i in range(len(s)) :
        char = s[i]
        if char in s and s.find(char) != i :
            return False
    return True

print(is_unique("jacksparrow"))
