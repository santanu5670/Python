numbers=list()
def countPrimeNumbers(numbers): 
    numbers1=list()
    flag=0
    for i in range(0,len(numbers)):
        # if numbers[i]==2:
        #     numbers1.append(numbers[i])
        if numbers[i]>2:
            for j in range(2,numbers[i]):
                if(numbers[i]%j==0):
                    flag=1
                    break
                else:
                    flag=0
            if flag==0:
                numbers1.append(numbers[i])
        if numbers[i]==2:
            numbers1.append(numbers[i])
    return numbers1
        # numbers1.append(numbers[i])
    # print(numbers1)

if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
    print(countPrimeNumbers(numbers))