def part(s,e,l):
    pi=s
    p=l[pi]
    while s<e:
        while s<len(l) and l[s]<=p:
            s+=1
        while l[e]>p:
            e-=1
        if s<e:
            l[s],l[e]=l[e],l[s]
    l[e],l[pi]=l[pi],l[e]
    return e
def qsort(s,e,l):
    if s<e:
        p=part(s,e,l)
        qsort(s,p-1,l)
        qsort(p+1,e,l)
    return l








n=list(map(int,input().split(" ")))


print(qsort(0,len(n)-1,n))






