list_1=[1,2,3,15,44,45,65,66,23,33,12,54]
div_by_3=list()
for items in list_1:
    if items%3==0:
        div_by_3.append(items)
print("Without Using List Comprehension",div_by_3)
print("With Using List Comprehension",[items for items in list_1 if items%3==0])