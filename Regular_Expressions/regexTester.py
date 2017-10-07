import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(input("Enter input: "))
print('Phone number found: ' + mo.group())
