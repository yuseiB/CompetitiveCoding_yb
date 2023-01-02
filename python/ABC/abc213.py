from scipy.stats import rankdata
import numpy as np
import bisect
import copy


def abc213a():
    a, b = map(int, input().split())
    print(a ^ b)
    return 0


def abc213b():
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    a.sort()
    print(b.index(a[n-2])+1)
    return 0


def abc213c():
    h, w, n = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in np.arange(n):
        a[i], b[i] = map(int, input().split())
    aorder = rankdata(np.array(a), method="dense")
    border = rankdata(np.array(b), method="dense")
    for i in np.arange(n):
        print(f"{int(aorder[i])} {int(border[i])}")
    return 0


if __name__ == '__main__':
    abc213c()
