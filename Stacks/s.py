# emplementing link list 

# class stack:
#     def __init__(self):
#         self.s= []
#         # self represent the current object (instance)

    
#     def length(self):
#         return len(self.s)

#     def push(self,value):
#         self.s.insert(0,value)

#     def peek(self):
#         if len(self.s)== 0:
#             raise Exception("Stack is empty")
#         else:
#             return self.s[0]
        
#     def pop(self):

#         if len(self.s) == 0:
#             raise Exception("Stack is")
         
#         else:
#             return self.s.pop(0)
        

     

# stk=stack()
# stk.push(10)
# stk.push(20)
# stk.push(30)

# # print(stk.peek())
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())

        
        
# emplementing using linklist
    
# class Node:
#    def __init__(self,data):
#       self.data=data
#       self.next=None

# class stack:
#    def __init__(self):
#       self.Top=None
     
    
#    def is_empty(self):
#        return self.Top is None
        
      

#    def push(self,value):
#        temp=Node(value)

#        temp.next=self.Top
#        self.Top=temp

#    def peek(self):
#        if self.is_empty():
#            raise Exception("stack is empty")
#        return self.Top.data
   
#    def pop(self):
#       if self.Top is None:
#          raise Exception("stack is empty")


#       popped=self.Top.data
#       self.Top=self.Top.next
#       return popped
   

#    def display(self):
#       temp=self.Top
#       while temp:
#           print(temp.data,end="->")
#           temp=temp.next
#       print("none")



# stk = stack()
# stk.push(10)
# stk.push(20)
# stk.push(30)

# stk.display()   # 30 -> 20 -> 10 -> None

# print(stk.pop())  # 30
# print(stk.peek()) # 20




# check the valid parenthese


def is_valid(s):
    stack=[]

    for bracket in s:
        if bracket == "[" or bracket == "{" or bracket == "(" :
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            ch=stack.pop()

            if (
                (bracket == "]" and ch == "[")
                or (bracket == "}" and ch =="{")
                or (bracket == ")" and ch == "(")
            ):
               
               continue
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False  
    


print(is_valid("()"))        # True
print(is_valid("({[]})"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False




 