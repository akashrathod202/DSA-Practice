# def prfix_sum(s):
#     prifix=[]
#     sum=0
#     for i in s:
#         sum+=i
#         prifix.append(sum)
#     return prifix
# s=[1,2,3,4]
# print(prfix_sum(s))
       


# subarray sum equal k
# def cntSubarrays(arr, k):
#     left=0
#     sum=0
#     prifix=[]
#     for i in arr:
#         if sum == k:
#             left+=1
#         sum+=i
#         prifix.append(sum)
        
        
#     return prifix
    
# arr=[1,-1,0,1,2,-1,3]
# k=3
# print(cntSubarrays(arr,k))
        

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