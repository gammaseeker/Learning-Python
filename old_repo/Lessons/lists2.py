Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L = [123, 'spam', 1.23]
>>> len(L)
3
>>> L[0]
123
>>> L[:-1]
[123, 'spam']
>>> L + [4, 5, 6]
[123, 'spam', 1.23, 4, 5, 6]
>>> L
[123, 'spam', 1.23]
>>> L.append('NI')
>>> L
[123, 'spam', 1.23, 'NI']
>>> L.pop(2)
1.23
>>> L
[123, 'spam', 'NI']
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']
>>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> M[1]
[4, 5, 6]

>>> m[1][2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    m[1][2]
NameError: name 'm' is not defined
>>> M[1][2]
6
>>> col2 = [row[1] for row in M]
>>> col2
[2, 5, 8]
>>> [row[1] + 1 for row in M]
[3, 6, 9]
>>> [row[1] for row in M if row[1] % 2 == 0]
[2, 8]
>>> diag = [M[i][i] for i in [0, 1, 2]]
>>> diag
[1, 5, 9]
>>> doubles = [c * 2 for c in 'spam']
>>> double
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    double
NameError: name 'double' is not defined
>>> doubles
['ss', 'pp', 'aa', 'mm']
>>> 
