
def list_comprehension(lst):
    solution = []
    for i in range(0, len(lst)):
        if(lst[i] % 2 == 0):
            solution.append(lst[i])
    return solution

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list_comprehension(list))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# naive solution O(a*b)
    def dups(lst1, lst2):
        solution = []
        for i in range(len(lst1-1, 0, -1)):
            for j in range(len(lst2)-1, i, -1):
                if(lst1[i] == lst2[j]):
                    solution.append(lst1[i])
                    del lst2[j] #lst2.pop(j)
        
        return solution