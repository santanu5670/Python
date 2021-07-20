this="    He is a good boy    "
print(this)
print(this.strip()) #Strip is used to remove extra space 

def string_replace(string,word):
    newstr=string.replace(word,"")
    # return newstr.split() # it is used to convert the string word into a list
    return newstr.strip()
n=string_replace(this, "good")
print(n)