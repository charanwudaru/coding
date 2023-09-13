def find_missing_number(arr):
    
    #write your code here
    for i in range(len(arr) - 1, 0, -1):
        
       
        for j in range(i):
            
            
            if arr[j] > arr[j + 1]:
                
            # Swap elements using tuple packing/unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    maxn = arr[-1]
    minm = arr[0]
    missing_number=0
    for k in range(minm-1,maxn+1):
        if k not in arr:
            missing_number=missing_number+k
    
    return missing_number

arr=[0,1,2,3,4]
print(find_missing_number(arr))