colors = {"pink","black","red"}
print(colors)
colors.add("orange")
print(colors)
colors.update(["yellow","green"])
print(colors)
colors.remove("green")
print(colors)
colors.discard("yellow")
print(colors)




#set operation
a={1,2,3,4}
b={6,9,8,7}
print(a|b)
print(a&b)
print(a-b)
print(a.difference(b))
#or print(a<b)
print(a.symmetric_difference(b))
#or print(a^b)
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
