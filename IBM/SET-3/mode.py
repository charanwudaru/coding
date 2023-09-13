def find_mode(arr):
    freq = {}
    for i in arr:
        if i in freq:
           freq[i] += 1
        else:
           freq[i] = 1
    mode = max(freq, key=freq.get)
    return mode
    
arr=[1,23,22,32,23,23,23]
print(find_mode(arr))