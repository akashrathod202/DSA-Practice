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
                     

     #  def deletelall(self,value):
           
          #  if self.head is None:
          #       print("List is empty")
          #       return
           
          #  t=self.head

          #  if self.head.data == value
          #       self.head=t.next
          #       self.head.prev=None
          #       return   
          #  while t is not None:
          #       if t.data == value:
          #            t.prev.next=t.next
          #            t.next.prev=t.prev
          #            return
          #  if t.data== value:
          #       t.prev.next=None
          #  t=t.next
                
      def deleteat_start(self):
           if self.head == None:
                print("this list is empty")
                return
           if self.head.next is None:
                self.head=None
                return
           self.head=self.head.next 
           self.head.prev=None


      def deleteat_at_end(self):
           if self.head is None:
                print("list is empty")

           t=self.head

           if self.head == None:
                self.head=None
                return
           
           while t.next is not None:
                t=t.next
           t.prev.next=None


      def deleate_at_mid(self,value):
          if self.head is None:
             print("list is empty")
             return

          t=self.head

          if t.data == value:
              if t.next is not None:
                 self.head = t.next
                 self.head.prev = None
              else:
            # only one node
                self.head = None
              return


          while t is not None:
               if t.data== value:

                 if t.next is not None:
                      t.prev.next=t.next
                      t.next.prev=t.prev

                 else:
                      t.prev.next=None

                 return
               t=t.next
          print("value not found")

                
      
           
           
      def printall(self):
           temp=self.head

           if temp is None:
             print("List is empty")
             return

           while temp is not None:
                print(temp.data,end="<->")
                temp=temp.next 
           print("None")
      def rev_display(self):
        if self.head is None:
           print("List is empty")
           return

        temp = self.head

        while temp.next is not None:
           temp = temp.next

        while temp is not None:
            print(temp.data, end="<->")
            temp = temp.prev

        print("None")


obj=doublyll()
obj.insert_atend(10)
obj.insert_atend(20)
obj.insert_atend(30)
obj.insert_atstart(5)
obj.insert_atmid(50,20)
obj.deleteat_at_end()
obj.deleate_at_mid(20)
obj.deleteat_start()
obj.printall()
obj.rev_display()
           

