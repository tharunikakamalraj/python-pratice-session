x=90
def siva():
    x=100
    print(x)
siva() #localvariable
print(x)   #gobalvariable
#return
def siva(a,b):
    sum=a+b
    sub=a-b
    mult=a*b
    div=a/b
    return sum,sub,mult,div
s,t,r,v=siva(100,90)
print("sum=",s)
print("sub=",t)
print("mult=",r)
print("div=",v)

    