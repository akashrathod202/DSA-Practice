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

arr=[41,25,3,4,5,6,7]
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




            
    
    
 
