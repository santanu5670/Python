a={1,2,4,5,1}
print(a)
b={} #it creats not creates a empty set its create a empty dictionary
print(type(b))

c=set() #it;s create a empty set
print(type(c))
print(c)
c.add(4)
print(c)
c.add(5)
print(c)
a.add(6)
print(a)

'''c.add([1,2,3]) # we can not add lsit in a set because we can change the contant of list
print(c)'''

c.add((1,2,3)) #we can add touple into a set
print(c)

'''c.add({1:3}) #we can not add dictionary into a set
print(c)'''

print(len(c))

c.remove(5)
print(c)

c.pop()
print(c)

d={4,5,6}
e={6,7}
f=d.union(e)
print(f)

g=d.intersection({5,6,9})
print(g)



