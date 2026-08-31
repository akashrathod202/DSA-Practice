def hasduplicates(s):
    s=set()

    for num in s:
        if num in s:
            return True
        s.add(num)
    return False
