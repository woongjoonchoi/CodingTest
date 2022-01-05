class DLL:
    def __init__(self):
        self.cur=None
        self.head=None
        self.end=None
        self.garbage=[]
        self.size=0
    def insert(self,node):
        node.previous=self.end
        self.end.next=node
        self.end=node
        self.size+=1
    def delete(self):
        if self.cur == self.head:
            self.head=self.cur.next
        if self.cur.previous is not None : self.cur.previous.next= self.cur.next
        if self.cur.next is not None: self.cur.next.previous=self.cur.previous
        self.garbage.append(self.cur)
        if self.cur.next!=None :self.cur=self.cur.next 
        else : self.cur=self.cur.previous
        self.size-=1
    def recovery(self):#  가장최근노드만
        node=self.garbage.pop()
        if node.previous is not None : node.previous.next=node
        else : self.head=node
        if node.next is not None : node.next.previous=node
        self.size+=1
    def D(self,steps):
        for i in range(steps) : 
            self.cur=self.cur.next
    def U(self,steps):
        for i in range(steps) :
            self.cur=self.cur.previous  
    def d_set(self,head):
        self.head=head
        self.end=head
        self.size+=1
class Node:
    def __init__(self,val):
        self.previous=None
        self.next=None
        self.val=val
    def get_value(self):
        return self.val
def solution(n, k, cmd):
    d_l = DLL()
    answer=''
    for i in range(n):
        nd= Node(i)
        if i == 0: 
            d_l.d_set(nd)
        else: d_l.insert(nd)
        if i == k:
            d_l.cur=nd
    for c in cmd:
        cm=c.split()
        if len(cm)==2 :
            com,num = cm
            if com=="U":
                d_l.U(int(num))
            elif com=="D":
                d_l.D(int(num))
            else:
                print("Error: not U D")
        elif len(c)==1 :
            com=c
            if com=="C":
                d_l.delete()
            elif com=="Z":
                d_l.recovery()
    # answer = ['O'] * n
    answer = ['X'] * n
    cur=d_l.head
    i=0

    while cur is not None :

        answer[cur.get_value()]='O'
        cur=cur.next
    answer=''.join(answer)
    return answer
# # solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
# solution(5, 0 ,["D 2"])
# # solution(	5, 0, ["C", "C", "C", "C"])