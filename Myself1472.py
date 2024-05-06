# Linked List 문제 

class MakeList(object): # 노드 생성 
    def __init__(self, value =0 ,next=None , prev = None): # back ,foward를 편이하게 위해 prev,next
        self.value = value
        self.next = next
        self.prev = prev



class BrowserHistory(object):

    def __init__(self, homepage): # linked list의 head 와 current 설정 필요  + tail 
        self.head = MakeList(value=homepage)
        self.current = MakeList(value=homepage)
        #self.tail = MakeList(value=homepage)
        

    def visit(self, url): # visit 시 기존 기록은 전부 지우고 새 연결 생성 
        self.current.next = MakeList(value=url, prev = self.current)
        self.current = self.current.next
        return None

    def back(self, steps): # step 수 만큼 link 탑승 

        while steps > 0 and self.current.prev != None:

            self.current = self.current.prev
            steps -=1
        return self.current.value

    def forward(self, steps):
        while steps > 0 and self.current.next != None:

            self.current = self.current.next
            steps -=1
        return self.current.value
        