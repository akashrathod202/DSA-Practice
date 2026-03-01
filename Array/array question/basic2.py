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





arr=[10,20,30,40]

i=1
j=3

arr[j],arr[i] =arr[i] ,arr[j]
print(arr)
