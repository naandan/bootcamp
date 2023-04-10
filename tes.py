import copy
a = ["a", "b", "c", "d","a", "e"]
b = copy.copy(a)
for item in a:
    if item == "a":
        print(item)
        b.remove(item)
a = copy.copy(b)
print(a)