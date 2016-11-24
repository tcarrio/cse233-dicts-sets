# Author: Tom Carrio
# Course: CSE-233

import sys

def setup_files():
    if(len(sys.argv)==4):
        infile=sys.argv[2]
        outfile=sys.argv[3]
        return infile,outfile
    else:
        fail_message("Not the correct number of args")
        return

def setup_ciphers():
    letter='A'
    cipher=list(set([c for c in "4ybdddifk&C!r1Nm6w6uuZK@Qc^5h%8Z3o$myCU6l!loGWdPK&EQzIVEC!".upper()]))
    encCipher={}
    for i in range(26):
        encCipher[letter]=cipher[i]
        letter=chr(ord(letter)+1)
    decCipher={v:k for k,v in encCipher.items()}
    return (encCipher,decCipher)

def do_the_thing(cipher,readfile,writefile):
    f=open(readfile,'r')
    o=open(writefile,'w')
    for c in f.read().upper():
        o.write(cipher.get(c,c))
    f.close()
    o.close()

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
        fail_message()
        return
    try:
        infile,outfile=setup_files()
        do_the_thing(this_cipher,infile,outfile)
    except Exception as e:
        fail_message("Failed in using files, {}".format(str(e)))
        return

if __name__ == "__main__":
    main()