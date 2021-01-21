###
# @Author: Qizhang Jia
# @Date: 2021-01-21 10:11:22
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-21 10:11:22
###

# Computing GC Content.
# FASTA format. DNA string labeling.

import numpy as np
with open('Rosalind/stronghold/input_files/rosalind_gc.txt', 'r') as f:
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

gc_content = np.zeros(len(id))
for j in range(len(id)):
    counts = seq[j].count('C') + seq[j].count('G')
    gc_content[j] = counts * 100 / len(seq[j])

print(id[gc_content.argmax()])
print(gc_content[gc_content.argmax()])
