def comma_code(lst):
    output = ''
    for i in range (0, len(lst)):
        if i == (len(lst)-1):
            output += 'and ' + lst[i]
            return output
        else:
            output += lst[i] + ', '

test1 = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(test1))
