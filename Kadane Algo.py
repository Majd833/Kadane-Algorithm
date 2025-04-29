#Program to find max subarray sum
def maxsubsum(a,asize):
    max=-999999999999
    curmax=0
    #Add current element to current max, check if curmax > max update max, if curmax is less than 0 then reset it to 0.
    for i in range(0,asize):
        curmax=curmax +a[i]
        if max < curmax:
            max=curmax
        if curmax<0:
            curmax=0
    return max
a=[1,2,3,-4,5,-14,34,2,-8]
print(maxsubsum(a,len(a)))