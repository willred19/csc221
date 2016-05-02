

def to_rna(dna):
    return ','.join(complements[nucleotide] for nucleotide in dna)
    '''
    >>>to_rna('C')
    'G'
    >>>to_rna('t')
    'a'
    >>>to_rna('g')
    'c'
    >>>to_rna('T')
    'A'
    >>>to_rna('ccc')
    'ggg'
    >>>to_rna('At Cg'
    'Ua Gc'
    '''

complements   = {'G':'C','C' : 'G',
                  'T' : 'A','A' : 'U',
                  'a' : 'u','c' : 'g',
                  'g' : 'c','t' : 'a'}

