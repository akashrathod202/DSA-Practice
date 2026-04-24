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



def removeOuterParentheses(s):
    result=''
    open_count=0

    for ch in s:
        if ch == "(" :
            if open_count > 0:
                result+=ch
            open_count+=1

        else:
            open_count-=1
            if open_count > 0:

                result +=ch

    return result
    
s='(()())'
print(removeOuterParentheses(s))


