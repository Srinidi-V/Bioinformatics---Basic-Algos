import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna,k,t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna, k)
        print(M)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
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
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    for i in count.items():
        j = i[1]
        for x in range(len(j)):
            j[x] = j[x] + 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile=CountWithPseudocounts(Motifs)
    for i in "ATCG":
        for j in range(k):
            profile[i][j] = profile[i][j]/ (t + 4)
    return profile

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

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    prob={}
    most_prob_k=[]
    for i in range(n-k+1):
        sub_string = text[i:i+k]
        p = Pr(sub_string,profile)
        prob[sub_string] = p
    max_prob = max(prob.values())
    for key in prob.items():
        if prob[key]==max_prob:
            most_prob_k.append(key)
    return most_prob_k[0]

def ProfileMostProbablePattern(text,k,profile):
    p=-1
    result=text[0:k]
    for i in range(len(text)-k+1):
        seq=text[i:i+k]
        pr=Pr(seq,profile)
        if pr>p:
            p=pr
            result=seq
    return result

def Motifs(Profile, Dna, k):
    motifs = []
    t = len(Dna)
    for i in range(t):
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs

dna=["TGACGTTC","TAAGAGTT","GGACGAAA","CTGTTCGC"]
i=0
y = RandomizedMotifSearch(dna,3,len(dna))
string = ""
for i in y:
    print(i)