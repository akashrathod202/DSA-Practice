

# infix to postfix
# class solution:
    
#     def precdedence(self,ch):
#         if ch =="+" or ch == '-':
#             return 1
#         if ch =="*" or ch == "/":
#             return 2
        
#         if ch == "^":
#             return 3
#         return 0 
    
#     def infixtopostfix(self,s):
#         stack=[]
#         result=[]


        
#         for char in s:
#             if ("a" <= char <="z") or ('A' <= char <="Z") or("0"<= char <="9"):
#                 result.append(char)

#             elif char == "(":
#                  stack.append(char)
            
#             elif char ==")":
#                 while stack and stack [-1] !=  '(':
#                     result.append(stack.pop())
#                 stack.pop()

#             else: 
#                 while stack and self.precdedence(stack[-1]) >= self.precdedence(char):
#                     result.append(stack.pop())
#                 stack.append(char)
            

#         while stack:
#             result.append(stack.pop())
#         return "".join(result)
    



# obj=solution()
# obj.precdedence("a+b*(c-d)")
# print(obj.infixtopostfix("a+b*(c-d)"))


# infix to prefix







# # infix to  prefix
# class solution:
    
#     def precdedence(self,ch):
#         if ch =="+" or ch == '-':
#             return 1
#         if ch =="*" or ch == "/":
#             return 2
        
#         if ch == "^":
#             return 3
#         return 0 
    
#     def infixtopostfix(self,s):

#         s=s[::-1]
#         temp=""
#         for ch in s:
#             if ch ==")":
#                temp+="("

#             elif ch=="(":
#                 temp+=")"

#             else:
#                  temp+=ch


#         stack=[]
#         result=[]
    

#         for char in temp :
#             if char.isalnum():
#                 result.append(char)

#             elif char == "(":
#                  stack.append(char)
            
#             elif char ==")":
#                 while stack and stack [-1] !=  '(':
#                     result.append(stack.pop())
#                 if stack:
#                    stack.pop()

#             else: 
#                 while stack and self.precdedence(stack[-1]) >= self.precdedence(char) :
                
#                     result.append(stack.pop())
#                 stack.append(char)
            

#         while stack:
#             result.append(stack.pop())
#         return "".join(result[::-1])
    



# obj=solution()
# obj.precdedence("")
# print(obj.infixtopostfix("a+b*(c-d)"))


# def reverse(s):
#     print(s)
#     s=s[::-1]
#     temp=""
#     for ch in s:
#         if ch == "(":
#             temp+=")"

#         elif ch == ")":
#             temp+="("
#         else:
#             temp +=ch
#     print(temp)

# print(reverse("a+b*(c-d)"))



# postfix to infix

class solution:
    def postfix_to_infix(self,s):
        stack=[]
        for ch in s:
            if ch.isalnum():
               stack.append(ch)
            
            else:
             op1=stack.pop()
             op2=stack.pop()
             ans=f"({op2}{ch}{op1})"

             stack.append(ans)

        return stack[-1]

        

obj=solution()
print(obj.postfix_to_infix('ab-de+f*/')
)