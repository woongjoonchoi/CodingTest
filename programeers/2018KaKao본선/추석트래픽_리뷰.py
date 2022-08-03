
#  1. 구간에 어떤 구간이 겹치는지 체크하는 부분 틀림  
#  나는 시작점 , 끝점이 전부 구간안에 포함이 되어야 한다고 코딩함
#  문제풀때는 시작점, 끝점중 하나가 구간안에 있으면된다고 함

# 2. 2개의 구간만 체크하면 되는데 중복되게 체크함

def solution(lines):
    answer = 0
    start = []
    end = []
    for l in lines :
        _ , S , T  = l.split()
        hh , mm , ss = list(map(float,S.split(':')))
        
        E = round(hh * 3600 + mm*60 + ss,3)
        S = round(E - float(T[:-1]) + 0.001,3)
        start.append(S)
        end.append(E)
        # print("{}  {}".format(S , E))
        
    # print(list(zip(start,end)))
    for s , e  in zip(start,end) :
        count = [0] * 4
        for s1, e1 in zip(start,end) :
            # t_s = [round(s-0.999,3), round(s,3) , round(e-0.999,3),round(e,3)]
            # t_e = [round(s,3) , round(s+0.999,3) , round(e,3) , round(e+0.999,3)]     
            t_s = [ round(s,3) ,round(e,3)]
            t_e = [ round(s+0.999,3)  , round(e+0.999,3)]
            for i , (ss , ee) in enumerate(zip(t_s,t_e)) :
                if ee >=s1  and ss <=e1 :
                    count[i] +=1
        # print(list(zip(t_s,t_e)))
        # print(count)
        answer = max(max(count),answer)
        
    return answer