###
# @Author: Qizhang Jia
# @Date: 2021-01-19 22:16:53
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-19 22:16:53
###

# 1. Installing Python
# import this

# 2. Variables and Some Arithmetic
# a = 902
# b = 872
# print(a ** 2 + b ** 2)

# 3. Strings and Lists
# string = 'djDPbdOneGwOscClqRlWiTHimantopusEwsXPmYIKzeT28USotCgBZeGyoVUQaZx8TPI2jUuE7cnIa4otIytwrZDYniEembCRLDk6DlSgvizo3nGbHdUegYttROa3rD4GCC3l8KC3Jstylifer9uJ5naeTLulga5e2a6tpg8xqZv'
# a = 22
# b = 31
# c = 138
# d = 145
#
# print('{} {}'.format(string[a:b+1], string[c:d+1]))

# 4. Conditions and Loops
# a = 4620
# b = 9295
# sum = 0
# for i in range(a, b + 1):
#     if (i % 2 != 0):
#         sum += i
# print(sum)

# 5. Working with Files.
# result = []
# input_filename = 'Rosalind/village/text.txt'
# output_filename = 'Rosalind/village/output.txt'
#
# with open(input_filename, 'r') as input_f:
#     result = input_f.readlines()
#
# with open(output_filename, 'w') as output_f:
#     for j in range(len(result)):
#         if (j % 2 == 1):
#             output_f.write(result[j])


# 6. Dictionaries
string = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
words = string.split(' ')
frequency = {}

for i in range(len(words)):
    if words[i] in frequency:
        frequency[words[i]] += 1
    else:
        frequency[words[i]] = 1

for key, value in frequency.items():
    print(key, value)
