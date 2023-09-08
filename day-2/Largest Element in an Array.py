arr1 = [2, 5, 1, 3, 0]
n = len(arr1)
m = arr1[0]
for i in range(1, n):
    if arr1[i] > m:
        m = arr1[i]
print(m) 