from random import shuffle

class Card():
    def __init__(self,s,k):
        self.info={
            "suit":s,
            "kind":k
        }
        self.symbol_map={
            'clubs':'♣',
            'diamonds':'♦',
            'hearts':'♥',
            'spades':'♠'
        }

    def value(self):
        if(self.info['kind']=='A'):
            return [1,11]
        elif(self.info['kind'] in ['J','Q','K']):
            return [10]
        else:
            return [int(self.info['kind'])]

    def __str__(self):
        return ("{:>2}{}".format(self.info['kind'],self.symbol_map[self.info['suit']]))

class Deck():
    def __init__(self):
        self.cards=[]
        for s in ['clubs','diamonds','hearts','spades']:
            for k in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.cards.append(Card(s,k))
        self.in_use=[]
        self.cards_played=0

    def shuffle(self):
        for i in range(10):
            shuffle(self.cards)
        self.cards_played=0

    def get_top(self):
        top=self.cards.pop()
        self.in_use.append(top)
        self.cards_played+=1
        print("Taking one from the top")
        print("It's a {}!".format(str(top)))
        return top

    def collect(self):
        for c in self.in_use:
            self.cards.insert(0,c)
        self.in_use=[]
        if(self.cards_played>26):
            self.shuffle()

class Hand():
    def __init__(self):
        self.cards=[]

    def hit(self,c):
        self.cards.append(c)

    def get_values(self):
        values=[]
        for c in self.cards:
            if(len(values)==0):
                values=c.value()
            else:
                tvals=[]
                for cv in c.value():
                    for v in values:
                        tvals.append(cv+v)
                values=tvals
        print("{} for cards: {}\n".format(values,
            ",".join([str(c) for c in self.cards])))
        return values

    def return_hand(self):
        self.cards=[]


class Player():
    def __init__(self,n):
        self.name=n
        self.hand=Hand()
        self.loser=False

    def hit(self,c):
        self.hand.hit(c)
        self.loser=self.value()>21

    def value(self):
        return min(self.hand.get_values())

    def set_lost(self,v=True):
        self.loser=v

    def has_lost(self):
        return self.loser

    def return_cards(self):
        self.hand.return_hand()

    def get_name(self):
        return self.name

class GameMaster():
    def __init__(self,fn="Richard"):
        self.deck=Deck()
        self.deck.shuffle()
        self.players=[Player(n) for n in (fn,"Charles")]
        self.gameover=False

    def play(self):
        while not self.gameover:
            current_players=[p for p in self.players if not p.has_lost()]
            if(len(current_players)==1):
                print("Player {} has won the game!\n".format(
                    current_players[0].get_name()))
                return
            else:
                for p in current_players:
                    print("Player {} says hit!".format(p.get_name()))
                    p.hit(self.deck.get_top())
                    if(p.has_lost()):
                        break

    def reset(self):
        for p in self.players:
            p.return_cards()
            p.set_lost(False)
        self.deck.collect()
        self.gameover=False
