a={"name":"boopathi","age":22,"pos":"intern"}
print(a)

b=dict(name="mathesh",age=22,pos="intern")
print(b)
for i,j in a.items():
    print(a[i])
for i in a:
    print(a[i])
print(a.get("age"))
a["grade"]="A"
print(a)
a["age"]=20
print(a)
print(a.pop("age"))
print(a.popitem())
print(a.keys())
print(a.values())

