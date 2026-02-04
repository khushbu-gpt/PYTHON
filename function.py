def isNum(num):
    return num
res=isNum(5)
print(res)

def power(x, n=2):
    return x ** n

power(1,3)

def add(a, b):
    return a + b

res1=add(b=2, a=1)
print(res1)

def f(*args, **kwargs):
    print(args)
    print(kwargs)
f(3,4)