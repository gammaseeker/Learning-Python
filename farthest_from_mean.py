lst = [1, 2, 3, 4, 5, 6, 7]
avg = sum(lst)/len(lst)
def func():
    farthest = [0, 0, 0]
    for i in range(0, len(lst)):
        diff = abs(avg - lst[i])
        if diff > farthest[2]:
            farthest[0] = i
            farthest[1] = lst[i]
            farthest[2] = diff
    lst.remove(farthest[1])        
    return farthest
print(func())
print(lst)
print(func())
print(lst)
print(func())
print(func())
