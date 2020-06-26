def Symbol(x):
    if x == 0:
        return "A"
    elif x == 1:
        return "C"
    elif x == 2:
        return "G"
    elif x == 3:
        return "T"

def Reverse(p):
    n = len(p)
    new_str = ""
    for i in range(n):
        new_str += p[n-i-1]
    return new_str

def NumberToPattern(index,k):
    p = ""
    while index >=4:
        x = index % 4
        sym = Symbol(x)
        p += sym
        index = int(index / 4)
    p += Symbol(index)
    new_p = Reverse(p)
    if len(new_p) < k:
        m = k - len(new_p)
        n_p=""
        i = 0
        while(i<m):
            n_p += "A"
            i = i + 1
        n_p += new_p
        return n_p
    return new_p

print(NumberToPattern(6337,10))