import re
import functools
# a:오른쪽 b: 왼쪽
def cmp(a,b):
    p = re.compile(r"""([\D]+?)(\d+?)\D""")
    a=p.search(a)
    b=p.search(b)
    a_head = a.group(1).casefold()
    a_num = int(a.group(2))
    b_head = b.group(1).casefold()
    b_num = int(b.group(2))

    if a_head > b_head :
        return 1
    elif a_head < b_head:
        return -1
    else :
        if a_num >= b_num:
            return 1
        elif a_num < b_num:
            return -1


def solution(files):
    answer = []
    p = re.compile(r"""([\D]+?)(\d+?)\D""")
    # for f in files:
    #     s=p.search(f)
    #     print(s.group(1))
    #     print(int(s.group(2)))
    answer=sorted(files,key=functools.cmp_to_key(cmp))
    # print(answer)
    return answer

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
# print('abc'<'abd')