import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #phoneNumRegex contains a Regex object
#typing r before string marks raw string so no need to use escape characters
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
# Desired pattern is passed into re.compile()
# Call search() for a match
# Result is stored in mo, mo.group() will return the match
''' Algorithm
    1. Import the regex module with import re.
    
    2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)

    3. Pass the string you want to search into the Regex object’s search() method.
This returns a Match object.

    4. Call the Match object’s group() method to return a string of the actual
matched text.


'''
