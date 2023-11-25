import tkinter as tk
from tkinter import *
import random

score_r = 0
score_p = 0
gelijk = 0

#antwoordscherm maken
antwoord_scherm = tk.Tk()
antwoord_scherm.title("JA OF NEE")
antwoord_scherm.geometry("225x75")
antwoord_info = tk.Label(text="Wil je spelen?")
antwoord_info.pack()
#spel functie maken
def spel():
    #optie input commandos
    def schaar_input():
        global score_p
        global score_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "schaar"
        if keuze_p == "schaar":
            if keuze_r == "steen":
                print('Je bent verloren!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "papier":
                print('Je bent gewonnen!')
                score_p = score_p + 1
                print(f"speler score: {score_p}")
            else:
                print("end")
    def steen_input():
        global score_p
        global score_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "steen"
        if keuze_p == "steen":
            if keuze_r == "papier":
                print('Je bent verloren!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "schaar":
                print('Je bent gewonnen!')
                score_p = score_p + 1
                print(f"speler score: {score_p}")
            else:
                print("end")
    def papier_input():
        global score_p
        global score_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "papier"
        if keuze_p == "papier":
            if keuze_r == "schaar":
                print('Je bent verloren!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "steen":
                print('Je bent gewonnen!')
                score_p = score_p + 1
                print(f"speler score: {score_p}")
            else:
                print("end")
    #scorebord maken


    def scoreboard():
        s_t_p.destroy()
        scoreboard = tk.Tk()
        scoreboard.title("Scorebord")
        tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Label(text="------------------------------scores:--------------------------------").pack()
        tk.Label(text=f"Speler score: {score_p}").pack()
        tk.Label(text=f"Computer score: {score_r}").pack()
        tk.Label(text=f"gelijke standen: {gelijk}").pack()
        if score_r > score_p:
            tk.Label(text="---------------------De computer is gewonnen!--------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        elif score_p == score_r:
            tk.Label(text="--------------------Gelijkstand! Niemand wint!---------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        else:
            tk.Label(text="------------------------Jij bent gewonnen!-------------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Button(text="Sluiten", command=scoreboard.destroy).pack()
    #vorig optie scherm verwijderen (afsluiten)
    antwoord_scherm.destroy()
    #scherm loop maken
    s_t_p = tk.Tk()
    s_t_p.wm_title("Spel")
    s_t_p.geometry("200x125")
    tk.Label(text="Schaar, Steen of papier?").pack()
    tk.Button(text="Schaar",command= schaar_input).pack()
    tk.Button(text="Steen",command= steen_input).pack()
    tk.Button(text="Papier",command= papier_input).pack()
    tk.Button(text="Einde",command= scoreboard).pack()
    s_t_p.mainloop()
antwoord_knop = tk.Button(text = "JA", command=spel)
antwoord_knop.pack()
antwoord_knop2 = tk.Button(text = "NEE", command=antwoord_scherm.destroy)
antwoord_knop2.pack()
antwoord_scherm.mainloop()