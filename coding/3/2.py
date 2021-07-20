letter='''Dear <|NAME|>
Greetings from ABC corporation. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
<|DATE|>'''
# print(letter)
name=input("Enter Candidate Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
