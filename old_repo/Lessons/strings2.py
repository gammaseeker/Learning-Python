S = 'Spam'
print len(S)
print S[0]
print S[1]

print S[-1] # Last item from the end in S
print S[-2] # Second to last item from the end
print S[1:3] # Prints S from index 1 to 2
print S[1:]
print S[0:3]
print S[:3]
print S[:-1] # Prints everything but the last character
print S[:] # Prints everything
print S * 8

# Strings are immutable
# S[0] = 'z' does not work
S = 'z' + S[1:]
print S # But we can run expressions to make new objects