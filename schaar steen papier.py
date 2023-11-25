import random
score_r = 0
score_p = 0
gelijk = 0
win = 1
gelijk_p = 1
speel_nu = True

def scoreboard():
    print("---------------------------------------------------------------------")
    print("------------------------------scores:--------------------------------")
    print(f"Speler score:{score_p}")
    print(f"Computer score:{score_r}")
    print(f"gelijke standen: {gelijk}")
    if score_r > score_p:
        print("De computer is gewonnen!")
    elif score_p == score_r:
        print("Gelijkstand! Niemand wint!")
    else:
        print("Jij bent gewonnen!")
        print("---------------------------------------------------------------------")
while speel_nu:
    keuze_r = str(random.choice(["schaar", "steen", "papier"]))
    print(f"computer: {keuze_r}")
    print("Schaar steen of papier?")
    keuze_p = input("Kies: ")
    print(f"computer: {keuze_p}")
    if keuze_p == "schaar":
        if keuze_r == "steen":
            print('Je bent verloren!')
            score_r = score_r + 1
            print(score_r)
        elif keuze_r == keuze_p:
            print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
            gelijk = gelijk + 1
            print(gelijk)
        elif keuze_r == "papier":
            print('Je bent gewonnen!')
            score_p = score_p + 1
            print(score_p)
        else:
            break
    elif keuze_p == "steen":
        if keuze_r == "papier":
            print('Je bent verloren!')
            score_r = score_r + 1
        elif keuze_r == keuze_p:
            print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
            gelijk = gelijk + 1
        elif keuze_r == "schaar":
            print('Je bent gewonnen!')
            score_p = score_p + 1
        else:
            break
    elif keuze_p == "papier":
        if keuze_r == "schaar":
            print('Je bent verloren!')
            score_r = score_r + 1
        elif keuze_r == keuze_p:
            print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
            gelijk = gelijk + 1
        elif keuze_r == "steen":
            print('Je bent gewonnen!')
            score_p = score_p + 1
        else:
            break
    elif keuze_p == "einde":
        scoreboard()
        break
    if keuze_p == "":
        print("Wilt u stoppen? Ja of Nee")
        keuze_stop = input("Ja of Nee: ").lower
        if keuze_stop == "ja":
            print("See you next time!")
            break
        elif keuze_stop == 'nee':
            print("schrijf een geldige waarde op!")
            continue
speel_nu = False