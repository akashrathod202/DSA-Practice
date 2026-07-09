# for i  in range(100):
#      if  i <= 1:
#           continue
#      is_prime=True
      
#      for j in range (2,i):
#           if i % j == 0:
#               is_prime=False
#               break
#      if is_prime:
#          print(i)
         
# print("loop is finshied")


# great common diverse

# l = 12
# m = 18

# gcd = 1

# for i in range(2, min(l, m) + 1):
#     if l % i == 0 and m % i == 0:
#         gcd = i

# print("The GCD is:", gcd)


# arr=[1,2,3,4,5,6,7]
# max=arr[0]
# for i in arr:
#     if max < arr[i]:
#         max=arr[i]

# print(max)




# reversed array

# arr=[41,25,3,4,5,6,7]
# # revers_arr=arr[::-1]
# # print(revers_arr)

# left =0
# right=len(arr)-1

# while left < right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)
    


# second largest


# def senon_l(arr):
#     larger=float('-inf')
#     second=float('-inf')
    
    
#     for num in arr:
#         if num > larger:
#             second = larger
#             larger = num
#         elif num > second and num != larger:
#                 second=num
#     print(second)

# arr=[12,4,5,5,6,8,8,59,76,]
# senon_l(arr)




# def thiredlargest(arr):
#     largest=float('-inf')
#     second=float('-inf')
#     third=float('-inf')
    
#     for num in arr:
#         if  num > largest :
#             third = second
#             second = largest
#             largest = num
            
#         elif num > second and num != largest:
#              third = second
#              second = num
                
#         elif num > third and num != second and num != largest:
#             third =num
            
#     print(largest,second,third)
  
  
# arr=[12,4,5,5,6,8,8,59,76,]  
# thiredlargest(arr)



# check the array is sorrted or not

# arr=[12,4,5,5,6,8,8,59,76]
# is_sorted=True
# for i in range(1,len(arr)):
#       if arr[i] < arr[i-1]:
#           is_sorted=False
#           break
      
# if is_sorted:
#     print("array is sorted")
# else:
#     print("array is not sorted")
      
  
# ind the largest and smallest elements in an array


# def find_max(arr):
#     largest = arr[0]
#     smallest = arr[0]

#     for num in arr:
#         if num > largest:
#             largest = num
#         elif num < smallest:
#             smallest = num

#     return largest, smallest

# arr = [2, 4, 5, 69872, 5, 6, 45, 6454, 1]

# largest, smallest = find_max(arr)
# print("Largest:", largest)
# print("Smallest:", smallest)


# implement brute-force right array rotation

# def right(arr,k):
#     n=len(arr)
    
#     for i in range(k):
#         last=arr[i-1]
        
#         for i in range(n-1,0,-1):
#             arr[i]=arr[i-1]
            
        
#         arr[0]=last
#     return num
    
# num=[1,2,3,4,5]
# print(right(num,1))




# implement brute-force Left array rotation  k times

# def left_rotation(arr,k):
#     n=len(arr)
#     for i in range(k):
#         first=arr[0]
#         for i in range(1,n,1):
#             arr[i-1]=arr[i]
        
#         arr[-1]=first
#     return arr
    
# arr=[1,2,3,4,5]
# print(left_rotation(arr,1))



# checking is this a pladrome or not using two pointer


arr=[1,2,3,2,1]
left=0
right=len(arr)-1

is_palindrome=True

while left < right:
     if arr[left]  != arr[right]:
         is_palindrome=False
         break
     left+=1
     right-=1
     
if is_palindrome:
    print("this is a palindrome")
else:
    print("this not a palindrome")

   
    
    
 
