def find_busiest_period(data):
    people = 0
    temp = 0
    best_time = 0

    for x in range(len(data)):
        i = data[x]
        if i[2] == 0:
            people -= i[1]
        else: 
            people += i[1]
            
        if x == len(data)-1 or data[x][0] != data[x+1][0]:
            if people > temp:
                temp = people
                best_time = i[0]
    return best_time


# def find_busiest_period(data):
#     people = 0
#     temp = 0
#     best_time = 0

#     # for x in range(len(data)):
#     #     if data[x][2] == 0:
#     #         people -= data[x][1]
#     #     else:
#     #         people += data[x][1]
#     #     if x <= len(data):
#     #         if people > temp:
#     #             temp = people
#     #             best_time = data[x][0]
#     # return best_time
   
#     for x in data:
#         if 

            
#         # for data[x][0] in data:

# # data = [ [1487799425, 14, 1], 
# #                  [1487799425, 4,  0],
# #                  [1487799425, 2,  0],
# #                  [1487800378, 10, 1],
# #                  [1487801478, 18, 0],
# #                  [1487801478, 18, 1],
# #                  [1487901013, 1,  0],
# #                  [1487901211, 7,  1],
# #                  [1487901211, 7,  0] ]

data = [[1487799425,14,1],
[1487799425,4,0],
[1487799425,2,0],
[1487800378,10,1],
[1487801478,18,0],
[1487801478,18,1],
[1487901013,1,0],
[1487901211,7,1],
[1487901211,7,0]]

# find_busiest_period(data)

print(find_busiest_period(data))