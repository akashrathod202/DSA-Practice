s='banana'
has={}
for ch in s:
    if ch  not in has:
        has[ch]=1
    else:
        has[ch]+=1
print(has)