n = [6, 7, 9, 0, 5, 4]

for i in range(len(n) - 1, 0, -1):
    for j in range(i):
        if n[j] > n[j + 1]:
            cat = n[j]
            n[j] = n[j + 1]
            n[j + 1] = cat

print("Sorted array is:", n)