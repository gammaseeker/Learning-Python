#Python data types

#numbers
var1 = 1
var2 = 10
#supports int, long, float, complex

#strings
str = 'Hello World!'
print str #Prints complete string
print str[0] #Prints first character of string
print str[2:5] #Prints characters from index 2 to index 4
print str[2:] #Prints string from index 2 to end
print str * 2 # Prints string two times
print str + "TEST" #Prints concatenated string

#lists
list = [ 'abd', 786, 2.33, 'john', 70.2 ]
tinylist = [123, 'john' ]
print list #Prints complete list
print list[0] #Prints first element of list
print list[1:3] #Prints elements from index 1 to index 2
print list[2:] #Prints elements from index 2 to end
print tinylist * 2 #Prints list two times
print list + tinylist #concat both lists

#tuples
tuple = ( 'abcd', 786, 2.23, 'john', 70.2 )
list = [ 'abcd', 786, 2.23, 'john', 70.2 ]
# tuple[2] = 1000 #Invalid syntax with tuple
list[2] = 1000 #Vaid with list

#dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict2 = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one'] #Prints value for 'one' key
print dict[2] # Prints value for 2 key
print dict2 # Prints complete dictionary
print dict2.keys() # Prints all the keys
print dict2.values() # Prints all the values