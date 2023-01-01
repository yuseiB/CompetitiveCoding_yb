import numpy as np
import bisect
import copy

def cin():
    a = int(input())
    print(a*2)
    
def abc212a():
    a,b = map(int, input().split())
    if 0<a and b==0:
        ret = "Gold"
    elif a==0 and 0<b:
        ret = "Silver"
    elif 0<a and 0<b:
        ret = "Alloy"
    else:
        return -1
    print(ret)
    return ret

def abc212b():
    d = int(input())
    flgsame = True if d%1111==0 else False
    d0 = copy.deepcopy(d)
    n = 4 
    dd=np.zeros(n)
    for i in np.arange(n):
        dd[i]=int(d/pow(10,n-i-1))
        d-=dd[i]*pow(10,n-i-1)
    flgstair = True
    for i in np.arange(n-1):
        if dd[i]-dd[i+1]!=-1 and dd[i]-dd[i+1]!=9:
            flgstair = False
    if flgsame or flgstair:
        ret="Weak"
    else:
        ret="Strong"
    print(ret)

def abc212c():
    n,m = map(int, input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    minval=1e9
    jstart=0

    for i in np.arange(m):
        jx=bisect.bisect_left(a,b[i])
        if 0<jx<n:
            minvaltemp = min(a[jx]-b[i],b[i]-a[jx-1])
        elif jx==0:
            minvaltemp = a[0]-b[i]
        elif jx==n:
            minvaltemp = b[i]-a[n-1]
        else:
            print("err")
            return -1
        if minvaltemp<minval:
            minval=minvaltemp
    print(minval)
    return 0


if __name__ == '__main__':
    abc212c()