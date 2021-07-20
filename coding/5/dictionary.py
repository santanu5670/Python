mydict={
    "Fast":"In a Quick Manner",
    "Santanu": "is a BCA student",
    "Marks": [1,2,4],
    "anotherdict": { 'Santanu':'Player' },
    1:2                  
}

print(mydict['Fast'])
print(mydict['Marks'])
print(mydict['anotherdict'])
print(mydict['anotherdict']['Santanu'])
mydict['Marks']=[45,48,78]
print(mydict['Marks'])

#Dictionary Methods

print(mydict.keys())
print(list(mydict.keys())) #conver the dict keys into list
print(type(mydict.keys()))
print(mydict.values())
print(mydict.items())

update_dict={
    "livesh" : "Friend",
    1:3
}
mydict.update(update_dict)
print(mydict)
mydict.update(({"Python":"Programming"}))
print(mydict)

print(mydict.get(1))
print(mydict[1])
print(mydict.get(3)) 
# 3 is not present at dictionary so it print none using .get() but print(mydict[3]) will through an error




