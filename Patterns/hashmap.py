
# def frequency_count(arr):
#     freq={}

#     for i in arr:
#         freq[i]=freq.get(i,0)+1

#     return freq

# a=[]
# print(frequency_count(a))
         


# two sum



def two_sum(arr,target):
    hashmap={}

    for i in range(len(arr)):
        complement=target-arr[i]

        if complement in hashmap:
            return[hashmap[complement],i]
        hashmap[arr[i]]=i

        
a=[2,4,6,8]
k=10
print(two_sum(a,k))


