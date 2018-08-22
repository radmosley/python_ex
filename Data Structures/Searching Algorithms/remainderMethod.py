#weighted remainder method
alist = [27, 13, 0]

def has(alist, tablesize):
    sum = 0
    for pos in range(len(alist)):
        sum = sum + alist[pos]

    return sum%tablesize

print(has(alist, 13))