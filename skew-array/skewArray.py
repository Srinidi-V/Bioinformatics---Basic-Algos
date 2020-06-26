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
    final = ""
    for i in positions:
        final = final + str(i) + " "
    return final

print(MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))