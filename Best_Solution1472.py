## APPROACH : LINKED LISTS ##
## LOGIC : GREEDY ##
# python 3 style 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while(steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while(steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val