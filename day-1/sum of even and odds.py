a= '12345' #O(n) time complexity n is length of str
c=0
b=0
for i in a:
    num= int(i)
    if num%2==0:
        c+=num
    else:
        b+=num
print(c,end =" ")
print(b)


a = '12345'
c = 0
b = 0
i = 0

while i < len(a):
    num = int(a[i])
    if num % 2 == 0:
        c += num
    else:
        b += num
    i += 1

print(c, end=" ")
print(b) #O(n) time complexity