def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind], arr[i]
    return arr
def bin_search(arr,low,high, key):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        bin_search(arr,mid+1,high,key)
    else:
        bin_search(arr,low,mid-1,key)      
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr) 
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
             
        arr[j+1] = key

def merge(arr):
    n = len(arr)
    if n > 1:
        mid = n //2
        
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge(left_half)
        merge(right_half)
        
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1  
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  
    elif target < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)
i_arr= [1,2,3,4,5,6]
k=6

r=binary_search_recursive(i_arr,0,len(i_arr)-1,k)
if r != -1:
    print(r)
else:
    print(-1)

