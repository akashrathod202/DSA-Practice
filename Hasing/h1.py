# s='banana'
# has={}
# for ch in s:
#     if ch  not in has:
#         has[ch]=1
#     else:
#         has[ch]+=1
# print(has)


# arr=[11,3,4,2,3]
# seen=set()
# for i in arr:
#     if i in seen:
#         print(i)
#         break
#     seen.add(i)
# print(seen)


# two_sum
 


def two_pointer(nums,target):
    seen={}
    for i,num in enumerate(nums):
        compliment=target-num
        if compliment in seen:
            return [seen[compliment],i]
        seen[num]=i
    

    

arr=[2,7,4,8,34]
print(two_pointer(arr,9))

        
