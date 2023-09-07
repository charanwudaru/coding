arr=[1,2,3,4,5]
n = 7
m=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==n:
            m.append([i,j])
print(m)



