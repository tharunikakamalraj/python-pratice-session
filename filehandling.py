# for read the file
f=open("hello.txt","r")
A=f.read()
print(A)
f.close()
#with usins
with open("hello.txt","r") as f:
    A=f.readline()#to  read the file line by line 
    B=f.readline()
    e=f.readline()
    print(A,B,e)
#write to rewrite the file 
with open("hello.txt","w") as f:
    f.write("hi divya and siva.\n")
    

    