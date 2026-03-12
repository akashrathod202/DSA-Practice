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



# num =int(input("enter the number :"))
# orignal = num
# rev=0
# digit=''
# while num != 0:
#    digit = num % 10
#    rev =rev * 10 + digit
#    num = num // 10
# print(rev)
# if orignal == rev :
#    print(" this is palndrome",rev)
# else:
#    print("this is not palndrome",rev)




# armstrong 

num =153 
# temp = num
# total=0
# nod = len(str(num))
# while num != 0:
#     digit=num % 10
#     total=total + digit ** nod
#     num =num // 10
# print(total)

# if temp == total :
#     print("armstrong")
# else:
#     print("not a armstrong")


     
# num=52731
# odd=0

# while num >0:
#     d=num % 10
#     if d % 2 != 0:
#        odd = d
#        print(odd ,end='')
#     num = num // 10 
# 
# 
# 
# 
#    




# largest odd sub string in string

# # to solve this problem traverse the string from last. 
# # check the first odd num from that index to first index there will be the largest odd substring
# num="8934"
# ans=""
# for i in range(len(num)-1,-1,-1):
#     if int(num[i]) % 2 != 0:
#         ans=num[:i+1]
#         #ans = num[:3]
#         break
# print(ans)




#isomophic problem

def is_isomorphic(s, t):
    map1 = {}
    map2 = {}

    for i in range(len(s)):
        if s[i] in map1:
            if map1[s[i]] != t[i]:
                return False
        else:
            map1[s[i]] = t[i]

        if t[i] in map2:
            if map2[t[i]] != s[i]:
                return False
        else:
            map2[t[i]] = s[i]

    return True


print(is_isomorphic("egg","add"))
