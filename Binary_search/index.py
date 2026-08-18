# def binary_search(arr,target):
#     left=0
#     right=len(arr)-1

#     while left <= right:
#         mid=(left + right) // 2

#         if arr[mid] == target:
#             return mid
        
#         elif arr[mid] < target:
#             left = mid + 1

#         else :
#             right=mid - 1

# arr = [2, 4, 6, 8, 10, 12, 14]

# print(binary_search(arr, 12))




# first_occurrence

# def first_occurrence(arr,target):
#     low=0
#     high=len(arr)-1
#     answer=-1


#     while  low <= high:
#         mid=(low + high) // 2

#         if arr[mid] == target:
#             answer=mid
#             high=mid-1


#         elif arr[mid] < target:
#             low=mid+1

#         else:
#             high=mid-1

#     return answer

# arr = [1, 2, 2, 2, 4, 5]
 
# print(first_occurrence(arr,2))


# # last_occurence

# def last_occurence(arr,target):
#     low=0
#     high=len(arr)-1
#     answer=-1


#     while low <= high:
#         mid=(low + high) // 2

#         if arr[mid] == target:
#             answer=mid
#             low=mid+1

#         elif arr[mid] < target:
#             low=mid+1

#         else:
#              high = mid - 1
#     return answer

             

# arr = [1, 2, 2, 2, 4, 5]
# print(last_occurence(arr,2))






# lower bound


# def lower_bound(arr,target):
#     low=0
#     high=len(arr)-1
#     answer=-1

#     while low <= high:
#         mid=(low + high) // 2

#         if arr[mid] >= target:
#             answer=mid
#             high=mid-1
        
#         elif arr[mid] < target:
#             low=mid+1
        
#         else :
#             high=mid-1
#     return answer


# arr = [1, 2, 2, 2, 4, 4, 6, 8]
# print(lower_bound(arr,4))



# uperbound


# def upper_bound(arr, target):
#     low = 0
#     high = len(arr) - 1
#     answer = -1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] > target:
#             answer = mid
#             high = mid - 1

#         else:
#             low = mid + 1

#     return answer


# arr = [1, 2, 2, 2, 4, 4, 6, 8]

# print(upper_bound(arr, 4))



# arr = [10, 20, 30, 40, 50, 60, 70]
# left=1
# right=5

# mid=left+(right-left)//2
# print(mid)


# def find_and_insert(arr,target):
#     left=0
#     right=len(arr)-1
    
#     while left <= right:
#         mid = left + (right - left) // 2
#         if arr[mid] ==target:
#             return mid
        
#         elif arr[mid] < target:
#             left=mid+1

#         else:
#             right=mid-1
#     return left

        

         


# nums = [1, 3, 5, 6]
# print(find_and_insert(nums,2))






# 







# Sqrt(x)

# num = 12

# left = 1
# right = num
# answer = 0

# while left <= right:
#     mid = (left + right) // 2

#     if mid * mid <= num:
#         answer = mid
#         left = mid + 1
#     else:
#         right = mid - 1

# print(answer)



# find peak

def peak(arr):
    left=0
    right=len(arr)-1

    while left < right:
        mid=(left + right) // 2
        
        if arr[mid] < arr[mid+1]:
            left=mid+1
        else:
            right=mid-1
    return arr[left]

n=[1, 2, 3, 4, 5, 3, 1]
print(peak(n))



        
       