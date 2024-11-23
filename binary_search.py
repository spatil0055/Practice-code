def binary_2d(matrix, key):

    if not matrix or not matrix[0]:
        return -1

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:

        mid = (left + right) //2

        row = mid // cols
        col = mid % cols
        
        if matrix[row][col] == key:
            return (row,col)
        elif matrix[row][col] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1
matrix = []
r = int(input())
c = int(input())

for i in range(r):
    row = list(map(int, input(f"Enter elements of row {i + 1} separated by space: ").split()))
    matrix.append(row)


target = int(input())
print(matrix)
result = binary_2d(matrix, target)

if result != -1:
    print(f"Element found at row {result[0]+1}, column {result[1]+1}")
else:
    print("Element not found")
