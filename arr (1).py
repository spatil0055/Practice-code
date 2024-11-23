def sum_arr(arr):
    f = arr[0]
    for i in range(len(arr)-1):
        arr[i] += arr[i+1]
    arr[-1] += f
    return arr


arr = list(map(int,input().split()))
result = sum_arr(arr)
print(result)