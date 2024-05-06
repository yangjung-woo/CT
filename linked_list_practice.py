class Node: 
    # 각 노드는 next node 의 address 정보도 가지고 있기 때문에 연속성 유지 가능 
    # 메모리 할당시 연속적으로 저장할 필요 없음 -> 메모리 사용성이 자유로움 
    def __init__(self, value=0 , next = None): # defalt  0, Null
        self.value = value 
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)   # f,s,t  의 value = 1,2,3 , next = null ,null ,null
first.next =second
second.next =third


class LinkedList(object):
    def __init__(self):
        self.head =None # linked list 생성시 반드시 head는 최초 노드를 가리켜야 한다
        self.tail = None # 성능 개선을 위한 tail , append_back 에 이용
    def append(self,value):
        new_node = Node(value) # 새 노드 생성

        if self.head == None:# 최초  head 가 아무것도 가리키지 않음
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next


    def get(self,idx):
        current = self.head
        for i in range(idx):
            current= current.next
        return current.value  # get 시간복잡도? O(n)

    def insert(self,idx,value):
        pass
    def delete(self,idx):
        pass