a = [-8,0,2,5]

def index_equals_value(a):
    index = 0
    for i in a:
        if index != i:
            index += 1
            
        
        
        else: 
            if index == i:
                print(index)
    else:
        print(-1)
index_equals_value(a)