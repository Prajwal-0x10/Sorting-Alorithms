
min=0
k=0
l=list(map(int,input().split(' ')))
for i in range(len(l)):
    min = i
    for j in range(i,len(l)):

        if l[j]<l[min]:
            min=j

    l[i],l[min]=l[min],l[i]

print(l)