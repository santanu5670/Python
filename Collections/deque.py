from collections import deque
a=['e','d','u','r','e','k','a']
d=deque(a)
print(d)
d.append("Python")
print(d)
d.appendleft("Java")
print(d)
d.pop()
print(d)
d.popleft()
print(d)
print(d.count('d'))
d.extend('opps')
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
