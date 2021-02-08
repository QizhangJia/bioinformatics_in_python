###
# @Author: Qizhang Jia
# @Date: 2021-01-19 23:53:48
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-19 23:53:48
###

# Complementing a Strand of DNA.

DNA_string = 'TGTATGCCCACGTAATCCGCGCCGTAGATTCAGGTCGTTTGCTGTACTACTGACGGGAGTATCGACGTTCAAGATCTTAGTCCAGTAACGTGGCATCGCGACAAGTGCAGTACATTGACCTTGTTCAAGCAGATTCCGTCTGGAGACCTCATCGTGTAACTTAGTGGGTGTAGTTCCAAGATATGGGGTCTCGTGTTGTAAAACCCCGCCCATCATTGCAAGCAGCCTCATCTAAGCGGTCGTCCGGCAGAAACGCGGTCTTCGGTGGGGACACTCGCTCTAAAGGAGCACTACGATGGCAGCCTCTCTTGCTTGTTACGTAAAGTGCTGCTGACGTCATTCAATCTCCGGCACTACAAGCCATGGCGCTATGCTGAATCCATGACAGTTAGTGCAGAAGGGTACTTTCGATGTTACAAGAGCCTTGTCGGACGTCGGCCATGGTGACTCAACGCCCTCTGAGTGCCCGACTTGCCTTTTCACTCCATCTGCCTTGGCGCTTCGCTCGATATTAAAGATTATAACCTCGCTGTAGGCAGAGGATTCATACAACCTTTTGTGGGGATTTCTCTTTGGTCGTCCACCGGATACGCACCTAGGTAACGGAAAGCAGGGTTGCTAAATCTGCTAGAGAGTCGACTGCACTCTGAACTATGGACAAGCGCGGAAACTAACGAATTGAATGGTAGACCGACCATTACGGTCGTCATAAAGAGTCTGGCTCGCATTATTGAGCCGAGTTAGACTGATCGTCTATCGCTCAGTCAACGAATACACTCACACGGGAGGCAGCATCTCAAATTACTAGTCTCTCGGCTCGTTTCGGCGGCACGAGTCGAAGAGTGGTAGATAAAGCCTATGATTTACCTGAAAGCACGATGTAGTGTAAGACCTATGACCGGCCGGGATCAAGTAAATGTCTTTACGAGTTTCGTTTTTAGACTGACGATGT'
abstract_string = DNA_string.replace('A', '1').replace(
    'T', '2').replace('C', '3').replace('G', '4')
reverse_complement = abstract_string.replace('1', 'T').replace(
    '2', 'A').replace('3', 'G').replace('4', 'C')[::-1]
print(reverse_complement)