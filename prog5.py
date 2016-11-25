import re
import pprint
import sys

def complain_about_life(s="Life is just horrible"):
    print(s)
    print("Syntax: prog5.py filename")

if(len(sys.argv)==2):
    filename=sys.argv[1]
    try:
        f=open(filename,'r')
        words=re.findall(r"[\w']+",f.read().lower())
        wordcount={}
        for w in words:
            if(wordcount.get(w,-1)==-1):
                wordcount[w]=1
            else:
                wordcount[w]+=1
        pprint.pprint(wordcount)
    except FileNotFoundError as nfe:
        complain_about_life("File not found!")
else:
    complain_about_life("No file given!")