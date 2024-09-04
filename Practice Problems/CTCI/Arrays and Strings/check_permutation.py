def check_permutation(s1:str,s2:str)->bool:
    if len(s1) != len(s2):
        return False
    m1 = {}
    m2 = {}
    for c in s1:
        if c in m1: 
            m1[c] += 1
        else:
            m1[c] = 1

    for c in s2:
        if c in m2: 
            m2[c] += 1
        else:
            m2[c] = 1

    if m1 == m2:
        return True
    return False

print(check_permutation("hello","lehlo"))

def check_permutation2(s1:str,s2:str)->bool:
    if len(s1) != len(s2):
        return False
    chars = [0]*256
    for char in s1:
        val = ord(char)
        if chars[val] :
            chars[val] += 1
        else :
            chars[val] = 1
    for char in s2:
        val = ord(char)
        chars[val] -= 1
        if chars[val] < 0:
            return False
    return True

print(check_permutation2("sdf","sdf"))
