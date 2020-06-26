def Suffix(Pattern):
    if len(Pattern)==1:
        return ""
    suffix = Pattern[1:]
    return suffix

def HammingDistance(p, q):
    n = len (p) #since both are of equal distances
    hamming_distance = 0
    for i in range(0,n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance

def FirstSymbol(Pattern):
    x = Pattern[0]
    return x

def Neighbours(Pattern,d):
    if d==0:
        return {Pattern}
    if len(Pattern)==1:
        x = ['A','C','T','G']
        return x
    Neighbourhood = set()
    SuffixNeighbours = Neighbours(Suffix(Pattern),d)
    for Text in SuffixNeighbours:
        if HammingDistance(Suffix(Pattern),Text) < d:
            for y in "ATCG":
                string = y + Text
                Neighbourhood.add(string)
        else:
            m = FirstSymbol(Pattern) + Text
            Neighbourhood.add(m)
    return Neighbourhood

x = Neighbours("TGCAT",2)
s = ""
for i in x:
    s = s + i + " "
print(s)
print(len(x))
if "TGCAT" in x:
    print("Yes")