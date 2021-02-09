###
# @Author: Qizhang Jia
# @Date: 2021-02-08 19:09:47
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-02-08 19:09:47
###

with open('Rosalind/stronghold/input_files/rosalind_subs.txt', 'r') as f:
    s = f.readline()
    t = f.readline()

locations = ''
for j in range(len(s) - len(t)):
    if s[j:j + len(t)] == t:
        locations += str(j+1) + ' '

print(locations)
