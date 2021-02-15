###
# @Author: Qizhang Jia
# @Date: 2021-02-09 14:30:36
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-02-09 14:30:36
###

# Mortal Fibonacci Rabbits.

import numpy as np
n = 81
m = 17

fib = np.zeros(n)
maturity = [0] * (m-2) + [1, 1]

fib[0] = 1
fib[1] = 1

index = 2
while index < n:
    fib[index] = fib[index - 1] + fib[index - 2] - maturity.pop(0)
    maturity.append(fib[index - 2])
    index += 1

print(int(fib[-1]))
