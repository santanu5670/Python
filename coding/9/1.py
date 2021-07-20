with open('E:\Python(6th sem)\coding\9\Poems.txt') as f:
    a=f.read()
print(a)
# b=a.find('Twinkle')
# print(b)
if 'Twinkle' in a:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()
