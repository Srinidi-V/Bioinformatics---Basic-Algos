def PatternMatching(Pattern, Genome):
    positions = "" # output variable
    n=len(Genome)
    k=len(Pattern)
    for i in range(n - k + 1):
        if Genome[i:i+k] == Pattern:
            positions = positions + str(i) + " "
    return positions

print(PatternMatching("CGC","ATGACTTCGCTGTTACGCGC"))