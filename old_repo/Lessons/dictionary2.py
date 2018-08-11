Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
>>> D['food']
'Spam'
>>> F
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    F
NameError: name 'F' is not defined
>>> D
{'food': 'Spam', 'color': 'pink', 'quantity': 4}
>>> D['quantity'] +=1
>>> D
{'food': 'Spam', 'color': 'pink', 'quantity': 5}
>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'job':  ['dev', 'mgr'],
           'age':  40.5}
>>> rec['name']
{'first': 'Bob', 'last': 'Smith'}
>>> rec['name']['last']
'Smith'
>>> rec['job']
['dev', 'mgr']
>>> rec['job'].append('janitor')
>>> rec
{'job': ['dev', 'mgr', 'janitor'], 'age': 40.5, 'name': {'first': 'Bob', 'last': 'Smith'}}
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> Ks = list(D.keys())
>>> Ks
['c', 'b', 'a']
>>> Ks.sort()
>>> Ks
['a', 'b', 'c']
>>> for key in Ks:
	print key, '=>', D[key]
	
SyntaxError: Missing parentheses in call to 'print'
>>> for key in Ks:
	print (key, '=>', D[key])

	
a => 1
b => 2
c => 3
>>> 
