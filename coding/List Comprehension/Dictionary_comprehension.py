dictionary={'a':45,'b':65,'A':5}
print({k.lower():dictionary.get(k.lower(),0)+dictionary.get(k.upper(),0) for k in dictionary.keys()})