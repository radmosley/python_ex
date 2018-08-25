
# def shortBubble(a):
#     exchanges = True
#     passnum = len(a)-1
#     while passnum > 0 and exchanges:
#         exhanges = False
#         for i in range(passnum):
#             if a[i] > a[i+1]:
#                 exhanges = True
#                 temp = a[i]
#                 a[i] = a[i+1]
#                 a[+1] = temp
#         passnum = passnum - 1
# alist = [9, 10, 6, 2, 4]

# shortBubble(alist)
# print(alist)

# def shortBubbleSort(alist):
#     exchanges = True
#     passnum = len(alist)-1
#     while passnum > 2 and exchanges:
#        exchanges = False
#        for i in range(passnum):
#            if alist[i]>alist[i+1]:
#                exchanges = True
#                temp = alist[i]
#                alist[i] = alist[i+1]
#                alist[i+1] = temp
#        passnum = passnum - 1

# # alist=[20,30,40,90,50,60,70,80,100,110]
# alist =  [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
# shortBubbleSort(alist)
# print(alist)

# def selectionSort(a):
#     for fillslot in range(len(a)-1, 0, -1):
#         positionOfMax = 0
        
#         for location in range(1, fillslot+1):
#             if a[location] > a[positionOfMax]:
#                 positionOfMax = location

#         temp = a[fillslot]
#         a[fillslot] = a[positionOfMax]
#         a[positionOfMax] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# print(alist)
# selectionSort(alist)
# print(alist)

# def insertSort(a):
#     for index in range(1, len(a)):
#         currentvalue = a[index]
#         position = index

#         while position > 0 and a[position-1] > currentvalue:
#             print(position)
#             a[position] = a[position-1]
#             position = position - 1

#         a[position] = currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertSort(alist)
# print(alist)

def shellSort(a):
    sublistcount = len(a)//3
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(a, startposition, sublistcount)

            print('After increments of size {} the list is {}'.format( sublistcount, a))

        sublistcount = sublistcount // 3
def gapInsertionSort(a, start, slc):
    for i in range(start+slc, len(a), slc):
        currentvalue = a[i]
        position = i

        while position >= slc and a[position-slc] > currentvalue:
            a[position] = a[position-slc]
            position = position-slc

        a[position] = currentvalue


alist = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7]
shellSort(alist)
print(alist)
print(10//3)