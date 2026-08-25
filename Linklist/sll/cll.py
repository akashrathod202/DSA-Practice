# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
         

    
# class cll:
#         def __init__(self):
#             self.head=None
        

#         def insertatstaet(self,data):
#             new_node=Node(data)

#             if self.head is None:
#                 self.head=new_node
#                 new_node.next=self.head
#                 return
            
#             temp=self.head
            
#             while temp.next !=self.head: 
#                  temp=temp.next  
#             new_node.next=self.head
#             temp.next=new_node
#             self.head=new_node
            
#         def inset_end(self,data):
#               newnode=Node(data)

#               if self.head is None:
#                  self.head=newnode
#                  newnode.next=self.head
#                  return
              
#               temp=self.head

#               while temp.next != self.head:
#                    temp=temp.next
#               temp.next=newnode
#               newnode.next=self.head
                   

             
#         def insertatmid(self,value,x):
#              newnode=Node(value)
#              if self.head ==  None:
#                   print("list is empty")
#                   return
             
           
#              temp= self.head

#              while True:
#                   if temp.data == x:
#                       newnode.next=temp.next
#                       temp.next=newnode
#                       return
                  
#                   temp=temp.next

#                   if temp == self.head:
#                        break
#              print("vlaue not found")
                
#         def deleteat_start(self):    
#              if self.head == None:
#                   print("list is empty")
#                   return
             
#             #  at start
#              if self.head.next == self.head:
#                   self.head = None
#                   return

#              temp = self.head

#              while temp.next != self.head:
#                     temp=temp.next
            
#              temp.next=self.head.next
#              self.head=self.head.next



#         def deleteat_end(self):    
#              if self.head == None:
#                   print("list is empty")
#                   return
             
#             #  at end
#              if self.head.next == self.head:
#                   self.head = None
#                   return

#              temp = self.head

#              while temp.next.next != self.head:
#                     temp=temp.next
            
#              temp.next=self.head



                       
        
#         def printall(self):
#             if self.head is None:
#               print("List is empty")
#               return
#             temp=self.head

#             while True:
#                   print(temp.data,end="-->")
#                   temp=temp.next
                  
#                   if temp==self.head:
#                        break

#             print("back to head")


# obj=cll()
# obj.insertatstaet(5)
# obj.insertatstaet(10)
# obj.insertatstaet(15)
# obj.inset_end(6)
# obj.insertatmid(45,10)
# obj.deleteat_end()
# obj.deleteat_start()
# obj.printall()
                  


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
     
class cll:
    def __init__(self):
        self.head=None
     
    def insert(self,value):
        newnode=Node(value)
        
        if self.head == None:
           self.head=newnode
           newnode.next=newnode
           return
        
        temp=self.head

        while temp.next != self.head:
              temp=temp.next
        temp.next=newnode
        newnode.next=self.head
        self.head=newnode
        

    def reverse(self):

        if self.head is None or self.head.next == self.head:
          
           return
        
        pre=None
        curr=self.head
        


        while curr !=self.head:
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next 

            if curr == self.head:
                break
            
        self.head.next=pre
            
        self.head=pre




     
     
    def printall(self):
        
        if self.head is None:
            print("List is empty")
            return
        
        temp=self.head

        while True:
             print(temp.data,end="-->")
             temp=temp.next
                  
             if temp==self.head:
               break
        print("back to head")


obj=cll()
obj.insert(6)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.printall()
obj.reverse()
 
        



        