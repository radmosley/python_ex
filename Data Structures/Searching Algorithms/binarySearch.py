a = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

def binarySearch(a, item):
    if len(a) == 0:
        return False
    else:
        midpoint = len(a)//2
        if a[midpoint] == item:
            return True
        else:
            if item < a[midpoint]:
                print(a[midpoint])
                return binarySearch(a[:midpoint], item)
            else:
                print(a[midpoint])
                return binarySearch(a[midpoint+1:], item)

binarySearch(a, 16)