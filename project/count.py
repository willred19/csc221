def rna_count(dna):
    d = {}
    for l in dna:
        d[l] = dna.count(l)
    '''
    >>>rna_count('CC' : 2)
    >>>rna_count('T' : 1)
    >>>rna_count('G' : 1)
    >>>rna_count('AAA' : 3)
    >>>rna_count('uu' : 2)
    '''
    for k in sorted(d):
        print(k + ': ' + str(d[k]))