from Blackjack import GameMaster

def main():
    print("Welcome to the game of Black Jack")
    username=input("What is your name: ")
    gm=GameMaster(username)
    prompt_str="Would you like to start a{} game of Blackjack? [y/N]"
    doplay=input(prompt_str.format(""))
    while(doplay.lower()=="y"):
        gm.play()
        doplay=input(prompt_str.format("nother"))
        gm.reset()
        print("")


if __name__=="__main__":
    main()
