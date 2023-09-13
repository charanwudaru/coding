def find_intersection(array1, array2):
    res=[]
    for i in array2:
        if i in array1:
            res.append(i)
            
            
    return res

array1=[1,2,3,4,5]
array2=[5,4,6,2]
print(find_intersection(array1,array2))