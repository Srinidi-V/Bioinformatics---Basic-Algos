def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + len(Pattern)] == Pattern :
            count = count + 1
    return count
    
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1,n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i] + 1
    return array

def SkewArray(Genome):
    skew_array=[]
    n=len(Genome)
    
    for i in range(0,n+1):
        skew_array.append(0)
  
    for i in range(0,n):
        if Genome[i] == "G":
            skew_array[i+1] = skew_array[i] + 1
        elif Genome[i] == "C":
            skew_array[i+1] = skew_array[i] - 1
        else:
            skew_array[i+1] = skew_array[i]

    return skew_array


def MinimumSkew(Genome):
    positions = [] # output variable
    skew = []
    skew = SkewArray(Genome)
    n = len(Genome)
    min_val = min(skew)
    for i in range(0,n):
        if skew[i] == min_val:
            positions.append(i)
    return positions

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
    return positions