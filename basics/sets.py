s = {1,2,3,4,5}

print(s)


s.add(3)
print(s)


print(len(s))

s2 = {11,22,44}

s.update(s2)
print(s)


s.remove(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)


fs = frozenset({1,2,3})
print(fs)

