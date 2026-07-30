# # s='banana'
# # has={}
# # for ch in s:
# #     if ch  not in has:
# #         has[ch]=1
# #     else:
# #         has[ch]+=1
# # print(has)


# # arr=[11,3,4,2,3]
# # seen=set()
# # for i in arr:
# #     if i in seen:
# #         print(i)
# #         break
# #     seen.add(i)
# # print(seen)


# # two_sum
 


# # def two_pointer(nums,target):
# #     seen={}
# #     for i,num in enumerate(nums):
# #         compliment=target-num
# #         if compliment in seen:
# #             return [seen[compliment],i]
# #         seen[num]=i
    

    

# # arr=[2,7,4,8,34]
# # print(two_pointer(arr,9))
 
# def firstUniqChar(s):
#     freq = {}

#     # Step 1: Count the frequency of each character
#     for ch in s:
#         if ch not in freq:
#             freq[ch] = 1
#         else:
#             freq[ch] += 1

#     # Step 2: Traverse the string again to find the first unique character
#     for i, ch in enumerate(s):
#         if freq[ch] == 1:
#             return i

#     return -1


# # Example
# s = "leetcode"
# print(firstUniqChar(s))   # Output: 0

# s = "loveleetcode"
# print(firstUniqChar(s))   # Output: 2

# s = "aabb"
# print(firstUniqChar(s))   # Output: -1





        
# A = [1,2,3,4]
# B = [3,4,5,6]
# B=set(B)
# for i in A:
#    if i in B:
#       print(i)


# anagram

# def anagram(a,b):
#     s=True
    
#     if len(a) == len (b):

#         for i in a:
#            if i not in b:
#               s=False

#         if s == True :
#             print("this is angram")
#         else:
#             print("this is not an angram")
#     else:
#         print("this is not an anagram")




# def anagram(a,b):
#     if len(a)  == len(b):
#         dic={}
       
#         for i in a:
#            if i in dic:
#              dic[i]+=1
#            else:
#              dic[i]=1
    

#         dic2={}
#         for j in b:
#             if j in  dic2:
#                dic2[j]+=1
#             else:
#                dic2[j]=1

#         if dic == dic2 :
#           print("this is angrm")
#         else:
#            print("this is not angram")
   
#     else :
#         print("this not an angram")


          
# a='aaaa'
# b='aaab'
# (anagram(a,b))



# def anagram2(a,b):
#      if len(a) != len(b):
#           print("This is not an anagram")
#           return
#      dic={}
#      for ch in a:
#           if ch in dic:
#                dic[ch]+=1
#           else:
#                dic[ch]=1

#      for ch in b:
#           if ch not in dic:
#                print("this is not an angram")
#                return
#           dic[ch]-=1
    
#      for  value in dic.values():
#           if value != 0:
#                print("this is not an angram")
#                return
#      print("This is an anagram")
          



# a='aaaa'
# b='aaab'
# (anagram2(a,b))


def majorityElement(nums):
  count={}
  for ch in nums:
     if  ch in count:
        count[ch]+=1
     else:
        count[ch]=1

  for key, value in count.items():
    if value >len(nums)// 2:
       return key
     
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


