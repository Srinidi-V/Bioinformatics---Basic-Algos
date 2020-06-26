def Reverse(Pattern):
    newPattern = ""
    for c in Pattern:
        newPattern = c + newPattern
    return newPattern

def Complement(Pattern):
    newPattern = ""
    for c in Pattern:
        if(c=='A'):
            newPattern += 'T'
        elif(c=='T'):
            newPattern += 'A'
        elif(c=='C'):
            newPattern += 'G'
        elif(c=='G'):
            newPattern += 'C'
    return newPattern

def ComplimentDna(Pattern):
    comp = ""
    comp = Complement(Pattern)
    comp = Reverse(comp)
    return comp

def HammingDistance(p, q):
    n = len (p) #since both are of equal distances
    hamming_distance = 0
    for i in range(0,n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    n1 = len(Text)
    n2 = len(Pattern)
    for i in range(0,(n1-n2+1)):
        h_d = HammingDistance(Pattern, Text[i:i+n2])
        if h_d <= d:
            positions.append(i)
    return len(positions)

def FreqWorsWithMismatchAndComp(Text,k,d):
    n = len(Text)
    freq = {}
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        x = ApproximatePatternMatching(Text,pattern,d)
        pattern1 = ComplimentDna(pattern)
        x1 = ApproximatePatternMatching(Text,pattern1,d)
        freq[pattern] = x + x1
    m = max(freq.values())
    final = []
    final1 = []
    for i in freq.items():
        if i[1]==m:
            final.append(i[0])
    for i in final:
        x = ComplimentDna(i)
        final1.append(i)
        final1.append(x)
    final_ = ""
    for i in final1:
        final_ = final_ + str(i)+ " "
    return final_

print(FreqWorsWithMismatchAndComp("GCCAAAAAAAACAACGCCAAAACGTCGCCAACGCCAACAAAAGTCGCCGTCGCCAAAAGCCAAGTGGTCGTCGTGGCCGCCGTGGCCGTCGTCGTGAACGCCAAAAAAAAAAAAGTGGCCGTCAAGTGGTGGTGAACAACGTGGCCGTCAACGTCAACGTGAAGTCGCCAACAAAACGTCGCCAAGTGGTGAAGCCGTGGTCAACGTCAACGTCAA",5,2))