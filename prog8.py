import pickle
import sys
import os
import pprint # debugging dicts

picklejar="test/addr_book.obj"
addrbook={}

def get_options(context="main"):
    return contexts.get(context,"Unknown context- Press q to quit")

def context_save():
    global addrbook
    #lets go pickle some contacts
    try:
        addr_file=open(picklejar,'wb')
        pickle.dump(addrbook,addr_file)
        addr_file.close()
        print("Addressbook has been saved to disk!")
    except IOError as e:
        gtfo("Could not store the addressbook at {}/{}".format(
            os.getcwd(),picklejar
        ))

def context_load():
    global addrbook
    #opening up that pickle jar now
    try:
        addr_file=open(picklejar,'rb')
        addrbook=pickle.load(addr_file)
        addr_file.close()
    except FileNotFoundError as fnfe:
        print("Could not find the addressbook at {}/{}".format(
            os.getcwd(),picklejar
        ))
    except IOError as ioe:
        print("Unknown IO error loading addressbook")

def context_main():
    global addrbook
    uin=input("""
    1: Print addressbook
    2: Add/update contact
    3: Delete contact
    4: Load addressbook
    5: Save addressbook

""")
    if(uin=="1"):
        context_print()
    elif(uin=="2"):
        context_update()
    elif(uin=="3"):
        context_delete()
    elif(uin=="4"):
        context_load()
    elif(uin=="5"):
        context_save()
    elif(uin=="q"):
        gtfo("Thanks for using the Address Book!")

def gtfo(exitstr="It's been fun guys"):
    sys.exit(exitstr)

def context_print():
    global addrbook
    print("The contents of the address book are the following:\n")
    print("="*51)
    print("{:<18}|{:<32}".format("Name","Email Address"))
    print("="*51)
    for k,v in addrbook.items():
        print("{:<18}|{:<32}".format(k,v))
    print("="*51)

def context_delete():
    global addrbook

    userkey=input("Who would you like to remove? ")
    try:
        addrbook.pop(userkey)
    except KeyError as ke:
        print("User {} not found".format(userkey))
    if(input("Would you like delete another? [y,N]").lower()=="y"):
        context_delete()


def context_update():
    global addrbook
    print("Who would you like to add?")
    tname=input("Enter their name: ").strip()
    temail=input("Enter their email: ").strip()
    continue_flag=False
    try:
        print("This entry exists as:\n{:<18}|{:<32}".format(
            tname, addrbook[tname]
        ))
        continue_flag=bool(input("Would you like to overwrite this entry? [y/N]",
            end="").lower()=='y')
    except KeyError as ke:
        continue_flag=True
    if(continue_flag):
        addrbook[tname]=temail
        print("Address book has been updated!")

    if(input("Would you like update another? [y,N]").lower()=="y"):
        context_update()

def main():
    global addrbook
    print("""Welcome to the address book!
[You may quit at any time by inputting Q]""")
    user_input=""
    while(True):
        context_main()

if __name__ == "__main__":
    main()
