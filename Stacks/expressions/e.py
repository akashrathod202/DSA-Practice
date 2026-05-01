class solution:
    def precdedence(self,ch):
        if ch =="+" or ch == '-':
            return 1
        if ch =="*" or ch == "/":
            return 2
        
        if ch == "^":
            return 3
        return 0 
    
    def infixtopostfix(self,s):
        stack=[]
        result=[]

        for char in s:
            if ("a" <= char <="z") or ('A' <= char <="Z") or("0"<= char <="9"):
                result.append(char)

            elif char == "(":
                 stack.append(char)
            
            elif char ==")":
                while stack and stack [-1] !=  '(':
                    result.append(stack.pop())
                stack.pop()

            else: 
                while stack and self.precdedence(stack[-1]) >= self.precdedence(char):
                    result.append(stack.pop())
                stack.append(char)
            

        while stack:
            result.append(stack.pop())
        return "".join(result)
    



obj=solution()
obj.precdedence("a+b*(c-d)")
print(obj.infixtopostfix("a+b*(c-d)"))