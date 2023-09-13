def remove_duplicates(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                arr.pop(j)
    return(arr)
            
                
arr=[1,2,3,4,5,6,1]
print(remove_duplicates(arr))


# def remove_duplicates(arr):
#     unique_elements = []
#     for item in arr:
#         if item not in unique_elements:
#             unique_elements.append(item)
#     return unique_elements

# arr = [1, 2, 3, 4, 5, 6, 1, 2]
# result = remove_duplicates(arr)
# print(result)