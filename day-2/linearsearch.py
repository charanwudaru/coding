# f=9
# n=[1,3,9,32,4]
# for i in range(len(n)):
#     if n[i]==f:
#         print(i)

def linear(f,n):
    for i in range(len(n)):
        if n[i]==f:
            return i
    return -2
    
f=9
n=[1,3,9,32,4]
k=linear(f,n)
if k!=-2:
    print(k)
else :
    print("not found")
    
