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

print(ComplimentDna("AAAACCCGGT"))