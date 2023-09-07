a=int(input())
count=0
for i in range(a+1):
    if i%2==0:
        count=count+1
        
if count==2:
    print("prime")
elif count>2:
    print('not prime')
else:
    print("give other than 1 or 0")
    