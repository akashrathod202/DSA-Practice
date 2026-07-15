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

def check(arr,k):
     for i in range(0,len(arr)):
        if arr[i] == k:
          return i,arr[i]
          
     return -1
     
 

arr= [5, 8, 2, 10, 6]
print(check(arr,8))

