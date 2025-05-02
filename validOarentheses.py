    
def getBool(s):
    if len(s)%2     == 1:
        return False
    needNext = []

    pairs = {
        "(":")",
        "{":"}",
        "[":"]" 
    }

    count = 0
    pos = 0
    last = len(s)
    while(pos != last):
        current = s[pos]
        if current in pairs:#if current is an open key add its value to our next needed stack
            needNext.append(pairs[current])
            count += 1
        else:#if our current is a closed value
            count -= 1
            if count < 0:
                return False
            if current == needNext[-1]:#if current is the next value needed
                needNext.pop()
            else:
                return False
            
        pos += 1
    if count != 0 or len(needNext) != 0:
        return False
    return True



testCases = ["(("]
for tests in testCases:
    ans = getBool(tests)
    print(tests + str(ans))

