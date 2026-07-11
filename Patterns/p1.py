# # def slidingwinodw(arr,k):
# #     window_sum=sum(arr[:k])
# #     max_sum=window_sum

# #     for i  in range(k,len(arr)):
# #         window_sum+=arr[i]-arr[i-k]
# #         max_sum=max(max_sum,window_sum)
# #     return window_sum / k



# # arr=[1,2,5,34,64,]
# # k=4
# # print(slidingwinodw(arr,3))





# # def slidingwind(arr,k):
# #     window_sum=sum(arr[:k])
# #     ans=window_sum

# #     #this is the manula window 

# #     for i in range(k,len(arr)):
# #         window_sum+=arr[i]
# #         window_sum-=arr[i-k]
# #         ans=max(ans,window_sum)

# #     return ans / k

# # arr=[1,2,34,5,3,5,3,]
# # k=3
# # print(slidingwind(arr,k))



# # def max_vowels(s,k):
# #     vowels="aeiou"
# #     count =0

# #     for i in range(k):
# #        if s[i] in vowels:
# #              count +1
# #     max_count=count

# #     for i in range(k,len(s)):
# #         if s[i] in vowels:
# #             count+1

# #         if s[i-k] in vowels:
# #            count -=1
    
# #            max_count =(max_count,count)

# #     return max_count




# # longest substring without reapating character

# # def check(s):
# #     charset=set()
# #     left=0
# #     maxelen=0

# #     for right in range(len(s)):
# #          while s[right] in charset:
# #             charset.remove(s[left])
# #             left+=1
# #          s.add(s[right])



# # frequency  count


# def show(arr):
#     dict={}
#     for i in arr:
#         if i in dict:
#              arr[i]+=1
#         else:
#            dict[i]=1

#     return dict
    
# arr=[1,2,3,4,12,3,2,2,4,3]
# print(show(arr))
       
        
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlylinkedlist:
    def __init__(self):   # ✅ FIXED HERE
        self.head = None

    def inseration_atstart(self, value):
        temp = node(value)
        temp.next = self.head
        self.head = temp

    def inseration_atend(self,value):
        new_node=node(value)

        if self.head == None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def inserationatmid(self,value,loc):
        new_node=node(value)

        if self.head == None:
            print("list")
            return
        temp=self.head

        while temp.next is not None:
            if temp.data == loc:
                new_node.next=temp.next
                temp.next=new_node
                return
            temp=temp.next

    def deletea(self,value):
          

          if self.head == None:
              print("empty")
              return
          if self.head == value:
              self.head=self.head.next
              
          temp=self.head
          prev=None

          while temp is not None:
              if temp.data == value:
                  prev.next=temp.next
                  return
              else:
                  prev=temp
                  temp=temp.next 
         
    


    
    def printall(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
         
obj = singlylinkedlist()
obj.inseration_atstart(10)
obj.inseration_atstart(4)
obj.inseration_atend(89)
obj.inserationatmid(4,10)
obj.printall()
        
