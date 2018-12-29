thisdict = {
    "brand":"Tesla",
    "model":"Model 3",
    "year": 2018
}
print(thisdict)
#del(thisdict)
thisdict.clear()
print(thisdict)

empty = {}
if 'test' in empty:
    print('test')
else:
    print('Not found')


thisdict = {
    "brand":"Tesla",
    "model":"Model 3",
    "year": 2018
}
for k, v in thisdict.items():
    print("{}: {}".format(k, v))
