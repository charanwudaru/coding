arr=[4,64,7,1,5,3]
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)



