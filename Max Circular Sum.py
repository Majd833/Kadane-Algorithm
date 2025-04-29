def kadane(a):
    n=len(a)
    maxsf=0
    maxeh=0
    for i in range(0,n):
        maxeh=maxeh+a[i]
        if maxeh<0:
            maxeh=0
        if maxsf <maxeh:
            maxsf=maxeh
    return maxsf
def maxcirsum(a):
    n=len(a)
    maxkadane=kadane(a)
    maxwrap=0
    for i in range(0,n):
        maxwrap+=a[i]
        a[i]=-a[i]
    maxwrap=maxwrap+kadane(a)
    if maxwrap>maxkadane:
        return maxwrap
    else:
        return maxkadane
a=[1,2,3,-4,56,3,-22,5,9]
print(maxcirsum(a))