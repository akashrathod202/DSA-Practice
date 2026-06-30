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
# revers_arr=arr[::-1]
# print(revers_arr)

left =0
right=len(arr)-1

while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)
    

    
    
 
