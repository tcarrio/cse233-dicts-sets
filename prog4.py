# Author: Tom Carrio
# Course: CSE-233

import re

with open('4.txt','r') as f:
    words=re.findall(r"[\w']+",f.read())
    unique=set(words)
    print("There are {} words total, {} of which are unique".format(
        len(words),len(unique)
    ))