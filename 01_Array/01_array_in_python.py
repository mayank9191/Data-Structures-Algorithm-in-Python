from array import *


a = array("i", [1, 2, 3])

print(type(a))

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i], end=" ")


a.append(4)
print(a)

a.pop()
print(a)

a.remove(1)
print(a)
