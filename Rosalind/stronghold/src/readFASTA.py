import numpy as np


def readFASTA(filename):
    """
    Reads the FASTA format and returns a list of DNA strings.
    dtype: filename: str
    rtype: list[str]
    """

    with open(filename, 'r') as f:
        results = f.readlines()

    id = []
    seq = []
    temp_seq = ''

    for j in range(len(results)):
        if results[j][0] == '>':
            seq.append(temp_seq)
            temp_seq = ''
            id.append(results[j][1:].strip())
        else:
            temp_seq += results[j].strip()

    seq.pop(0)
    seq.append(temp_seq)

    return seq
