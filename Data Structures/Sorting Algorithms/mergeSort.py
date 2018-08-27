def mergeSort(a):
    print('Splitting ', a)
    if len(a) > 1:
        mid = len(a)//2
        front = a[:mid]
        rear = a[mid:]

        mergeSort(front)
        mergeSort(rear)

        i = 0 
        j = 0
        k = 0
        while i < len(front) and j < len(rear):
            if front[i] < rear[j]:
                a[k] = front[i]
                i = i + 1
            else:
                a[k] = rear[j]
                j = j + 1
            k = k + 1

        while i < len(front):
            a[k] = front[i]
            i = i + 1
            k = k + 1

        while j < len(rear):
            a[k] = rear[j]
            j = j + 1
            k = k + 1
    print('Merging', a)

alist = [54,26,93,17,77,31,44,55,20]
alist =  [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
mergeSort(alist)
print(alist)

