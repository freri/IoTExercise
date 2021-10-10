import random, json

class Card():
    def __init__(self, suit = None, value = None):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit
    def __repr__(self):
        return str(self)

class Deck():
    def __init__(self):
        self.cards = []
        self.suits = ['Hearts','Diamonds', 'Clubs', 'Spades']
        self.values= [str(i) for i in range(2,11)]
        self.values.extend(['J','Q','K'])
        self.values.insert(0,'A')
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value))
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, numberOfCards = 1):
        if numberOfCards > len(self.cards):
            print(f"Requested {numberOfCards} cards, but only {len(self.cards)} left in the deck!")
            return
        try:
            cardsToDeal =  self.cards[0:numberOfCards]
            self.cards = self.cards[numberOfCards-1:-1]  
        except:
            print("Something went wrong!")
            return       
        
        return cardsToDeal
class Contact():
    def __init__(self, name, surname, email):
        self.info = {
            "name": name,
            "surname": surname,
            "email": email
        }
        try: contacts = json.load(open("contacts.json"))
        except: contacts = []
        if self.info not in contacts:
            contacts.append(self.info)
        json.dump(contacts,open("contacts.json","w"),indent=2)

    def __str__(self):
        return "Name: " + self.info["name"] + \
         "\nSurname: " + self.info["surname"] + \
             "\nEmail: " + self.info["email"] + "."
    def __repr__(self):
        return str(self)
         

class AdressBook():
    def __init__(self):
        try: self.contacts = json.load(open("contacts.json"))
        except: self.contacts = []
    def add_contact(self, name, surname, email):
        Contact(name,surname,email)
        self.contacts = json.load(open("contacts.json"))
    def show(self):
        print("All contacts:")
        for c in self.contacts:
            print(c)
    def find_by_name(self,name):
        for c in self.contacts:
            for key,value in c.items():
                if key == "name" and value == name:
                    print(f"found contact {name}")
                    print(c)

    def remove_contact(self,name):
        remove = []
        for c in self.contacts:
            for key,value in c.items():
                if key == "name" and value == name:
                    remove.append(c)
                else:
                    pass
        for r in remove:
            self.contacts.remove(r)
        json.dump(self.contacts,open("contacts.json","w"),indent=2)
        
    def update(self,target, name, surname, email):
        for c in self.contacts:
            for key, value in c.items():
                if key == "name" and value == target:
                    print("target found")
                    c["name"] = name
                    c["surname"] = surname
                    c["email"] = email
        print(self.contacts)
        json.dump(self.contacts,open("contacts.json","w"),indent=2)



def exercise3():
    deck = Deck()
    deck.shuffle()
    myHand = deck.deal(5)
    print(myHand)

def exercise4():
    book = AdressBook()
    book.add_contact("eeridn", "zrawfei", "drraei")
    book.add_contact("Fredrik","tasf","gagag")
    book.add_contact("eerin","tfassfasf","gagagfasf")
    book.remove_contact("eerin")
    book.show()
    book.update("Fredrik", "Freic", "E", "A")
if __name__ == "__main__":
    exercise3()
    exercise4()