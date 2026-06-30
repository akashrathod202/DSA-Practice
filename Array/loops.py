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

l = 12
m = 18

gcd = 1

for i in range(2, min(l, m) + 1):
    if l % i == 0 and m % i == 0:
        gcd = i

print("The GCD is:", gcd)