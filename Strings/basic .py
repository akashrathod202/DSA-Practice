def prints(s):
    vowels = "aeiou"

    for ch in s:
        if ch.lower() in vowels:
            print(f"{ch} is a vowel")
        else:
            print(f"{ch} is not a vowel")

s = "AKASH"
prints(s)




# def palindrome(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         if arr[left] != arr[right]:
#             return False

#         left += 1
#         right -= 1

#     return True


# s = "madam"

# if palindrome(s):
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")



def remove_space(arr):
    result=[]
    for i in arr:
        if i != " ":
           result.append(i)
        
    return "".join(result)
     
arr='akash rathod'
print(remove_space(arr))
