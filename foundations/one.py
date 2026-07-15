# arr = [1,2,3,3,3,4,3,2,1,6,4,53,4]

# freq = {}

# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# large = 0
# element = None

# for key, value in freq.items():
#     if value > large:
#         large = value
#         element = key

# print("Element:", element)
# print("Frequency:", large)

# def check(arr,k):
#      for i in range(0,len(arr)):
#         if arr[i] == k:
#           return i,arr[i]
          
#      return -1
     
 

# arr= [5, 8, 2, 10, 6]
# print(check(arr,8))



# def count_occurrence(arr,k):
#     count=0
#     for i in range(len(arr)):
#         if arr[i] == k:
#          count+=1
#     return count
    
# arr = [2, 5, 2, 7, 2, 8]
# print(count_occurrence(arr,2))





# def first_occurence(arr,k):
#     for  i in range(0,len(arr)):
#         if k == arr[i]:
#             return i
#             break
        
#     return -1
    
# arr=[3,3,4,5,6,77,57,5,45,45]
# print (first_occurence(arr,45))



def last_occurance(arr,k):
    for i in range(len(arr)-1,-1 ,-1):
        if k == arr[i]:
         return arr[i],i
         break
    return -1
            
        
arr=[3,3,4,5,6,77,57,5,45,45]
print (last_occurance(arr,45))
        



