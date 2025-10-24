num=input("Enter a string:")
count = 0
for char in num:
    if char.lower() in "auiou":
        count+=1
print("Number of vowel:",count)