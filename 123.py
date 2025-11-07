def fib(n):
    if n==1 or n==2:
        return 1
    a,b = 1,1
    for _ in range(3,n+1):
        c = a+b
        a,b = b,c
    return b
n=int(input("请输入一个整数n:"))
result=fib(n)
print(f"f({n})={result}")