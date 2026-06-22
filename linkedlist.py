class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return
    def add_beg(self,data):
        obj=Node(data)
        if self.head is None:
            self.head=obj
            return
        obj.next=self.head
        self.head=obj
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = new

    def display(self):
        itr = self.head

        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next

        print("None")


ll = LinkedList()

ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)

ll.display()