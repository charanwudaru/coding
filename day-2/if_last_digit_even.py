# d=[1,2,4,4,4,6,8,9,0,3]
# i = len(d) - 1

# while i >= 0:
#     if d[i]%2==0:
#         d.pop(i)
#     else:
#         print(d)
#         break
#     i=i-1
    
    
a= int(input())
while a>0:
    k=a%10
    if k%2==0:
        a=a//10
        print(a)
        break
    else:
        print(a)
        break






