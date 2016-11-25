import sys
import re
import pprint

def yoyoyo(s="Something definitely went south"):
    print(s)
    print("Syntax: prog6.py file1 file2")

def main():
    try:
        print("File 1 is {} and File 2 is {}".format(sys.argv[1],sys.argv[2]))
        f1=open(sys.argv[1],'r')
        f2=open(sys.argv[2],'r')
        f1w=set(re.findall(r"[\w']+",f1.read().lower()))
        f2w=set(re.findall(r"[\w']+",f2.read().lower()))
        onlyf1w=f1w.difference(f2w)
        onlyf2w=f2w.difference(f1w)
        print("All the words contained in both files:\n{}".format(f1w.union(f2w)))
        print("Words the are in both files:\n{}".format(f1w.intersection(f2w)))
        print("Words only in the first file:\n{}".format(onlyf1w))
        print("Words only in the second file:\n{}".format(onlyf2w))
        print("Words not in both files:{}".format(onlyf1w.union(onlyf2w)))
    except Exception as e:
        yoyoyo(str(e))

if __name__=="__main__":
    main()