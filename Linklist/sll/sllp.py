# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Sll:
#     def __init__(self):
#        self.head=None
    
#     def insert(self, value):
#         newnode = Node(value)


#         if self.head == None:
#            self.head=newnode
#            return
         

#         newnode.next = self.head   # ✅ link
#         self.head = newnode 

#     def count(self):
#             count=0

#             t=self.head

#             while t is not None:  
#                 count+=1
#                 t=t.next
#             print( "the node count is",count) 

#     def search_for(self,x):
#         temp=self.head
#         pos=0

#         while temp is not None:
#             if temp.data == x:
#                 return pos
#             temp=temp.next
#             pos+=1
#         return -1
               
#     def reverse(self):
#         prev=None
#         curr=self.head


#         while curr is not None:
#             next=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next
#         self.head=prev



        

#     def printall(self):
#         temp=self.head

#         while temp is not None:
#             print(temp.data)
#             temp=temp.next

# obj=Sll()
# obj.insert(6)
# obj.insert(8)
# obj.insert(10)
# obj.count()
# obj.search_for(10)
# obj.reverse()
# obj.printall()




# class Solution:
#     def deleteMiddle(self, head, x):
        
#         # Case 1: Empty list
#         if head is None:
#             return None
        
#         # Case 2: If head itself is to be deleted
#         if head.data == x:
#             return head.next
        
#         temp = head
        
#         # Traverse to find the node before the one to delete
#         while temp.next is not None:
#             if temp.next.data == x:
#                 temp.next = temp.next.next
#                 return head
            
#             temp = temp.next
        
#         return head   # if value not found

''







# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class sll:
#     def __init__(self):
#         self.head = None

#     def array(self, arr):
#         if len(arr) == 0:
#             return None
        
#         self.head = Node(arr[0])
#         temp = self.head

#         for i in range(1, len(arr)):
#             newnode = Node(arr[i])
#             temp.next = newnode
#             temp = newnode

#     def rearrangeEvenOdd(self):
#         if self.head is None:
#             return

#         odd_head = None
#         odd_tail = None
#         even_head = None
#         even_tail = None

#         temp = self.head

#         while temp is not None:
#             next_node = temp.next   # store next

#             if temp.data % 2 != 0:   # odd
#                 if odd_head is None:
#                     odd_head = temp
#                     odd_tail = temp
#                 else:
#                     odd_tail.next = temp
#                     odd_tail = temp
#             else:   # even
#                 if even_head is None:
#                     even_head = temp
#                     even_tail = temp
#                 else:
#                     even_tail.next = temp
#                     even_tail = temp

#             temp = next_node

#         # connect lists
#         if odd_tail is not None:
#             odd_tail.next = even_head

#         if even_tail is not None:
#             even_tail.next = None

#         self.head = odd_head if odd_head is not None else even_head

#     def printall(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end="->")
#             temp = temp.next
#         print("null")


# # Driver code
# obj = sll()
# arr = [1, 2, 3, 4, 5, 6, 7]

# obj.array(arr)
# obj.rearrangeEvenOdd()
# obj.printall()







# fast and slow pointer  find the middle

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class sll:
#     def __init__(self):
#         self.head=None

#     def inset_at_end(self,value):
#         newnode=Node(value)

#         if self.head == None:
#             self.head=newnode
#             return
        
#         temp=self.head

#         while temp.next != None:
#             temp=temp.next
        
#         temp.next=newnode

#         # finding the middle useing the slow and fast pointe

#     def find_mid(self):

#         slow=self.head
#         fast=self.head


#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next

#         return slow



#     def print(self):
#         if self.head == None:
#             return
        
#         t=self.head

#         while t != None:
#             print(t.data,end="->")
#             t=t.next

# obj=sll()
# obj.inset_at_end(1)
# obj.inset_at_end(2)
# obj.inset_at_end(3)
# obj.inset_at_end(4)
# obj.inset_at_end(5)
# obj.inset_at_end(6)
# obj.inset_at_end(7)
# obj.print()

# middle=obj.find_mid()
# print("middle element is :",middle.data)
        
            




# question of cycle detect

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def inset_at_end(self,value):
        newnode=Node(value)

        if self.head == None:
            self.head=newnode
            return
        
        temp=self.head

        while temp.next != None:
            temp=temp.next
        
        temp.next=newnode

        # finding the middle useing the slow and fast pointe

    def find_mid(self):

        slow=self.head
        fast=self.head


        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        
       
        return slow


    def has_cycle(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True
            
        return False


    def print(self):
        if self.head == None:
            return
        
        t=self.head

        while t != None:
            print(t.data,end="->")
            t=t.next

obj = sll()
obj.inset_at_end(1)
obj.inset_at_end(2)
obj.inset_at_end(3)
obj.inset_at_end(4)
obj.inset_at_end(5)

obj.print()

middle = obj.find_mid()
print("middle element is:", middle.data)

print("Cycle present:", obj.has_cycle())