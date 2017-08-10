
def list_comprehension(lst):
    solution = []
    for i in range(0, len(lst)):
        if(lst[i] % 2 == 0):
            solution.append(lst[i])
    return solution

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list_comprehension(list))