n=int(input("Enter a number:"))
st=str(n)
sum=0
pow=len(st)
for i in st:
    sum += int(i) ** pow
print(sum)
if(sum==n):
    print("It is a AIMSTRONG number")
else:
    print("It is not a AIMSTRONG number")