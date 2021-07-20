text = input("Enter the text = ")
spam = False
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    pass
elif("subscribe this" in text):
    spam = True
else:
    spam = False
if(spam):
    print("Alert this text comtain spam words")
else:
    print("The text is ok")
