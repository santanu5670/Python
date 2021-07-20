# n=input()
# lst1=list(n)
# print(lst1)
# lst2 = [x.upper() for x in lst1]
# count=0
# print(lst2)
# for i in range(0,len(lst2)):
#     if lst2[i]=='A' or lst2[i]=='E' or lst2[i]=='I' or lst2[i]=='O' or lst2[i]=='':
#         count=count+1
# print(count)

n=input()
count=0;n1=n.lower()
print(n1)
for i in n1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print(count)

