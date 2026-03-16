def slidingwinodw(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i  in range(k,len(arr)):
        window_sum+=arr[i]-arr[i-k]
        max_sum=max(max_sum,window_sum)
    return window_sum



arr=[1,2,5,34,64,]
k=4
print(slidingwinodw(arr,3))