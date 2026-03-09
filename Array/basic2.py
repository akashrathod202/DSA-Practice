# def isAnagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# print(isAnagram("listen", "silent"))


 

# arr =[1,2,0,3,0,4,5]
# pos=0

# for i in arr:
#     if i == pos:



# def move_zeros(arr):
#     j=0
#     for i in range(len(arr)):
#         if arr[i]!=0:
#             arr[j],arr[i]=arr[i],arr[j]
#             j += 1
#     return arr

# arr = [1,0,1,0,3,12]
# print(move_zeros(arr))





# arr=[10,20,30,40]

# i=1
# j=3

# arr[j],arr[i] =arr[i] ,arr[j]
# print(arr)



#linear searach

# def serach(arr,target):
#     for i in range(len(arr)):
#         if arr[i]== target:
#             return i
#     return -1
# print(serach([3,5,7,9],9))



# check the array is sorted or n
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i +1]:
#             return  False
#     return True







# checking from last
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i] < arr[i + 1]:
#             return False
#     return True


# arrs=[7,6,5,4,3,6]
# print(is_sorted(arrs))


# star pattarn

# n=5
# # for i in range(n):
# #     for j in range(n):
# #       print("*",end ='')
# #     print()



# n = 4

# for i in range(n):        # rows
#     for j in range(n-i):    # columns
#         print("*", end=" ")
#     print()







# ___________________________________________________________________

# array rotation

    # 1]  left rotate by 1

# def left_rotate(arr):
#     first=arr[0]

#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]

#     arr[len(arr)-1]=first
#     return arr

# arr =[1,2,3,4,5]
# print(left_rotate(arr))



def right_rotate(arr):
    last = arr[-1]

    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]

    arr[0]=last
    return arr

arr =[1,2,3,4,5,6]
print(right_rotate(arr))




