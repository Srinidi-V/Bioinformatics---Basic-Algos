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
        while i < m:
            n_p += "A"
            i = i + 1
        n_p += new_p
        return n_p
    return new_p

def MedianString(Dna,k):
    Median = ""
    dist = float('inf')
    for i in range(4**k):
        Pattern = NumberToPattern(i,k)
        if dist > DistanceBetweenPatternAndStrings(Pattern, Dna):
            dist = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
            print(Pattern)
    return Median
    
def HammingDistance(p, q):
    n = len (p) #since both are of equal distances
    hamming_distance = 0
    for i in range(0,n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    dist = 0
    k = len(Pattern)
    n = len(Dna[0])
    for text in Dna:
        HammingDist = float('inf')
        kmers = []
        for i in range(n-k+1):
            kmers.append(text[i:i+k])
        for pattern1 in kmers:
            if HammingDist > HammingDistance(Pattern,pattern1):
                HammingDist = HammingDistance(Pattern,pattern1)
        dist += HammingDist
    return dist

dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
"GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
"GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
print(DistanceBetweenPatternAndStrings("GTCAGCG",dna))
