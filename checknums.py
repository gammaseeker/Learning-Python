numbers = [1, 1, 3, 4]
def checknums(num):
    if num in numbers:
        return True
    else:
        return False
for i in filter(checknums, [1,2,3]):
    print(i)
