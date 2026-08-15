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


# last_occurence

def last_occurence(arr,target):
    low=0
    high=len(arr)-1
    answer=-1


    while low <= high:
        mid=(low + high) // 2

        if arr[mid] == target:
            answer=mid
            low=mid+1

        elif arr[mid] < target:
            low=mid+1

        else:
             high = mid - 1
    return answer

             

arr = [1, 2, 2, 2, 4, 5]
print(last_occurence(arr,2))




