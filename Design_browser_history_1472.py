class ListNode(object):

     def __init__(self, val = "", next =None , prev = None):
        self.val = val # value
        self.next = next 
        self.prev = prev 

class BrowserHistory(object):
    # linked list problem

    def __init__(self, homepage):
        self.head = ListNode(val=homepage)
        self.current = ListNode(val=homepage)
        
        
    def visit(self, url):
        self.current.next = ListNode(val=url, prev= self.current)
        self.current = self.current.next
        return None
        

    def back(self, steps):
        while steps >0 and self.current.prev !=None:
            steps -=1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps >0 and self.current.next !=None:
            steps -=1
            self.current = self.current.next
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)