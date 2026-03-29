# def slidingwinodw(arr,k):
#     window_sum=sum(arr[:k])
#     max_sum=window_sum

#     for i  in range(k,len(arr)):
#         window_sum+=arr[i]-arr[i-k]
#         max_sum=max(max_sum,window_sum)
#     return window_sum / k



# arr=[1,2,5,34,64,]
# k=4
# print(slidingwinodw(arr,3))





# def slidingwind(arr,k):
#     window_sum=sum(arr[:k])
#     ans=window_sum

#     #this is the manula window 

#     for i in range(k,len(arr)):
#         window_sum+=arr[i]
#         window_sum-=arr[i-k]
#         ans=max(ans,window_sum)

#     return ans / k

# arr=[1,2,34,5,3,5,3,]
# k=3
# print(slidingwind(arr,k))



# def max_vowels(s,k):
#     vowels="aeiou"
#     count =0

#     for i in range(k):
#        if s[i] in vowels:
#              count +1
#     max_count=count

#     for i in range(k,len(s)):
#         if s[i] in vowels:
#             count+1

#         if s[i-k] in vowels:
#            count -=1
    
#            max_count =(max_count,count)

#     return max_count




# longest substring without reapating character

# def check(s):
#     charset=set()
#     left=0
#     maxelen=0

#     for right in range(len(s)):
#          while s[right] in charset:
#             charset.remove(s[left])
#             left+=1
#          s.add(s[right])



# frequency  count


def show(arr):
    dict={}
    for i in arr:
        if i in dict:
             arr[i]+=1
        else:
           dict[i]=1

    return dict
    
arr=[1,2,3,4,12,3,2,2,4,3]
print(show(arr))
       
        