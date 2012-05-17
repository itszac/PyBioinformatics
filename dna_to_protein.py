##a few functions that can be used for bioinformatics programming

def transcribe_dna(sequence):
    rna=sequence.replace('T', 'U')
    return rna

def translate_sequence(sequence):
    #convert dna to rna
    rna = transcribe_dna(sequence)
    codon_dict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    #cut off extra rna bases
    if len(rna) % 3 == 1:
        rna = rna[0:len(rna)-1]
        print "final base deleted \n"
    elif len(rna) % 3 == 2:
        rna = rna[0:len(rna)-2]
        print "final 2 bases deleted \n"
    else:
        print "No bases deleted \n"
    #split rna into codons
    rna = rna.upper()
    i = range(0,len(rna)/3)
    protein = []
    for x in range(0,len(rna),3):
        codon = rna[x:x+3]
        #look up codon in dictionary
        protein.append(codon_dict[codon])
    return protein

