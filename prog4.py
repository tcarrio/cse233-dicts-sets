# Author: Tom Carrio
# Course: CSE-233

import re
import pprint

with open('4.txt','r') as f:
    og=f.read()
    words=re.findall(r"[\w']+",og.lower())
    unique=set(words)
    # print("There are {} words total, {} of which are unique".format(
    #     len(words),len(unique)
    # ))
    # print('The original file contained:\n{}\nAnd the list of words are:\n'.format(og))
    pprint.pprint(unique)