def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo(n-1) + fibo(n-2) 
def prime(n):
    for i in range(2,n//2 +1):
        if n%i==0:
            return False
    return True

n= int(input())
f=0
s=1
print(prime(n))
print(fibo(n))
print(f)
print(s)
for i in range(2,n):
    t = f + s
    print(t, end=",")
    f = s
    s = t