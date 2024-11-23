def reverse(num):
    res = 0
    temp = num
    while temp > 0:
        r = temp % 10
        res = (res*10) + r
        temp //= 10
    print(res)


num = int(input("enter: "))
reverse(num)