###
# @Author: Qizhang Jia
# @Date: 2021-01-21 11:12:31
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-21 11:12:31
###

# Counting the point mutations.
# Hamming distance

with open('Rosalind/stronghold/input_files/rosalind_hamm.txt', 'r') as f:
    seq_1 = f.readline().strip()
    seq_2 = f.readline().strip()

hamm_distance = 0
for j in range(len(seq_1)):
    if seq_1[j] != seq_2[j]:
        hamm_distance += 1

print(hamm_distance)
