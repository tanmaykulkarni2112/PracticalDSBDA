arr = [-2,32,1,4,5,6,8,9,0,0,76,32,7]

for i in range(len(arr)):
    minn = arr[i]
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
