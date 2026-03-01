# # # reverse the arrar

# # arr=[1,2,3,4,5]
# # rev=[]

# # for i in range(len(arr)-1,-1,-1):
# #     rev.append(arr[i])

# # print(rev)


# # find maximmum in array

# arr=[1,3,43,4,34,14,4,7,65,3,6,5,24,54,5]
# max_val =arr[0]

# for num in arr:
#     if num > max_val:
#         max_val=num

# print("maximum element :", max_val)


# # find min 
# arr=[5,45,3,4,23,2,54,2]
# min_arr=arr[0]
 
# for num in arr:
#     if num < min_arr:
#         min_arr=num
# print("the minimum element",min_arr)


# # sum of elements

# num=[1,2,3,4,5,6,7,8,9,10]
# total=0

# for i in num:
#     total=total+i
# print("the sum of the elements is",total)
    

# sum of digits

# num=12345
# total=0

# while num > 0:
#     digit= num % 10
#     total=total + digit
#     num= num // 10


# reverse the digit


# num =12321
# original=num
# rev=0

# while num > 0:
#     digit=num%10
#     rev= rev * 10 + digit
#     num = num // 10

# if rev == original:
#     print("yes,plaindrome")
# else:
#     print("no, this is not palindrome")


# second largest element


# num=[1,2,3,4,5,6,7,8,9,10]
# largest=secondlargest=third=num[0]

# for i in num:
#     if i > largest:
#          third=secondlargest
#          secondlargest =largest
#          largest=i
#     elif i > secondlargest and i != largest:
#          third=secondlargest
#          secondlargest = i
#     elif  i > third and i != secondlargest :
#         third=i


# print("largest",largest)
# print("second largest:",secondlargest)
# print("third largest",third)




# remove duplicate 


# num=[1,2,3,4,5,6,7,7,8,9,10]
# real=[]

# for ch in num:
#     if ch not in real:
#         real.append(ch)
# print(real)


# for i in range(3,-1,-1):
#     print(i)



# num=[1,2,3,4,2,5,6,7,7,8,9,10]
# count=0
# for i in num:
#     if i == 2:
#         count+=1
# print(count)




    

