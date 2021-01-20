# DNA Toolkit file

import collections
Nucleotides = ['A', 'T', 'C', 'G']

# Check the sequence to make sure it is a DNA String.


def validateSeq(dna_seq):
  tmpseq = dna_seq.upper()
   for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# Count the Nucleotide frequency of a DNA String.

def countNucFrequency(dna_seq):
    tmpFreqDict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nuc in dna_seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict


def countNucFrequency_optimized(dna_seq):
    return dict(collections.Counter(seq))
