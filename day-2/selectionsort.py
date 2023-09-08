a=[4, 6, 1, 0, 5]
n=len(a)
for i in range(n):
    min=i
    for j in range(i+1,n): #range(start, stop, step)
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
print(a)
