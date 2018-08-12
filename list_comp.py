a = 4
b = 9
count_list = [1,2,3,a,5,6,7,8,b,10]
#List comprehensions in Python are constructed as follows: list_variable = [x for x in iterable]
s = [x**2 for x in range(10)]
print(s)

v = [2**i for i in range(13)]
print(v)

m = [x for x in s if x % 2 == 0]
print(m)

q = [x**3 for x in range(11)]
print(q)
