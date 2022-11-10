import random
import time
import pdb

researched_precentages = [0.00015, 0.00135, 0.02, 0.14, 0.20, 0.39, 2.11, 4.75, 42.25, 50.2]

#Funktion zur Ermittlung des Kartentyps
def get_card_type(cards):
    card_types = []
    for i in cards:
        card_types.append(i%13)
    return card_types

# Funktion zur Ermittlung der Kartenfarbe
def get_card_color(cards):
    card_colors = []
    for i in cards:
        card_colors.append(i//13)
    return card_colors
 
# Kartenziehen
def draw_cards(count):
    drawn = []
    for i in range(count):
        card = random.randint(0, 51)
        while card in drawn:
           card = random.randint(0, 51)
        drawn.append(card)
    return drawn

# Statistik generieren
def generate_statistic():
    stats = {"Royal Flush":0, 
             "Straight Flush":0, 
             "Four of a kind":0, 
             "Full House":0, #
             "Flush":0, 
             "Straight":0, 
             "Three of a kind":0, 
             "Two Pair":0, 
             "One Pair":0, 
             "High Card":0}
    return stats

# Gibt Elemente zurück, die nicht zum max der jeweiligen liste gehört ==> verwendet um zweites pair zu finden
def get_list_without_max(list):
    another_pair = []
    for x in list:
        if x != max(list, key=list.count):
            another_pair.append(x)
    return another_pair
    
# Kombinationen der Hand ermitteln
def calculate_hand_combinations(drawn_types, drawn_colors):
    max_color_count = drawn_colors.count(max(drawn_colors, key=drawn_colors.count))
    max_type_count = drawn_types.count(max(drawn_types, key=drawn_types.count))
    
    drawn_types.sort()
    #breakpoint() ==> interessant
    if max_color_count == 5:
        if list(range(8,12+1)) == drawn_types:
            statistic["Royal Flush"] += 1
            return #Royal Flush
        drawn_types.sort()
        if drawn_types[len(drawn_types)-1] - 4 == drawn_types[0]:
            statistic["Straight Flush"] += 1
            return # Straight Flush
        statistic["Flush"] += 1
        return # Flush
    
    if max_type_count == 4:
        statistic["Four of a kind"] += 1
        return # Four of a kind
     
    if max_type_count >= 3:
        not_max_list = get_list_without_max(drawn_types)
        if not_max_list.count(max(not_max_list, key=not_max_list.count)) == 2:
            statistic["Full House"] += 1
            return # Full House
        statistic["Three of a kind"] += 1
        return # Three of a kind
    
    if max_type_count >= 2:
        not_max_list = get_list_without_max(drawn_types)
        if not_max_list.count(max(not_max_list, key=not_max_list.count)) == 2:
            statistic["Two Pair"] += 1
            return # Two Pair
        statistic["One Pair"] += 1
        return # One Pair
        
    drawn_types.sort()
    if drawn_types[len(drawn_types)-1] - 4 == drawn_types[0]:
        statistic["Straight"] += 1
        return # Straight
    statistic["High Card"] += 1
    return # High Card
    
# Ein Durchgang ==> Ziehen, Typ und Farbe ermitteln und Kombinationen ermitteln            
def runthrough():
    drawn = draw_cards(5)
    colors = get_card_color(drawn)
    types = get_card_type(drawn)
    calculate_hand_combinations(types, colors)

def main():
    time_1 = time.time()
    print("Print the desired number of tries: ")
    tries = int(input())
    #tries = 100000    
    for i in range(tries):
        runthrough()
    print(statistic)
    print("---------------------------------------------------------------------")
    precentages = []
    for j in statistic.values():
        precentages.append(j/tries*100)
    x = 0
    for i in statistic:
        print(i+": "+str(round(precentages[x], 5))+" %"+"\t | "+"Researched: "+str(researched_precentages[x])+" %")
        x += 1
    print("Execution Time: " + str(time.time() - time_1) + " s")

if __name__ == '__main__':
    statistic = generate_statistic()
    main()