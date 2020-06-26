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

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    n=len(Genome)
    k=len(Pattern)
    for i in range(n - k + 1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    return positions