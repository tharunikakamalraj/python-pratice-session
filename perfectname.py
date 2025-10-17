Number=int(input("Enter a number:"))
sum=0
for i in range(1,Number):
    if (Number%i==0):
        sum+=i
print(sum)
if(sum==Number):
    print("It is a perfect number")
else:
    print("It is not a perfect number")