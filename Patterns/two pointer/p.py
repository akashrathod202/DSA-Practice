arr = [-1, 0, 1, 2, -1, -4]
target = 0

n = len(arr)
my_set = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == target:
                temp = [arr[i], arr[j], arr[k]]  # Use a list
                temp.sort()                      # Lists can be sorted
                my_set.add(tuple(temp))          # Convert to tuple for the set

result = [list(ans) for ans in my_set]
print(result)