def binary_search(l, key):
    high = len(l)-1
    low = 0
    while(high >= low):
        mid = low + (high - low)/2
        if(l[mid] == key):
            return mid
        if(l[mid] > key):
            high = mid -1
        if(l[mid] < key):
            low = mid + 1
    return -1

my_list =[x for x in range(27, 50)] 
print(binary_search(my_list, 23))


