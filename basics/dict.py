d = dict(name="suhbaib", age=2)

dd = {
    "name":"safan",
    "age":22
}

print(d)
print(dd)


print(d["name"])
print(dd.get("name"))


print(d.keys())
print(dd.values())


d["name"] = "update"

print(d)

dd["extra"] = "new element"

print(dd)

dd.pop("extra")
print(dd)


dd.popitem()
print(dd)

dd.clear()
print(dd)





