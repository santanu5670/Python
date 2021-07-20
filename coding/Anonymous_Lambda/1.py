def a_first(a):
    return a[1]
a=[[1,14],[5,6],[8,23]]
a.sort(key=a_first)
print(a)