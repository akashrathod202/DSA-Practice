# s='banana'
# has={}
# for ch in s:
#     if ch  not in has:
#         has[ch]=1
#     else:
#         has[ch]+=1
# print(has)

arr=[11,3,4,2,3]
seen=set()
for i in arr:
    if i in seen:
        print(i)
        break
    seen.add(i)
print(seen)
        
