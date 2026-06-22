class Node:
    def __init__(self):
        self.data=None
        seld.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next = new