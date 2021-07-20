import re
if(re.search('inform','We need to imform him about latest information')):
    print("This is a latest inform")

allinform=re.findall('inform', 'we need to infrom him Otherwise anyone can infrom him')

for i in allinform:
    print(i)