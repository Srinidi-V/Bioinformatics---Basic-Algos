def SymbolToNumber(s):
    if s=="A":
        return 0
    elif s=="C":
        return 1
    elif s=="G":
        return 2
    elif s=="T":
        return 3
    
def LastSymbol(p):
    n = len(p)
    return p[n-1]

def Prefix(p):
    newstr = ""
    n = len(p)
    newstr = p[:n-1]
    return newstr
    
def PatternToNumber(Pattern):
    if Pattern == "":
        return 0
    symbol = LastSymbol(Pattern)
    prefix = Prefix(Pattern)
    return (4 * PatternToNumber(prefix) + SymbolToNumber(symbol))    

print(PatternToNumber("ATGAGGTGATGAAAC"))