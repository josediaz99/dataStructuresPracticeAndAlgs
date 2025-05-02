x = 101

result = True
palendrome = str(x)
backwards = palendrome[::-1]

for i in range(1,len(palendrome)):
    char1 = palendrome[i]
    char2 = backwards[i]
    if char1 != char2:
        result = False
        break

print(result)