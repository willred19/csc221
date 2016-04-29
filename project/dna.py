complements   = { 'G' : 'C',
                  'C' : 'G',
                  'T' : 'A',
                  'A' : 'T'}

def to_rna(dna):
    ''' Generate the complementary RNA strand from the given DNA strand

    >>> to_rna("GCTA")
    'CGAT'
    >>> to_rna("gcta")
    'cgat'
    >>> to_rna("gc TA")
    'cg AT'
    '''
    rna = ''
    for c in dna:
        rna = rna + complements[c]
    return rna

