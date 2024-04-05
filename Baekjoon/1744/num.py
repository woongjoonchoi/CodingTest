N =int( input())

li = []
for _ in range(N) :
    li.append(int(input()))
    
li.sort()
# print(li)
min_end_ind= -1
plus_start_ind = -1
one_start_ind = -1
one_end_ind  = -1
for i,n in enumerate(li) :
    if n ==0 :
        if min_end_ind < 0 : min_end_ind=i
    elif n==1 :
        if min_end_ind <0 : min_end_ind=i-1
        if one_start_ind <0 : one_start_ind=i
        # if min_end_ind <0 : min_end_ind=i-1
    elif n>0 :
        if min_end_ind <0 : min_end_ind=i-1
        if one_start_ind >=0 : one_end_ind = i-1
        plus_start_ind = i
        break
if li[-1] < 0 :
    min_end_ind = N-1
if li[0] >=0 :
    min_end_ind = -1
if li[-1] == 1 :
    one_end_ind= N-1
# print('--------')
# print(min_end_ind)
# print(plus_start_ind)
# print(one_start_ind)
# print(one_end_ind)
# print('----------')
# print(plus_start_ind)

list_min = li[:min_end_ind+1]
list_plus = li[plus_start_ind:]

# for i in range(len())
ans  = 0
if one_start_ind >=0 :
    ans+= one_end_ind-one_start_ind+1
if min_end_ind >=0 :
    for i in range(0,len(list_min)-2,2) :
        ans += list_min[i] * list_min [i+1]
    
# print(list_min)
    if len(list_min)%2 == 0 :
        ans += list_min[-1] * list_min[-2]
    else :
        ans += list_min[-1]


# print(ans)

# print(list_plus)
if plus_start_ind >=0 :

    for i in range(len(list_plus)-1,len(list_plus)%2,-2) :
        ans += list_plus[i] * list_plus[i-1]
        
    if len(list_plus) %2 != 0:
        ans += list_plus[0]
            
print(ans)
# s_min = {min_length :0}

# s_min[min_length-1] = li[min_]
# l_plus = {0 :0}
