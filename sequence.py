n = int(input())
gap = 0
first = 1
if n == 1:
    print(first)
else:
    print(first, end = ' ')
    while n > 1:
        for j in range(2):
            first += gap
            print(first, end=' ')
            n -= 1
            if n == 1:
                break
        gap += 1

