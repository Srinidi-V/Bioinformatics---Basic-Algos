def HammingDistance(p, q):
    n = len (p) #since both are of equal distances
    hamming_distance = 0
    for i in range(0,n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance

def ApproximatePatternCount(Text, Pattern, d):
    count = 0 # initialize count variable
    positions = [] # initializing list of positions
    n1 = len(Text)
    n2 = len(Pattern)
    for i in range(0,(n1-n2+1)):
        h_d = HammingDistance(Pattern, Text[i:i+n2])
        if h_d <= d:
            positions.append(i)
    count = len(positions)
    return count

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    n1 = len(Text)
    n2 = len(Pattern)
    for i in range(0,(n1-n2+1)):
        h_d = HammingDistance(Pattern, Text[i:i+n2])
        if h_d <= d:
            positions.append(i)
    return positions

def FrequentWordsWithMismatch(Text,k,d):
    n = len(Text)
    freq = {}
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        x = ApproximatePatternMatching(Text,pattern,d)
        freq[pattern] = x
    m = max(freq.values())
    final = ""
    for i in freq.items():
        if i[1]==m:
            final = final + str(i[0])+ " "
    return final

print(ApproximatePatternCount("CGTGACAGTGTATGGGCATCTTT","TGT",1))