# Author: Tom Carrio
# Course: CSE-233

import sys
import pprint

def setup_files():
    if(len(sys.argv)==4):
        infile=sys.argv[2]
        outfile=sys.argv[3]
        return infile,outfile
    else:
        fail_message("Not the correct number of args")
        return

def setup_ciphers():
    tmp_cipher=[c for c in "lpDzQ2FEnOJXCHAPc8Rb16j5i3LogGBU7Im0V9duYsyTa4KSxveh"]
    encCipher={}
    decCipher={}
    for letter,offset in {'a':0,'A':26}.items():
        for i in range(26):
            encCipher[letter]=tmp_cipher[i+offset]
            decCipher[tmp_cipher[i+offset]]=letter
            letter=chr(ord(letter)+1)
    encCipher['__type']="encrypt"
    decCipher['__type']="decrypt"
    return (encCipher,decCipher)

def do_the_thing(cipher,readfile,writefile):
    f=open(readfile,'r')
    o=open(writefile,'w')
    fin=f.read()
    print("File in:\n{}".format(fin))
    for c in fin:
        o.write(cipher.get(c,c))
    f.close()
    o.close()
    with open(writefile,'r') as fout:
        print("File out:\n{}".format(fout.read()))

def fail_message(msg=""):
    print("You have input functionality that is not supported")
    print("Error: {}".format(msg))
    print("""The syntax to this command is:
    python 3.py [encrypt/decrypt] fileIn fileOut""")

def main():
    if(sys.argv[1]=='encrypt'):
        this_cipher=setup_ciphers()[0]
    elif(sys.argv[1]=='decrypt'):
        this_cipher=setup_ciphers()[1]
    else:
        fail_message("Not a valid option")
        return
    try:
        print("The cipher type in use is '{}''".format(this_cipher['__type']))
        infile,outfile=setup_files()
        do_the_thing(this_cipher,infile,outfile)
    except Exception as e:
        fail_message("Failed in using files, {}".format(str(e)))
        return

if __name__ == "__main__":
    main()