
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
alist = [9, 10, 6, 2, 4]
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

def selectionSort(a):
    for fillslot in range(len(a)-1, 0, 1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if a[location] > a[positionOfMax]:
                positionOfMax = location

            