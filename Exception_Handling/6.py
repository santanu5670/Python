try:
    f=open('Sample.txt')
    if f.name=='Sample.txt':
        raise FileNotFoundError
except:
    print("ok")