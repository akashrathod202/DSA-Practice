# # Maximum Sum Subarray of Size K (Sliding Window)
# def max_subarry(arr,k):
#     window_sum=sum(arr[:k])
#     max_sum=window_sum

#     for  i in range(k,len(arr)):
#         window_sum+=arr[i]-arr[i-k]
#         max_sum=max(max_sum,window_sum)
#     return max_sum

# arr=[2,1,5,1,3,2]
# print(max_subarry(arr,3))


# def prifix_sum(arr):
#     prifix=[0]*len(arr)
#     prifix[0]=arr[0]
#     for i in range(len(arr)):
#          prifix[i]=prifix[i-1]+arr[i]
#     return prifix
# arr=[2,4,1,6,3]
# print(prifix_sum(arr))



