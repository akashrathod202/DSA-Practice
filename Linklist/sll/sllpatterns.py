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
        
        self.tail.next=self.head.next.next.next

    
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

    def del_postions(self,postion):

        if self.head is None:
            print("list is empty")
            return
        
        if postion == 0:
            self.head=self.head.next
            return
        
        prv=None
        current=self.head
        index=0

        while current is not  None:
            if postion == index:
                prv.next=current.next
                return
                
            

            prv=current
            index+=1
            current=current.next
        print("postion doesnot exitsts")
            

    def delete_byvalue(self,value):
        if self.head is None:
            print("the list is empty")
            return
        
        current=self.head
        prev=None
        while current is not None:
            if current.data==value:
                prev.next=current.next
            
            prev=current
            current=current.next
        print("value doesnot exsits in node")

                

    def del_nthnode_fromlast(self):
        if self.head is None:
            print("list is empty ")
            return
        
        temp=self.head
        prev=None
        while temp.next is not None:
            prev=temp
            temp=temp.next
        print("we reached",temp.data)
        print("and the prev is",prev.prev.prev.data)

        # while prev.prev != self.head:
        #     prev=prev.prev
        #     print(temp.data)
        # print("we back to head",prev.data)

    def want_list(self,n):
        if self.head == None:
            print("list is empty")
            return[]
        temp=self.head
         
        list=[]
        while temp.next is not None:
            if temp.data != n:
                 list.append(temp.data)
                  
             

          
            temp=temp.next
            
                
        return list



       

    # def check_start(self):
       

    #     if self.head is None:
    #         print("the list is empty")
    #         return
    #     visted=()
    #     temp=self.head

    #     while temp:
    #         if temp in visted:
    #              return temp
            
    #         visted.add(temp)

    #         temp=temp.next
                
    #     print("we got")


    def check_start_by_slow_and_fast_pointer(self):
        if self.head is None:
            return None
        
        slow=self.head
        fast=self.head


        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if  slow ==fast:
               break
        else:
                return None
            
        slow=self.head

        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
              
             

             

        
        

 
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
ll.create_loop()
# ll.del_postions(29)
# ll.del_nthnode_fromlast()
# ll.delete_byvalue(509)
# print(ll.want_list(40))
print(ll.check_start())
# ll.display()
# print(ll.detect_cycle())

 