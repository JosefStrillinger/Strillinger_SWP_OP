import random

def generate_cards():
    cards = []
    types = ["Spades", "Hearts", "Diamonds", "Clubs"]
    highs = ["Ace", "King", "Queen", "Jack"]
    for i in range(0,4):
        for j in range(2,15):
            if j > 10:
                cards.append(highs[j-11] + " " + types[i])
            else:
                cards.append(str(j) + " " + types[i])
    return cards

def draw_cards(cards):
    for i in range(1,6):
        rand = random.randint(0, len(cards)-1)
        cards[len(cards)-i], cards[rand] = cards[rand], cards[len(cards)-i]
    return cards[len(cards)-5:len(cards)]

if __name__ == '__main__':
    print(generate_cards())
    print("------------------------------------------")   
    print(draw_cards(generate_cards()))     