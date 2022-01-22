import itertools
높이 = 너비 = int(input())
# NxN 크기의 복도라는 :파워:워드:
복도 = [
    input().split()
    for __ in range(높이)
]

선생님들 = [
    (r, c)
    for r in range(높이)
    for c in range(너비)
    if 복도[r][c] == 'T'
]

가로_구역 = []
세로_구역 = []

## 선점구역 , v
for r, c in 선생님들:
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        a = []
        학생발견 = False
        while 0 <= nr < 높이 and 0 <= nc < 너비:
            if 복도[nr][nc] == 'X':
                a.append((nr, nc))
            elif 복도[nr][nc] == 'S':
                학생발견 = True; break
            else: break
            nr += dr; nc += dc
        if 학생발견:
            (가로_구역 if dr == 0 else 세로_구역).append(set(a))

성공 = True
if len(가로_구역) > 3 or len(세로_구역) > 3:
    성공 = False
else:
    
    #무조건 커버해야만 하는 범위
    집합들 = []
    쓴_세로 = set()
    for i, v in enumerate(가로_구역):
        flg = False
        #flg : 겹치는 범위 
        for j, v2 in enumerate(세로_구역, len(가로_구역)):
            if v & v2:
                집합들.append({i, j})
                flg = True
                쓴_세로.add(j)
        if v and not flg: 집합들.append({i})
    for j, v in enumerate(세로_구역, len(가로_구역)):
        if v and j not in 쓴_세로: 집합들.append({j})
        
    #집합들 : 무조건 커버 해야 하는 범위들 
    if len(집합들) <= 3:
        성공 = len(set().union(*집합들)) == len(가로_구역) + len(세로_구역)
    if len(집합들) > 3:
        성공 = False
        for t in itertools.combinations(집합들, 3):
            s = set()
            for s2 in t: s.update(s2)
            if len(s) == len(가로_구역) + len(세로_구역):
                성공 = True
print('YES' if 성공 else 'NO')