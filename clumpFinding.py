def FrequentWords(Text, k):
    words = ""
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words += key
    return words

def FrequentWordsTimes(Text, k):
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    return m

def FrequencyMap(Text, k):
    freq={}
    n=len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i+k]
        freq[Pattern]=0
        for i in range(n - k + 1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] += 1
    return freq

def ClumpFind(Genome,k,L,t):
    n = len(Genome)
    final = []
    for i in range(n-L+1):
        Text = Genome[i:i+L]
        x = FrequentWords(Text,k)
        m = FrequentWordsTimes(Text,k)
        if m>=t:
            final.append(x)
    final = set(final)
    result = ""
    for i in final:
        result = result + i + " "
    return result

Genome = "TTCGCTACTCCGCGCCTTGAGAAATCCTAATTAAGTAGTTGGTTCGCGACAATTACGTCCGACCACAACAGGTTGAGCCAGACGACCTACTCAATATTTCACTGAAATCACCAGTACGTGCAGACCGTTTCCCGACTCCCCACCCTCCTAAGGCTCCTCTACCTAAGGCTCTCCCTATAGAGGCGGGATGACCGCTATTCTTCACGTGTGGCTCAGGGCGTCCAAAGTGCTTTCCTTATTGAATTTTTTGGACGCAATAGCTTAATAGCCACAGGTCCGACGGGGCGCTCCGCGAACGTCGCCGCGTTTGCGAAGCTGCCCCTTCCGTGCTATTCTCTGAGTCTCCCCTTTGCCCTCGTTTGCGTAAAACATTTAGATTCCGAACGCTTAAGGTAAATGTTATGTTGATAGGATCGTCAAAATCCTCCAAAGTTAAGCGAAATGACACAAGTTAGAACGCTGGCAGGCTTTATGCTATTCGCGACGCACTCCAGGGAAAACCAAGGTTCCCTCTATCTAGTCTAGTATTTTTTTTCTTCGTCGCTTGAAATCTCTTCCGCTCCTAGCCAGATCAAGAAAGTACCTCCCAGGCGGTGAATTCACCTCAGTATTAAGGTCCGACCGACCACTGCCCTGCTTGAAGAAATTCGTGGACCTAAATCTATTTATCCCAAAACCGCGCGTTTATTCGGGCTAACAGCAGTTTCGAGCGTCGCGCGAGCGTCGCGTCGCGCGTGTTTTCATCTAAATCTAGAGAGTCTAGAGAGATTGCAGACGTACAGACGTCTAAAGACTTTCGGAGTCTTCGGAGAAAGCTGGTCTGATATGCCTTAGCATGAAGGTCTCCACTCCAGTCCTCTCCCTCCAGTCCTCACCTCGGCCACCTCGGCCACCTCGGCCGGCAATGATCAGTCACAACCACGCGATAAGATAGTTCCCTGCACGTGCGTGCGTTCACAACGTTGAGTCCAAGAGCTCAGAGCAGACCAATTGCCCCCAAAGGGACCTGCTTTTGTCAGATCGGCTGTATTACGAATTGTACCGCGGCGGCCCCCATCGGCCCCCATTTTATAGGAGGAGTACAAGTTCGCTGGCGACTCTCTAAATGTGTGATGAGACATCGCGCCTGTGCCAATCCAAGCCTAGCTTAAGCTAGCTTACAAGCTTACAGTTGTTCGAAGTTTTCACAAATGCACAAATGGTGTGTTAGACTATTTATGTAACAGTGTCACTCCCAACTGTTTTCTATATGGAGGTTCCGAAATCCCTATTTATTGCACCGTAGGGTATGTACGTTACTTGTACCCACTACTACGAAGACAAAATCAAACGTACATCACTTTATTGGCGTTTCACGGTCATGACGAATGCGGGCGGCGAACCCAACAAGGCGGCTGCACCATAGACTGGCTTGCTTACTGGCTTGACCTATGGTACACTGTCATCAGTGATATACTGTAGCTTTCGCACACGTGGAGGAGTCCCGCAGTCCCGCACCGCACAAAACGGCCCTCCGAGGCTGATGGCAAGCAGAAGGGCCCGTCGCCCGCCCGTCAAAGAGGCTCAAAGAGGCTAAGAGGCTCTTGATGGACGTCCTGTTAGCGGCGATTGATTCTATAATCACACATCCAGGTCGTAGATAGAACCTCATGAATATTTCTGTAAGCGAGTATTAGCGAGTATTAGCGAGTATTAGCGAGTATTAGCGAGTATTAGCGAGTATTAGCTTTTATATCCGGGATATTATATCCGGGTGGACGTAACTGGACGTAACTGGACGTAACTGGACGTAACTGGACGTAACTGGACGTAACTGGACGTAACTGGACGTAAC"
print(ClumpFind(Genome,10,29,4))