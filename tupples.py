t = (1, 2, 3)
print(t)         
print(type(t))  


t = 1, 2, 3
print(t)         


t = tuple([1, 2, 3])
t2 = tuple("abc")
print(t)       # (1, 2, 3)
print(t2)      # ('a', 'b', 'c')


t = (1, 2, (3, 4))
print(t[2][0])  # 3


a, b, c = (1, 2, 3)

t1 = (1,)   # single element
t2 = 1,     #  single element without parentheses
t3 = (1)    # NOT a tuple, just int


t1 = tuple([1, 2, 3])   # from list
t2 = tuple("abc")       # from string
t3 = tuple({1, 2, 3})   # from set

