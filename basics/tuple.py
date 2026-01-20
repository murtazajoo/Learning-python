a = ("a","b","c","d")
y = ("another")
print(a)


#change
x = list(a)
x[0] = "first"
a= tuple(x)
print(a)
#add

x.append("last")


a = tuple(x)

print(a)



#remove
x.remove("c")
a = tuple(x)

print(a)


#pop
x.pop()
a = tuple(x)

print(a)


#delete

del a
#print(a)

