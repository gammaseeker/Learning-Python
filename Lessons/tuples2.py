Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
>>> squares
[1, 4, 9, 16, 25]
>>> squares = []
>>> for x in [1, 2, 3, 4, 5]:
	squares.append(x**2)

	
>>> squares
[1, 4, 9, 16, 25]
>>> T = (1, 2, 3, 4)
>>> len(T)
4
>>> T[0]
1
>>> T.index(0)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    T.index(0)
ValueError: tuple.index(x): x not in tuple
>>> T.index(4)
3
>>> 
