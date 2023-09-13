def find_second_largest(arr):
    for i in range(len(arr) - 1, 0, -1):
        
        for j in range(i):
            
            if arr[j] > arr[j + 1]:
                
            # Swap elements using tuple packing/unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    second_largest = arr[-2]
    
    return second_largest

arr=[3,54,22,43,75,45,23,86,4,0]
print("Second largest element is",find_second_largest(arr))