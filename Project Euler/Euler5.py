#Joey Jiemjitpolchai
num = 0
for x in range(180,1000000000,10):
    if num != 0:
        break
    for y in range(2,21):
        if x % y != 0:
            break
        if x % y == 0:
            if y == 20:
                num = x
            continue
print (num)
