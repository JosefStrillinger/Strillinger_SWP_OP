import random

researched_precentages = [0.00015, 0.00135, 0.02, 0.14, 0.20, 0.39, 2.11, 4.75, 42.25, 50.2]

def get_card_type(cards):
    card_types = []
    for i in cards:
        card_types.append(i%13)
    return card_types

def get_card_color(cards):
    card_colors = []
    for i in cards:
        card_colors.append(i//13)
    return card_colors
 

def draw_cards(count):
    drawn = []
    for i in range(count):
        card = random.randint(0, 51)
        while card in drawn:
           card = random.randint(0, 51)
        drawn.append(card)
    return drawn

def generate_statistic():
    stats = {"Royal Flush":0, "Straight Flush":0, "Four of a kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a kind":0, "Two Pair":0, "One Pair":0, "High Card":0}
    return stats

def calculate_hand_combinations(drawn_types, drawn_colors):
    max_color = drawn_colors.count(max(drawn_colors, key=drawn_colors.count))
    max_type = drawn_types.count(max(drawn_types, key=drawn_types.count))
    if max_color == 5:
        if list(range(8,13)) == drawn_types:
            statistic["Royal Flush"] += 1
            return
        drawn_types.sort()
        if drawn_types[-1] -4 == drawn_types[0]:
            statistic["Straight Flush"] += 1
            return
        statistic["Flush"] += 1
        return
    
    if max_type >= 2:
        if max_type >= 3:
            if max_type == 4:
                statistic["Four of a kind"] += 1
                return
            else:
                filtered_list = [x for x in drawn_types if x != max(drawn_types, key=drawn_types.count)]
                if filtered_list.count(max(filtered_list, key=filtered_list.count)) == 2:
                    statistic["Full House"] += 1
                    return
                statistic["Three of a kind"] += 1
                return
        else:
            filtered_list = [x for x in drawn_types if x != max(drawn_types, key=drawn_types.count)]
            if filtered_list.count(max(filtered_list, key=filtered_list.count)) == 2:
                statistic["Two Pair"] += 1
                return
            statistic["One Pair"] += 1
            return
        
    drawn_types.sort()
    if drawn_types[-1] - 4 == drawn_types[0]:
        statistic["Straight"] += 1
        return
    statistic["High Card"] += 1
    return
                
def runthrough():
    drawn = draw_cards(5)
    colors = get_card_color(drawn)
    types = get_card_type(drawn)
    calculate_hand_combinations(types, colors)

if __name__ == '__main__':
    tries = 100000
    statistic = generate_statistic()
    for i in range(tries):
        runthrough()
    print(statistic)
    print("---------------------------------------------------------------------")
    precentages = []
    for j in statistic.values():
        precentages.append(j/tries*100)
    x = 0
    for i in statistic:
        print(i+": "+str(precentages[x])+" %"+" | "+"Researched: "+str(researched_precentages[x])+" %")
        x += 1