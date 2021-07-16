def bs(l,low,high,m):
    if m==l[high]:
        return high
    elif m==l[low]:
        return l[low]
    else:
        mid = (low + high) // 2
        if l[mid]==m:
            return mid-1
        elif m>l[mid]:
            return bs(n,mid+1,high,m)
        elif m<l[mid]:
            return bs(n,low,mid-1,m)




n=list(map(int,input().split(" ")))

m=int(input())
low = 0
high = len(n) - 1
print(bs(n,low,high,m))



