###
# @Author: Qizhang Jia
# @Date: 2021-02-08 19:24:53
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-02-08 19:24:53
###

from src.readFASTA import readFASTA

seq = readFASTA('Rosalind/stronghold/input_files/rosalind_cons.txt')

n = len(seq[0])

profile = {'A': [0 for _ in range(n)],
           'C': [0 for _ in range(n)],
           'G': [0 for _ in range(n)],
           'T': [0 for _ in range(n)]}

for j in range(len(seq)):
    for k in range(n):
        char = seq[j][k]
        profile[char][k] += 1

consensus = ''

for j in range(n):
    consensus_list = [profile[char][j] for char in ['A', 'C', 'G', 'T']]
    argmax = [i for i, j in enumerate(
        consensus_list) if j == max(consensus_list)]
    if argmax[0] == 0:
        consensus += 'A'
    elif argmax[0] == 1:
        consensus += 'C'
    elif argmax[0] == 2:
        consensus += 'G'
    else:
        consensus += 'T'


print(consensus)
for char in ['A', 'C', 'G', 'T']:
    print(char + ': ' + ' '.join([str(int) for int in profile[char]]))
