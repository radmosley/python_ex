n = [1, 3, 1]
l = [4, 7, 5, 7]
k = [4, 8, 1, 4]

def min_value(digits):
    prune = sorted(list(set(digits)))
    num = int(''.join(map(str, prune)))
    return num

print(min_value(k))

# min_value(l)