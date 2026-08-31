class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkList:
    def __init__(self):
        self.head=None

    def insert_at_start(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        
        temp = self.head

        while temp.next != self.head:
            temp=temp.next

        new_node.next=self.head
        temp.next=new_node
        self.head=new_node

    
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head

        while True:
            print(temp.data,end="->")
            temp=temp.next

            if temp == self.head:
                break

        print("back to haed")
