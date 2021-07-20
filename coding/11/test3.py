#!/bin/python3

# import math
# import os
# import random
# import re
# import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:
    s=0
    p=0
    def __init__(self,roll,name,marks_list,count):
        self.roll=roll
        self.name=name
        self.marks=marks_list
        self.count=count
    def calculate_percentage(self):
        s=sum(marks)
        self.p=s//count
        return self.p
    def find_grade(self):
        # return self.p
        if self.p>=80:
            return 'A'
        elif self.p>=60 and self.p<80:
            return 'B'
        elif self.p>=40 and self.p<60:
            return 'C'
        else:
            return 'F'
if __name__ == '__main__':
    roll=int(input())
    name=input()
    count=int(input())
    marks=[]
    for i in range(count):
        marks.append(int(input()))
    s=Student(roll,name,marks,count)
    print(s.calculate_percentage())
    print(s.find_grade())