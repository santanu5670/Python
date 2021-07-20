try:
    f=open('Sample.txt')
    # ab=cd
    z=10/0
except (FileNotFoundError,NameError,ZeroDivisionError): #any of this three error occour it will print the below line
    print("Error Occour")
except: #For other error it will print the below line
    print("Error")