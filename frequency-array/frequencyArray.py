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

def ComputingFrequencies(Text,k):
    FreqArr = {}
    for i in range(0, 4**k):
        FreqArr[i] = 0
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FreqArr[j] += 1
    Result = ""
    for item in FreqArr.values():
        Result = Result + " " + str(item)
    return Result

x = ComputingFrequencies("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",8)
print(x)