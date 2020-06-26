import random
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    Motifs = RandomMotifs(Dna,k,t)
    BestMotifs = Motifs
    j = 0
    while j < N:
        i = random.randint(0,t-1)
        n_Motifs = []
        for k in range(len(BestMotifs)):
            if k!= i:
                n_Motifs.append(BestMotifs[k])
        Profile = ProfileWithPseudocounts(n_Motifs)
        Motifs[i] = ProfileGeneratedString(Dna[i], Profile, k)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        j = j + 1
    return BestMotifs

def RandomMotifs(Dna, k, t):
    r_motifs = []
    r = len(Dna[0])
    for i in range(t):
        x = random.randint(0,r-k)
        r_motifs.append(Dna[i][x:x+k])
    return r_motifs

def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    t = len(Motifs)
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    for i in count.items():
        j = i[1]
        for x in range(len(j)):
            j[x] = j[x] + 1
    return count

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile=CountWithPseudocounts(Motifs)
    for i in "ATCG":
        for j in range(k):
            profile[i][j] = profile[i][j]/ (t + 4)
    return profile

def Normalize(Probabilities):
    sum = 0
    d = {}
    for i in Probabilities.values():
        sum += i
    for k in Probabilities.items():
        d[k] = Probabilities[k] / sum
    return d

def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    x = 0
    for k,v in Probabilities.items():
        if p>=x and p<=v+x:
            kmer = kmer + k
            return kmer
        else:
            x += v

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k],profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def Score(Motifs):
    count = CountWithPseudocounts(Motifs)
    consensus = Consensus(Motifs)
    sum=0
    row=0
    for i in consensus:
        sum1=0
        for j in count:
            if j!= i:
                sum1 += count[j][row]
        sum += sum1
        row +=1
    return sum

def Consensus(Motifs):
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    k = len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
