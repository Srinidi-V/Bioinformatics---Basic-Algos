def HammingDistance(p, q):
    n = len (p) #since both are of equal distances
    hamming_distance = 0
    for i in range(0,n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance

print(HammingDistance("CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA","CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"))