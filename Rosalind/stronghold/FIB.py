###
# @Author: Qizhang Jia
# @Date: 2021-01-21 09:51:02
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-21 09:51:02
###

# Rabbits and Recurrence Relations.
def fib(n, k):
    """
    Fibonacci sequence.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return(fib(n-1, k) + k*fib(n-2, k))


n = 32
k = 2
print(fib(n, k))
