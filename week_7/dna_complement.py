def dna_complement(dna,reverse):
    dna = dna.upper()
    complement = ''
    if reverse: 
        dna = list(dna)[::-1]
        dna = ''.join(dna)
        for letter in dna:
            if letter == 'A':
                complement += 'T'
            elif letter == 'T':
                complement += 'A'
            elif letter == 'C':
                complement += 'G'
            elif letter == 'G':
                complement += 'C'
    else:
        for letter in dna:
            if letter == 'A':
                complement += 'T'
            elif letter == 'T':
                complement += 'A'
            elif letter == 'C':
                complement += 'G'
            elif letter == 'G':
                complement += 'C'
    return complement


print(dna_complement('AAAATTTCGGCATAGCGATC', False))
print(dna_complement('AAAATTTCGGCATAGCGATC', True))