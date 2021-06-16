def selectionsort(a):
    for i in range(len(a)):
        min_ind=i
        for j in range(i,len(a)):
            if a[j]<a[min_ind]:
                min_ind=j
        a[i],a[min_ind]=a[min_ind],a[i]
#driver code
a=list(map(int,input().split()))
selectionsort(a)
print(a)


