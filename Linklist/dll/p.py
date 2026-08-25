class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def insert_at_start(self,value):
        Newnode=Node(value)


        if self.head == None:
            self.head=Newnode
            return
        else:
            Newnode.next=self.head
            self.head.prev=Newnode
            self.head=Newnode

    def reverse(self):
        curr=self.head
        temp=None

        while curr:

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
             

l = dll()
l.insert_at_start(10)
l.insert_at_start(20)
l.insert_at_start(30)

l.display()

     
    