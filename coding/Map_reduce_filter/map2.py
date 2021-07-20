# numbers=[1,2,3,4,5,6,7,8]
# num=list(map(lambda x:x**2,numbers))
# print(num)
# print(map)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(max(arr))
print(arr)
s=[]
for i in arr:
    if i<max(arr):
        s.append(i)
print(s)
print(max(s))