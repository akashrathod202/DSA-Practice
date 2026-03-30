# def prfix_sum(s):
#     prifix=[]
#     sum=0
#     for i in s:
#         sum+=i
#         prifix.append(sum)
#     return prifix
# s=[1,2,3,4]
# print(prfix_sum(s))
       


 
        

def prfix_sum(s,k):
    sum=0
    psum=[]
    for i in range(k,len(s)):
        sum+=i
        psum.append(sum)
    return psum


s=[1,2,3,4,4,3,2,5,5,]
k=5
print(prfix_sum(s,k))







def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    hashmap = {0: 1}  # important (base case)
    
    for num in nums:
        prefix_sum += num
        
        if (prefix_sum - k) in hashmap:
            count += hashmap[prefix_sum - k]
        
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    
    return count