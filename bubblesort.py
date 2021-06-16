def bubblesort(a,l,h):
    for i in range(l,h):
        for j in range(i,h):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]


#driver code
a=list(map(int,input().split()))
bubblesort(a,0,len(a)-1)
print(a)
