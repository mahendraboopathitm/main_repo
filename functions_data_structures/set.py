a={1,2,3,4,5,5}
print(a)
b={4,5,6,7,8,9}
print("unoin",a|b)
print("intersection",a&b)
print(a.difference(b))
print(a.symmetric_difference(b))
# a.add(9)
# print(a)
a.update(["mango","banana"])
print("kh",a)
a.remove("banana")
a.discard("kiwi")
print(2 in a)
for i in b:
    print(i)

