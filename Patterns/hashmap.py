
# def frequency_count(arr):
#     freq={}

#     for i in arr:
#         freq[i]=freq.get(i,0)+1

#     return freq

# a=[]
# print(frequency_count(a))
         


# two sum



# def two_sum(arr,target):
#     hashmap={}

#     for i in range(len(arr)):
#         complement=target-arr[i]

#         if complement in hashmap:
#             return[hashmap[complement],i]
#         hashmap[arr[i]]=i


# a=[2,4,6,8]
# k=10
# print(two_sum(a,k))




# def show_dubli(arr):
#     freq={}
#     result={}

#     for i in range(arr):
#         freq[i]=freq.get(i,0)+1

#     for key in freq:

#         if freq[key] >1:
#             result.append(key)
#         return result
        
            



def count(a, b):
    n = min(len(a), len(b))
    hashmap={}
    count=0
    
    for i in range(n):
        hashmap[i]=hashmap.get(i,0)+1
        if i in hashmap:
            count += 1
    
    return count

a = [1,2,3,4,5,6,7,8,9,10]
b = [3,45,6,7,8,4,3,2,1]

print(count(a, b))


