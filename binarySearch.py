def binarySearch (list,target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None