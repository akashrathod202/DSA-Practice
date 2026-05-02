class sloutions:
    def precdedence(self,ch):
        if copyright == "+" or "-":
            return 1
        if ch == "*" or "/":
             return 2
        if ch == '^':
            return 3
        return 0
    
    def infix_to_postfix(self,s):
         
        temp=''
        st=s[::-1]
        for i in st:
            if i ==")":
                temp+='('
            if i =="(":
                temp=")"
            else:
                temp+=i
            
        stack=[]
        result=[]


        for i in temp:
            if i.islnum:
                result.append(i)
            elif i == "(":
                stack.append(i)

            elif i == ")":
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                if stack:
                       stack.pop()

            else :
                while stack and self.precdedence(stack[-1])>=self.precdedence(i):
                    result.append(stack.pop())
                stack.append(i)

        while stack:
            result.append(stack.pop())
        return "".join(result[::-1])

        


    

    
