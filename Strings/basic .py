def prints(s):
    vowels = "aeiou"

    for ch in s:
        if ch.lower() in vowels:
            print(f"{ch} is a vowel")
        else:
            print(f"{ch} is not a vowel")

s = "AKASH"
prints(s)