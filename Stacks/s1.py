# def reverse_string(s):
#     stack = []

#     # push all characters
#     for char in s:
#         stack.append(char)
 

#     result=[]

#     # pop all characters
#     while stack:
#         result.append(stack.pop())

#     return result


# print(reverse_string("hello"))



# def removeOuterParentheses(s):
#     result=''
#     open_count=0

#     for ch in s:
#         if ch == "(" :
#             if open_count > 0:
#                 result+=ch
#             open_count+=1

#         else:
#             open_count-=1
#             if open_count > 0:

#                 result +=ch

#     return result
    
# s='(()())'
# print(removeOuterParentheses(s))



# check is it goodstring or not


# def isGoodString(s):

#     n=len(s)

#     if  n == 1:
#         return True
    

#     for i in range(n-1):
#         diff =abs(ord(s[i]) - ord(s[i+1]))
        

#         dist=min(diff, 26-diff)

#         if dist != 1:
#               return"No"
#     return "yes"

        

# print(isGoodString("aaa"))  # NO
# print(isGoodString("cbc"))  # YES
# print(isGoodString("ab"))   # YES
# print(isGoodString("az"))


# balcnced or not

def balenced(s):
    stack=[]
    for bracket in s:
        if bracket == '(' or bracket == "{" or bracket == "[":
           stack.append(bracket)

        else:
            if len(stack)== 0:
                return False
            else:
                ch=stack.pop()
            if( bracket == ')' and ch =='(' 
            or bracket == '}' and ch =='{' or
               bracket == ']' and ch =='[' ):
                
                continue
            else:
                return False
            
    return len(stack) == 0

         

print(balenced('((){})'))