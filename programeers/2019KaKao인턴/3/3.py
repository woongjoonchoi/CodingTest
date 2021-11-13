
count = 0
c_set=[]
def ban(c_l , level , s):
    
    global count
    global c_set
    if level == len(c_l) :
        k= set(s)
        if len(k) == len(c_l):
            if k not in c_set :
                count+=1
                c_set.append(k)
        return
    for c in c_l[level] :
        s.append(c)
        ban(c_l,level+1,s)
        s.pop()
    
    return

def solution(user_id, banned_id):
    answer = 0
    temp = 0
    c_l=[]
    for b in banned_id :
        li = []
        cnt = []
        for i,d in enumerate(b):
            if d == '*':
               li.append(i)
        for u in user_id:
            s = list(u)
            for k in li :
                if k < len(u) :
                    s[k] = '*'
            s = ''.join(s)
            if s == b:
                cnt.append(u)
        c_l.append(cnt)
    s=[]
    
    ban(c_l,0,s)
        
    answer=count
        
    return answer

solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])


# st =set()
# s1=set([1,2])
# s2=set([2,1])


# st.add((1,2))
# st.add((2,1))

# print(st)
# if s1==s2 :
#     print(True)