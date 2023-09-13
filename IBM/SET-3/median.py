arr=[1,2,3,4,5,6]
n=len(arr)
if n%2!=0:
    k=int((n+1)/2)
    print(k) 
else:
    arr.sort()
    k=int(n//2)
    p=(arr[k-1]+arr[k])/2
    print(p)