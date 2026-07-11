# def two_sum(arr,target):
#     left=0
#     right=len(arr)-1

#     while left < right:
#         s =arr[left] + arr [right]

#         if s == target :
#             return left,right
#         elif s < target:
#             left +=1
#         else:
#             right -=1
#     return -1

# arr=[2,3,4,5,7,5,3,89,5,7]
# k=8
# print(two_sum(arr,k))



# def check_palndrome(str):
#     left=0
#     right=len( str)-1

#     while left < right:
#         if str[left] != str[right]:
#             return False
        
#         left +=1
#         right-=1
#     return True  





# s='maam'
# print(check_palndrome(s))



# palndromes

# def check_it(s):
#     s=s.replace(" ","").lower()

#     left=0
#     right=len(s)-1

#     while left < right:

#         if s[left] != s[right]:
#             return False
        
#         left +=1
#         right -=1

#     return True

# s="A man a plan canal Panama"
# print(check_it(s))



# def check_it(s):

#     left=0
#     right=len(s)-1

#     while left < right:

#         if s[left] == s[right]:
             
        
#         left +=1
#         right -=1
        
#     return True

# s=[2,3,5,3,7,8,4]
# print(check_it(s))




# remove duplicate

# def remove_duplicates(arr):
#     if len(arr)== 0:
#         return 0
#     slow =0
#     for fast in range(1, len(arr)):
#         if arr[slow] != arr[fast]:
           
#             slow+=1

#             arr[slow]=arr[fast]
#     return slow+1

# arr=[1,2,2,3,4,3,64,7,87,54]
# print(remove_duplicates(arr))


# move zeros

# def move_zeros(arr):
#     if len(arr)==0 :
#        return 0
#     left=0
#     right=len(arr)-1

#     for i in range(len(arr)):
#         if arr[left] == 0:
#             arr[right]=arr[left]

# arr=[1,2,3,0,4,6,0,9]
# print(move_zeros(arr))



# def movez(arr):
#     left=0

#     for right in range(len(arr)):
#         if arr[right] != 0:
#             arr[left], arr[right] =arr[right],arr[left]
#             left+=1
#     return arr

# arr=[0,4,3,40,34,0,34,34]
# print(movez(arr))
          

arr = [-1, 0, 1, 2, -1, -4]
target = 0

n = len(arr)
my_set = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == target:
                temp = [arr[i], arr[j], arr[k]]  # Use a list
                temp.sort()                      # Lists can be sorted
                my_set.add(tuple(temp))          # Convert to tuple for the set

result = [list(ans) for ans in my_set]
print(result)




