lst=list()
# print(lst)
def percent():
    n = int(input("Enter how many number do you want to enter the list:"))
    f=int(input("Enter full marks="))
    print("Enter Marks:")
    for i in range(0,n):
        ele=int(input())
        lst.append(ele)
    marks = (sum(lst)/f)*100
    print("Percentage of marks = ",marks)
percent()