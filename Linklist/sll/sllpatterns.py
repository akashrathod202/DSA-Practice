class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail=new_node
            return

        current = self.head

        self.tail.next=new_node
        self.tail=new_node

    def middle(self):
        if self.head is None:
            print("list is empty")

        slow=self.head
        fast=self.head

        while fast  and fast.next:
              slow=slow.next
              fast=fast.next.next

        return slow.data

    def create_loop(self):
        if self.head is None:
            print("the list empty")
            return
        
        self.tail.next=self.head.next.next

    
    def detect_cycle(self):
        if self.head == None:
            print("list is empty")
            return
               
        
        slow=self.head
        fast=self.head
 

        while fast  and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast :
                print("cycle detect")
                return True
        
        print("not detect")
        return False


    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" → ")
            current = current.next

        print("None")


# Create linked list
ll = SinglyLinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
# print(ll.middle())
# ll.create_loop()
# ll.display()
print(ll.detect_cycle())
 