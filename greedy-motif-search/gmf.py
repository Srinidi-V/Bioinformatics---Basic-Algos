def Count(Motifs):
    count = {} # initializing the count dictionary
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
    return count

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile=Count(Motifs)
    for i in "ATCG":
        for j in range(k):
            profile[i][j] = profile[i][j]/t
    return profile

def Consensus(Motifs):
    count = Count(Motifs)
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
    count = Count(Motifs)
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

def GreedyMotifSearch(Dna,k,t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs