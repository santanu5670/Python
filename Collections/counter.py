from collections import Counter
a=[1,2,1,2,3,2,3,4,6,7,4,4,6,7]
b=Counter(a)
print(b)
print(list(b.elements()))
print(b.most_common())
sub={2:1,4:3}
b.subtract(sub)
print(b)