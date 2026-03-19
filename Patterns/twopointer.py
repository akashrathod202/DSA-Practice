def two_sum(arr,target):
    left=0
    right=len(arr)-1

    while left < right:
        s =arr[left] + arr [right]

        if s == target :
            return left,right
        elif s < target:
            left +=1
        else:
            right -=1
    return -1

arr=[2,3,4,5,7,5,3,89,5,7]
k=8
print(two_sum(arr,k))