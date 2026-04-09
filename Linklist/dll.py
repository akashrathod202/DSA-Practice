class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class doublyll:
      def __init__(self):
           self.head=None
    
      def inseration__attheend(self,data):
           temp=Node(data)

           if self.head  is None:
                self.head=temp
                return
            
           
           t=self.head
           while t.next is not None:
               t.next= temp
           t.next=t
           temp.prev=t


      def printall(self):
           temp=self.head

           while temp is not None:
                print(temp.data)
                temp=temp.next 
        


obj=doublyll()
obj.inseration__attheend(10)
obj.printall()
           

