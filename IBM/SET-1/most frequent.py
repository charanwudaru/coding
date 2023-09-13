def find_most_frequent(arr):
    count=0
    temp=0
    index=0
    for i in range(0,len(arr)):
        temp=arr.count(arr[i])
        
        if temp>count:
            count=temp
            index=i
    most_frequent = arr[index]
    return most_frequent

arr=[2,3,2,4,5,3,4,3]
print(find_most_frequent(arr))