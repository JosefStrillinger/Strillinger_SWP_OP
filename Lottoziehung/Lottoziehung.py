import random

def init_list(min, max):
    #list_draws.extend(range(1,46))
    list_draws = []
    for i in range(min,max+1):
        list_draws.append(i)
    return list_draws

def init_dict(min, max):
    dict_stat = {}
    for i in range(min,max+1):
        dict_stat[i]=0
    return dict_stat

def lottoziehung(number_picks):
    allowed_draws = list_draws[:]
    draws_done = []
    for i in range(number_picks):
        gez_zahl = random.choice(allowed_draws)
        allowed_draws.remove(gez_zahl)
        draws_done.append(gez_zahl)
        dict_stat[gez_zahl]+=1
    return draws_done

def lottoziehung_statistik(number_picks, draws):
    for i in range(draws):
        lottoziehung(number_picks)
    print(dict_stat)

def lottoziehung_gut_programmiert(min, max, number_picks):
    #done_draws = []
    for i in range(number_picks):
        gez_index = random.randrange(0, max-min-1)      
        last_pos = len(list_draws)-1-i
        list_draws[last_pos], list_draws[gez_index] = \
            list_draws[gez_index], list_draws[last_pos]
    return list_draws[-number_picks:]
               
def lottoziehung_statistik_gut_programmiert(min, max, number_picks, draws):
    for i in range(draws):
        for i in lottoziehung_gut_programmiert(min, max, number_picks):
            dict_stat[i] += 1
    print(dict_stat)

#Ein guter Programmierer programmiert, das so, dass es dynamisch ist
#man soll nur ein paar variablen ändern müssen
if __name__ == '__main__':
       
    min = 10
    max = 20
    number_picks = 6
    
    list_draws = init_list(min, max)
    dict_stat = init_dict(min, max)

    count = input("Bitte geben Sie die Anzahl der Ziehungen ein: ")
    print(count + " Ziehungen")
    lottoziehung_statistik_gut_programmiert(min, max, number_picks, int(count))# gut programmiert ==> Rubner approved
    #lottoziehung_statistik(number_picks, int(count))
    print(sorted(dict_stat.values()))
    print(sorted(dict_stat.keys()))