import tkinter as tk
from tkinter import *
import random

score_r = 0
score_p = 0
skore_r = 0
skore_p = 0
gelijk = 0
equal = 0
options = ["Dutch", "English"] 

#antwoordscherm maken
answer_window = tk.Tk()
answer_window.geometry("400x100")
answer_window.title("JA OF NEE / YES OR NO")
clicked = StringVar()
clicked.set("Dutch") 
drop = OptionMenu( answer_window , clicked , *options ) 
drop.pack() 
#game functions
def spel_nl():
    #optie input commandos
    def schaar_input():
        global skore_p
        global skore_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "schaar"
        if keuze_p == "schaar":
            if keuze_r == "steen":
                print('Je bent verloren!')
                skore_r = skore_r + 1
                print(f"computer score: {skore_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "papier":
                print('Je bent gewonnen!')
                skore_p = skore_p + 1
                print(f"speler score: {skore_p}")
            else:
                print("end")
    def steen_input():
        global skore_p
        global skore_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "steen"
        if keuze_p == "steen":
            if keuze_r == "papier":
                print('Je bent verloren!')
                skore_r = score_r + 1
                print(f"computer score: {skore_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "schaar":
                print('Je bent gewonnen!')
                skore_p = skore_p + 1
                print(f"speler score: {skore_p}")
            else:
                print("end")
    def papier_input():
        global skore_p
        global skore_r
        global gelijk
        keuze_r = str(random.choice(["schaar", "steen", "papier"]))
        keuze_p = "papier"
        if keuze_p == "papier":
            if keuze_r == "schaar":
                print('Je bent verloren!')
                skore_r = skore_r + 1
                print(f"computer score: {skore_r}")
            elif keuze_r == keuze_p:
                print("Jullie hebben dezelfde keuze gemaakt. Niemand wint!")
                gelijk = gelijk + 1
                print(f"gelijke standen: {gelijk}")
            elif keuze_r == "steen":
                print('Je bent gewonnen!')
                skore_p = skore_p + 1
                print(f"speler score: {skore_p}")
            else:
                print("end")
    #scorebord maken


    def skorebord():
        s_t_p.destroy()
        skorebord = tk.Tk()
        skorebord.title("Scorebord")
        tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Label(text="------------------------------skores:--------------------------------").pack()
        tk.Label(text=f"Speler score: {skore_p}").pack()
        tk.Label(text=f"Computer score: {skore_r}").pack()
        tk.Label(text=f"gelijke standen: {gelijk}").pack()
        if skore_r > skore_p:
            tk.Label(text="---------------------De computer is gewonnen!--------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        elif skore_p == skore_r:
            tk.Label(text="--------------------Gelijkstand! Niemand wint!---------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        else:
            tk.Label(text="------------------------Jij bent gewonnen!-------------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Button(text="Sluiten", command=skorebord.destroy).pack()
    #vorig optie scherm verwijderen (afsluiten)
    answer_window.destroy()
    #scherm loop maken
    s_t_p = tk.Tk()
    s_t_p.wm_title("Spel")
    s_t_p.geometry("200x125")
    tk.Label(text="Schaar, Steen of papier?").pack()
    tk.Button(text="Schaar",command= schaar_input).pack()
    tk.Button(text="Steen",command= steen_input).pack()
    tk.Button(text="Papier",command= papier_input).pack()
    tk.Button(text="Einde",command= skorebord).pack()
    s_t_p.mainloop()
def game_en():
#option input commands
    def scissor_input():
        global score_p
        global score_r
        global equal
        choise_r = str(random.choice(["scissor", "stone", "paper"]))
        choise_p = "scissor"
        if choise_p == "scissor":
            if choise_r == "stone":
                print('You lost!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif choise_r == choise_p:
                print("You made the same choise. Nobody wins!")
                equal = equal + 1
                print(f"equalities: {equal}")
            elif choise_r == "paper":
                print('You won!')
                score_p = score_p + 1
                print(f"player score: {score_p}")
            else:
                print("end")
    def stone_input():
        global score_p
        global score_r
        global equal
        choise_r = str(random.choice(["scissor", "stone", "paper"]))
        choise_p = "stone"
        if choise_p == "stone":
            if choise_r == "paper":
                print('You lost!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif choise_r == choise_p:
                print("You made the same choise. Nobody wins!")
                equal = equal + 1
                print(f"equalities: {equal}")
            elif choise_r == "scissor":
                print('You won!')
                score_p = score_p + 1
                print(f"player score: {score_p}")
            else:
                print("end")
    def paper_input():
        global score_p
        global score_r
        global equal
        keuze_r = str(random.choice(["scissor", "stone", "paper"]))
        keuze_p = "paper"
        if keuze_p == "paper":
            if keuze_r == "scissor":
                print('You lost!')
                score_r = score_r + 1
                print(f"computer score: {score_r}")
            elif keuze_r == keuze_p:
                print("You made the same choise. Nobody wins!")
                equal = equal + 1
                print(f"equalities: {equal}")
            elif keuze_r == "stone":
                print('You won!')
                score_p = score_p + 1
                print(f"player score: {score_p}")
            else:
                print("end")
    #scorebord maken


    def scoreboard():
        r_p_s.destroy()
        scoreboard = tk.Tk()
        scoreboard.title("Scorebord")
        tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Label(text="------------------------------scores:--------------------------------").pack()
        tk.Label(text=f"Speler score: {score_p}").pack()
        tk.Label(text=f"Computer score: {score_r}").pack()
        tk.Label(text=f"gelijke standen: {equal}").pack()
        if score_r > score_p:
            tk.Label(text="-------------------------The computer won!------------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        elif score_p == score_r:
            tk.Label(text="---------------------It's equal, nobody wins!----------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        else:
            tk.Label(text="-----------------------------You won!------------------------------").pack()
            tk.Label(text="---------------------------------------------------------------------").pack()
        tk.Button(text="Close", command=scoreboard.destroy).pack()
    #vorig optie scherm verwijderen (afsluiten)
    answer_window.destroy()
    #scherm loop maken
    r_p_s = tk.Tk()
    r_p_s.wm_title("Game")
    r_p_s.geometry("200x125")
    tk.Label(text="Rock, paper or scissor?").pack()
    tk.Button(text="Scissor",command= scissor_input).pack()
    tk.Button(text="Stone",command= stone_input).pack()
    tk.Button(text="Paper",command= paper_input).pack()
    tk.Button(text="End",command= scoreboard).pack()
    r_p_s.mainloop()
def start():
    drop_o = clicked.get()
    if drop_o == "Dutch":
        spel_nl()
    elif drop_o == "English":
        game_en()
tk.Label(text="Wil je spelen? / Do you want to play?")
answer_button = tk.Button(text = "JA / YES", command=start).pack()
answer_button2 = tk.Button(text = "NEE / NO", command=answer_window.destroy).pack()
answer_window.mainloop()