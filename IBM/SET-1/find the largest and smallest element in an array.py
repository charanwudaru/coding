arr=[3,54,22,43,75,45,23,86,4,0]
a=len(arr)
for i in range(a):
    for j in range(i+1,a):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print("Sorted array is:",arr)
print(arr[-1])
print(arr[0])