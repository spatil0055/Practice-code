def second_l(arr):
    largest = float("-inf")
    second = float("-inf")
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
arr = [1,2,3,4,9805,0]
print(second_l(arr))