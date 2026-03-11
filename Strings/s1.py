print("hello world")

# counts the digits

# num=12345
# count=0


# while num !=0 :
#    num = num // 10
#    count  +=1
# print("number of digits",count)



# checking the string or the number is plandrom or not
# string=input("enter the string for check is it palndrome or:")
# ch=''
# for i in string:
#     ch= i + ch
# if ch == string :
#   print("this sring is palndrome",ch)
# else :
#     print("this string is not palandrome",ch)



num =int(input("enter the number :"))
orignal = num
rev=0
digit=''
while num != 0:
   digit = num % 10
   rev =rev * 10 + digit
   num = num // 10
print(rev)
if orignal == rev :
   print(" this is palndrome",rev)
else:
   print("this is not palndrome",rev)


     

