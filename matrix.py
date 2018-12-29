#matrix = [[0 for y in range(8)] for x in range(8)]
#print (matrix)

matrix = []
row = []
for j in range(1, 26):
    if(j%5 == 0):
        row.append(j)
        matrix.append(row[:])
        row.clear()
    else:
        row.append(j)
print(matrix)
