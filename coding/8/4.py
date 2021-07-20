n=int(input("Enter a number"))
def naturalsum_recursive(n):
    sum=0
    for i in range(1,n+1):
        sum=naturalsum_recursive(n-1)+n
        return sum
m=naturalsum_recursive(n)
print(m)
