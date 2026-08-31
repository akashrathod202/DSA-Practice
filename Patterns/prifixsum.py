# def prfix_sum(s):
#     prifix=[]
#     sum=0
#     for i in s:
#         sum+=i
#         prifix.append(sum)
#     return prifix
# s=[1,2,3,4]
# print(prfix_sum(s))
       


 
        

# def prfix_sum(s,k):
#     sum=0
#     psum=[]
#     for i in range(k,len(s)):
#         sum+=i
#         psum.append(sum)
#     return psum


# s=[1,2,3,4,4,3,2,5,5,]
# k=5
# print(prfix_sum(s,k))



# def subarray(nums,k):
#     count = 0
#     n=len(nums)

#     for i in range(n):
#         total = 0
#         for j in range(i,n):
#             total+=nums[j]
#             if total ==k :
#                 count +=1
#     return count






# array=[1,2,3,4,2,4,2,5,3,5,9,6,8,7,4,6,6,4]
# k=23
# print(subarray(array,k))


# def subarraySum(nums, k):
#     prefix_sum = 0
#     count = 0
#     hashmap = {0: 1}  # important (base case)
    
#     for num in nums:
#         prefix_sum += num
        
#         if (prefix_sum - k) in hashmap:
#             count += hashmap[prefix_sum - k]
        
#         hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    
#     return count



# def subarray(arr):
#     quries=[(0,2),(1,3)]
#     prifix=[0]*len(arr)
#     prifix[0]=arr[0]
     
#     for i in range(1,len(arr)):
#         prifix[i]=prifix[i-1] + arr[i]
#         result=[]
#         for i ,j in quries:
#          if i == 0:
#             result.append(prifix[j])
#         else:
#            result.append(prifix[j]-prifix[i-1])

      
#     return result
# arr = [2, 4, 1, 3]
# print(subarray(arr))



# def subarray(arr,k):
#     curr_sum=0
    
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             curr_sum+=arr[j]

#             if curr_sum == k:
#                  count+=1
#     return count
# arr= [1, 1, 1]
# k = 2
# print(subarray(arr,k))







# sum of subarray equals to k

# def subarraySum(nums, k):
#     prefix_sum = 0
#     count = 0
#     hashmap = {0: 1}
#     for num in nums:
#         prefix_sum+=num
#         if(prefix_sum - k) in hashmap:
#             count+=hashmap[prefix_sum - k]
#         hashmap[prefix_sum]=hashmap.get(prefix_sum,0)+1

#     return count


# arr=[2,3,-5,5,1,4]
# k=5
# print(subarraySum(arr,k))





# longest sub array equal 0


# def maxlen(arr):
#      n=len(arr)
#      maxlength=0   
   
#      for i in range(n):
#         currurentsum=0

#         for j in range(i,n):
#            currurentsum+=arr[j]

#            if currurentsum == 0:
#             length=j-i+1
#             maxlength=max(maxlength,length)

#      return maxlength


# arr = [1, 0, -4, 3, 1, 0]
# print(maxlen(arr))




# optimal solution
def mexlen(arr):
    prifix_sum=0
    hasmap={}
    max_length=0

    for i in range(len(arr)):
        prefix_sum+=arr[i]

        if prifix_sum==0:
            max_length = i + 1

            



 
