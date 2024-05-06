
class makenode(object):
    def __init__(self, val = "" ,next = None , prev = None ):
        self.val = val
        self.next = next
        self.prev = prev



class BrowserHistory(object):

    def __init__(self, homepage): # current , head 설정 
        self.head = makenode(val=homepage)
        self.current = makenode(val=homepage)
        

    def visit(self, url):
        self.current.next = makenode(val=url, prev= self.current)# 새 노드 생성
        self.current = self.current.next # 현재 노드 변경 갱신 
        return None

    def back(self, steps):
        while steps >0 and self.current.prev != self.head:
            self.current = self.current.prev
            steps -=1
        return self.current.val
        

    def forward(self, steps):
        while steps >0 and self.current.next != self.head:
            self.current = self.current.next
            steps -=1
        return self.current.val
        
