from scipy.stats import rankdata
import numpy as np
import bisect
import copy


def abc214a():
    n = int(input())
    if n <= 125:
        ret = 4
    elif n <= 211:
        ret = 6
    elif n <= 214:
        ret = 8
    else:
        ret = -1
    print(ret)
    return 0


def abc214b():
    s, t = map(int, input().split())
    cnt = 0
    for a in np.arange(0, s+1):
        for b in np.arange(0, s-a+1):
            c1 = s-a-b
            if a*b == 0:
                c2 = 1e4+1
            else:
                c2 = int(t/a/b)
            # print(f"{a},{b},{c1},{c2},{min(c1, c2)+1}")
            cnt += min(c1, c2)+1
    print(cnt)
    return 0


if __name__ == '__main__':
    abc214b()
