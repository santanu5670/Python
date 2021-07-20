from collections import namedtuple
a=namedtuple('Courses','name , technolodgy')
# s=a('Data Science','Python')
s=a._make(['AI','Python'])
print(s)