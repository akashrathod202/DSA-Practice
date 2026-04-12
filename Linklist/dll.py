class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class doublyll:
      def __init__(self):
           self.head=None
    
      def insert_atend(self,data):
           temp=Node(data)

           if self.head  is None:
                self.head=temp
                return
            
           
           t=self.head
           while t.next is not None:
                    t=t.next
           t.next=temp
           temp.prev=t

      def insert_atstart(self,data):
           temp=Node(data)

           if self.head is  None:
                self.head=temp
                return
 
           temp.next=self.head
           self.head.prev=temp
           self.head=temp

      def insert_atmid(self,data,x):
           new_node=Node(data)

           if self.head is None:
                print("list is empty")
                return
           
           t=self.head

           while t is not None:
                if t.data == x:
                    new_node.next=t.next
                    t.next.prev=new_node
                    t.next=new_node
                    new_node.prev=t
                t=t.next
                     
 

           
           
      def printall(self):
           temp=self.head

           if temp is None:
             print("List is empty")
             return

           while temp is not None:
                print(temp.data,end="<->")
                temp=temp.next 
           print("None")
        


obj=doublyll()
obj.insert_atend(10)
obj.insert_atend(20)
obj.insert_atend(30)
obj.insert_atstart(5)
obj.insert_atmid(50,20)
obj.printall()
           

