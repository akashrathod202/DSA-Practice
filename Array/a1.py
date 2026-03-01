# # we can't use array directly in python for that we have 2 ways:
# # 1 through Module
# # 2 through numpy

# import array as arr
# from array import *  


# val =arr.array('i',[1,2,3,4,5,6,7,8,9,10])
# # for i in val:
# #     print(i)


# # copy array
# copyArray=array(val.typecode,(x for x in val))
# print(copyArray)



# # slicing
# abc=val[2:-3]
# # print(abc)

# # revers
# a=val[::-1]
# print(a)



# # array or input from user

# # arrs=array('i',[]) 
# # n= int(input("enter the number:"))

# # for i in range(0,n):
# #     arrs.append(int(input("enter the value:")))

# # print(arrs)



# # search element in array

# i=val.index(4)
# print(i)


# #remove element from array
# val.remove(4)
# print(val)

# #remove element from array using pop
# val.pop()
# print(val)


# from numpy import *

# if we are using numpy to create array so there is not need to give type code
# we also create hetrogenous array using the numpy


# remember to learn what is timespace
# from numpy import *

# val = linspace(10, 20, 11)
# print(val)



# #second way is arrange
# val =arange(10,20,2)
# print(val) 


# both linspace and arrange are used to create array
# syantax of linspace is: linspace(start,stop,number of elements)
# it includes stop value
# it gives number of values between start and stop

#syantax of arrange is:arrange(start,stop,step)
# it does not include stop value
# it give step size


# “Give me 11 numbers between 10 and 20” → use linspace()

# “Start from 10 and keep adding 2” → use arange()





# to create the array of zero we use zeros

val=zeros(5)
print(val)


# to create the array of one we use ones

val=ones(5)
print(val)


# if we have to create array of any another number for that we use full

val=full(5,7)
print(val)