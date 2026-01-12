a = ["a","b","c","d"]

print(a)

a[0] = "x"

print(a)

a.insert(0,"m")

print(a)

a.append("last")

print(a)

b = ["another","list"]

a.extend(b)

print(a)


a.remove("last")
print(a)


a.pop()
print(a)


a.pop(0)
print(a)

del a[0]
print(a)


a.clear()
print(a)

del a
