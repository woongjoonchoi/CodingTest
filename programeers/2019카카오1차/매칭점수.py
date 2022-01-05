import re
import functools


# def cmp(x ,y) :
#     if 
def solution(word, pages):
    answer = 0
    score=[]
    s = 'abc'
    basic_a={}
    re2 = re.compile('<meta property=\\"og:url\\" content=\\"(https)?:\/\/.*\"')
    # print('<meta property=\"og:url\" content=\"(https)?:\/\/.*\"')
    # re2 = re.compile()
    re1 = re.compile('\"(https)?:\/\/.*\"')
    link_a={}
    for j,p in enumerate(pages):
        # p=p.lower()
        t = p.replace('>','>\n')
        # print(t)
        ind = 0
        basic = 0
        site=''
        link=[]
        meta = re1.search(p[p.find('<head') : p.find('</head>')])
        meta2 = re2.search(p[p.find('<head') : p.find('</head>')])
        # print(meta2)
        # site = meta.group()[1:-1]
        # print(meta2.group()[len('<meta property="og:url" content="'):-1])
        site = meta2.group()[len('<meta property="og:url" content="'):-1]
        # linked =  re.findall('<a href=.*\">' , p[p.find('<body') : p.find('</body>')].replace('>','>\n'))
        linked =  re.findall('<a href="https:[^>]*">' , p[p.find('<body') : p.find('</body>')])
#       link 찾을때 왜 > 를 주의해야하는가?
#       정규식으로 잘안될때 는 split,find를 이용하자
#       태그를 파싱할떄 <> 안에 >가 다시 안나오므로 >가 아닌 문자로 범위를 좁혀준다.
        # for link_long in p.split('a href=\"')[1:]:
        #     print(link_long)
        #     print('-------------------')
        #     link.append(link_long.split('\"')[0])
        #     print(link_long.split('\"'))
        #     print('===================')
        for l in linked :
            # print(l)
            # print(1)
            link.append(re1.search(l).group()[1:-1])
            # print(link)
        link_a[site] = link
        cnt = re.sub('[^a-zA-Z]', ' ', t).lower().split().count(word.lower())
        basic_a[site] = cnt
        score.append([j, site, cnt, link, len(link)])
    final={}
    for i in basic_a.keys():
        final[i] = basic_a[i]
    for k,v in link_a.items():
        for l in v:
            if l in link_a.keys() and l in basic_a.keys():
                final[l]+=basic_a[k] / len(link_a[k])
                # print(final)
    # print(final)
    li=[]
    for i,v in enumerate(final.values()):
        li.append([i,v])
        
    li.sort(key=lambda x: x[1], reverse=True)
    
    # a=[4,5,5,4,4]
    # print(a.index(max(a)))
    return li[0][0]