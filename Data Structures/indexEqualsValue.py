array = [-8,0,2,5]
array2 = [-8,1,3,5]
array3 = [-8,0,3,5]

def index_equals_value(array):
    index = 0
    for a in array:
        if a != index:
            index += 1
        else:
            return index
    return -1

# print(index_equals_value(array))
# print(index_equals_value(array2))
# print(index_equals_value(array3))