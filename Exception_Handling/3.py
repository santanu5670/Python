try:
    f=open('Sample.txt')
    # ab=cd
    z=10/0
#Here we handle multiple exception using multiple except block
except FileNotFoundError: 
    print("File not found")
except NameError as e:
    print(e)
except Exception as f:
    print(f)
except: #use this if we not know the exception
    print("Some Error occur")