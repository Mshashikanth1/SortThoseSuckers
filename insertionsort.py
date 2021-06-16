def insertionsort(a):
    for i in range(1,len(a)):
        for j in range(i):
            if a[j]>a[i]:
                a[j],a[i]=a[i],a[j]
        
#driver code
a=list(map(int,input().split()))
insertionsort(a)
print(a)
