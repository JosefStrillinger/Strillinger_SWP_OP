import random

list_draws = []
dict_stat = {}

def init_list():
    list_draws.extend(range(1,46))

def init_dict():
    for i in range(1,46):
        dict_stat[i]=0
    
def Lottoziehung():
    allowed_draws = list_draws[:]
    draws_done = []
    for i in range(6):
        gez_zahl = random.choice(allowed_draws)
        allowed_draws.remove(gez_zahl)
        draws_done.append(gez_zahl)
        dict_stat[gez_zahl]+=1
    return draws_done

def Lottoziehung_Statistik(draws):
    for i in range(draws):
        Lottoziehung()
    print(dict_stat)

if __name__ == '__main__':
    init_list()
    init_dict()
    a = Lottoziehung()
    print(a)
    count = input("Bitte geben Sie die Anzahl der Ziehungen ein: ")
    print(count + " Ziehungen")
    Lottoziehung_Statistik(int(count))