t1 = ("THARUNIKA",7,8)
t2 = ("AIML")
print(t1)
print(t2)
print(type(t1))
print(type(t2))
print(t1[1])
print(t1[0:3:2])
t3 = "THARUNIKA","DIVYA","SIVA",1,2,3
print(tuple(t3))
s,t,u,v,w,x=t3
print(s)
print(t)
print(u)
print(v)
print(w)
print(x)
r,*p,e=t3
print(r)
print(*p)
print(e)
num=[1,2,8,9,7,10,5,8,6]
t4=tuple(num)
print(t4)
print(len(t4))
print(min(t4))
print(max(t4))
print(sum(t4))
print(t4.index(10))
print(t4.count(8))


