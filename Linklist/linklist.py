# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head
#         while temp.next:
#             temp = temp.next

#         temp.next = new_node


# # Example usage
# ll = SinglyLinkedList()
# ll.insert_at_end(10)
# ll.insert_at_end(20)
# ll.insert_at_end(30)



# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class SinglyLinkedlist:
#     def __init__(self):
#         self.head=None


#     def insertend(self,value):
#         temp=node(value)
#         if(self.head != None):
#             t1=self.head
#             while(t1.next != None):
#                 t1=t1.next
#             t1.next=temp
#         else:
#             self.head=temp
        
#     def printll(self):
#         t1=self.head
#         while(t1.next != None):
#             print(t1.data)
#             t1=t1.next
#         print(t1.data)

# obj=SinglyLinkedlist()
# obj.insertend(10)
# obj.insertend(20)
# obj.insertend(30)
# obj.printll()


 

# optimize code


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class signly_list:
    def __init__(self):
        self.head=None


    def insert_atstart(self,value):
       temp=node(value)
       temp.next=self.head
       self.head=temp


    def insert_end(self,value):
        new_node=node(value)
        

        if self.head is None:
             self.head=new_node
             return
        
        temp =self.head
        while temp.next is not None:
            temp=temp.next
        
        temp.next=new_node

    def inserationat_mid(self,value,x ):
        temp=node(value)
        if self.head is None:
            print("list is empty")
            return
        t1=self.head

        while t1 is not None:
            if t1.data == x:
                temp.next=t1.next
                t1.next=temp
                return 
            
            t1=t1.next


# deletion

    def deletell(self,value):

        if self.head is None:
           print("List is empty")
           return
     
        if self.head.data==value:
           self.head = self.head.next
           return
        
        t1=self.head
        prev=None
 
        while t1 is not None:
            if (t1.data == value):
                prev.next=t1.next
                return
            else:
                prev=t1
                t1=t1.next


        print("Value not found")
             



    def print_list(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next

obj = signly_list()
obj.insert_atstart(5)
obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.inserationat_mid(60,10)
obj.deletell(30)
obj.print_list()



