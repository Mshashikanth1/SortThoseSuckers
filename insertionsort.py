#this is an implementaion of insertion sort
#detail explanation at https://www.youtube.com/watch?v=Gq8lno2N0n0&t=

def insertionsort(a):
    for i in range(1,len(a)):
        for j in range(i):
            if a[j]>a[i]:
                a[j],a[i]=a[i],a[j]
        
#driver code
a=list(map(int,input().split()))
insertionsort(a)
print(a)
