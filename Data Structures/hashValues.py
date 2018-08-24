array4 = [113, 117, 97, 100, 114, 108, 116, 105, 99]

def mod(array, tablesize):
    for a in array:
        print(a%tablesize)


mod(array4, 11)