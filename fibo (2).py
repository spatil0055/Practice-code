def fibo(num):
    f = 0
    s = 0
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num >2:
        return fibo(num-1) + fibo(num-2)

def facto(n):
    if n==1 or n==0:
        return 1
    return n*facto(n-1)

def swap_num(n1,n2):
    n1 = n1 + n2
    n2= n1 - n2
    n1 = n1 - n2
    print(n1,n2)

def gcd(n1,n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1%n2)


n = int(input())
m = int(input())
print(gcd(n,m))
# print(fibo(n))
# print(facto(n))
# first = 0
# second= 1
# if n == 1:
#     print(first)
# elif n == 2:
#     print(first," ",second)
# elif n>=3:
#     print(first,second,end=" ")
#     for i in range(2,n):
#         third = first + second
#         print(third,end=" ")
#         first = second
#         second = third
# else:
#     print("invalid number")

