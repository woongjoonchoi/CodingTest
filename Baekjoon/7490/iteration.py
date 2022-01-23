# l  = int(input())


# num = [int(input()) for _ in range(l)]


# def eval(left, right,i,before,s) :
#     while i < len(s) :
#         if s[i] == ' ':
#             pass 
#         elif s[i] == '+' or s[i] == '-' :
#             if before =='+' :
#                 left += int(right)
#             else :
#                 left -= int(right)
#             right=''
#             before=s[i]
#         else : 
#             right +=s[i]
#         i+=1
#     if before == '+' :
#         left += int(right)
#     else : 
#         left -= int(right)
#     return left 
# def make_exp(i,n , s ) :
#     if i == n :
#         # s += str(i)
#         if eval(0,'' , 0 , '+' , s + str(i)) ==0 :
#             print(s+ str(i))
#         return 
#     k = [' ','+' ,'-']
#     for ss in k : 
#         make_exp(i+1 , n , s + str(i) + ss )
           
# for n in num :
#     make_exp(1,n,'')
#     print('')


s = "312" 

s +="4"

s[-1]=""
print(s)