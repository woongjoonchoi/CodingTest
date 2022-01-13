# O = [[ [3,5] , [1,1]]]

# # alloc = [ [5,5] , [1,1]]
# alloc = [[1,2] , [1,1]]
# count_O = 3
# print(alloc[0][0])
# if alloc is not None:
#     flag = False
#     for i in range(len(O)) :
#         x,y = O[i]
#         if max(alloc[0][0] , x[0] ) <= min(alloc[0][1] , x[1])  and \
#             max(alloc[1][0] , y[0] ) <= min(alloc[1][1] , y[1]):
#             flag = True
#             O[i][0]  = [max(alloc[0][0] , x[0] ) , min(alloc[0][1] , x[1])]
#             O[i][1]  = [max(alloc[1][0] , y[0] ) , min(alloc[1][1] , y[1])]
#             break
#         if not flag  :
#             O.append(alloc)
#             count_O-=1
# print(O)
# print(count_O)



a = [(1,2) , (3,4)]
print(set(a))