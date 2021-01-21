###
# @Author: Qizhang Jia
# @Date: 2021-01-21 11:17:27
# @Last Modified by:   Qizhang Jia
# @Last Modified time: 2021-01-21 11:17:27
###

# Mendel's First Law.
# Mendelian Inheritance.

k = 16
m = 18
n = 21

# all outcomes. (k+m+n)*(k+m+n-1)
# 1. homozygous dominant: k/(k+m+n)
# 2. heterozygous: m/(k+m+n)*(k+.75*(m-1)+.5*n)/(k+m+n-1)
# 3. homozygous recessive: n/(k+m+n)*(k+.5*m)/(k+m+n-1)

probability = k / (k + m + n) + \
    m / (k + m + n) * (k + .75 * (m - 1) + .5 * n) / (k + m + n - 1) + \
    n / (k + m + n) * (k + .5 * m) / (k + m + n - 1)


# probability = (k*k+2*k*m+2*k*n+.75*m*m+.5*m*n -
#                k-.75*m+.5*n)/((k+m+n) * (k+m+n-1))

print(probability)
