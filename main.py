from tkinter import *
from tkinter.messagebox import *

# http://tkinter.fdex.eu/doc/caw.html#lignes
# http://fsincere.free.fr/isn/python/cours_python_tkinter.php#executable
# http://fr.wikibooks.org/wiki/Programmation_Python/Tkinter
# http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Utilisation_de_fen%C3%AAtres_et_de_graphismes
# http://sametmax.com/la-difference-entre-__new__-et-__init__-en-python/


def on_key(event):
    # Gestion de l'événement Appui sur une touche du clavier
    global PosX, PosY, joueur, Pion, Pionx1, Pionx2
    touche = event.keysym
    # déplacement vers le haut
    if (touche == 'Up' and PosY - 200 > 100):
        PosY -= 200
     # déplacement vers le bas
    if (touche == 'Down' and PosY + 200 < 700):
        PosY += 200
     # déplacement vers la droite
    if (touche == 'Right' and PosX + 200 < 700):
        PosX += 200
     # déplacement vers la gauche
    if (touche == 'Left' and PosX - 200 > 100):
        PosX -= 200

    # on dessine le pion à sa nouvelle position
    if (joueur == 1):
        Fen.coords(Pion, PosX-50, PosY-50, PosX+50, PosY+50)
    elif (joueur == 0):
        Fen.coords(Pionx1, PosX-50, PosY-50, PosX+50, PosY+50)
        Fen.coords(Pionx2, PosX+50, PosY-50, PosX-50, PosY+50)


def on_enter(event):
    global joueur, PosX, PosY, grille, coup, Fen, Pion, Pionx1, Pionx2
    x = int(((PosX+50)/200)-1)
    y = int(((PosY+50)/200)-1)

    if (joueur == 1 and grille[x][y] == "-"):
        print("1")
        joueur = 0
        grille[x][y] = "o"
        Fen.create_oval(PosX-75, PosY-75, PosX+75, PosY+75, width=2)
        Fen.itemconfigure(Pion, state='hidden')
        Fen.itemconfigure(Pionx1, state='normal')
        Fen.itemconfigure(Pionx2, state='normal')
        Fen.coords(Pionx1, PosX-50, PosY-50, PosX+50, PosY+50)
        Fen.coords(Pionx2, PosX+50, PosY-50, PosX-50, PosY+50)
        coup += 1
    elif (joueur == 0 and grille[x][y] == "-"):
        print("0")
        joueur = 1
        grille[x][y] = "x"
        Fen.create_line(PosX-75, PosY-75, PosX+75, PosY+75, width=2)
        Fen.create_line(PosX+75, PosY-75, PosX-75, PosY+75, width=2)
        Fen.itemconfigure(Pion, state='normal')
        Fen.itemconfigure(Pionx1, state='hidden')
        Fen.itemconfigure(Pionx2, state='hidden')
        Fen.coords(Pion, PosX-50, PosY-50, PosX+50, PosY+50)
        coup += 1

    end = is_victoire()

    print(f'0{grille[0]}')
    print(f'1{grille[1]}')
    print(f'2{grille[2]}')

    if (end != None):
        win(end)
    elif (coup == 9):
        not_win()

def is_victoire():
    global grille
    e = 0
    while (e <= 2):
        if (grille[e][0] != '-' and grille[e][0] == grille[e][1] and grille[e][1] == grille[e][2]):
            return grille[e][0]
        if (grille[0][e] != '-' and grille[0][e] == grille[1][e] and grille[1][e] == grille[2][e]):
            return grille[0][e]
        e += 1

    if (grille[0][0] != '-' and grille[0][0] == grille[1][1] and grille[1][1] == grille[2][2]):
        return grille[0][0]
    elif (grille[0][2] != '-' and grille[0][2] == grille[1][1] and grille[1][1] == grille[2][0]):
        return grille[0][2]
    return None


def win(joueur):
    global scj1, scj2
    if (joueur == "o"):
        scj1 += 1
        j1.delete(1.0, 2.10)
        j1.insert(END, "Joueur 1:\n")
        j1.insert(END, scj1)
        showinfo("Résultat", "Le joueur 1 a gagné")
    if (joueur == "x"):
        scj2 += 1
        j2.delete(1.0, 2.10)
        j2.insert(END, "Joueur 2:\n")
        j2.insert(END, scj2)
        showinfo("Résultat", "Le joueur 2 a gagné")
    main_loop()
    Mafenetre.quit()


def not_win():
    showinfo("Résultat", "Aucun joueur n'a gagné")
    main_loop()


def main_loop():
    global grille, coup, PosX, PosY, Fen
    grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    coup = 1
    PosX = 350
    PosY = 350
    Fen.destroy()
    Fen = Canvas(Mafenetre, width=700, height=720, bg='white')
    Fen.pack(side=LEFT)
    # Fen.create_rectangle(0,0,1280,720,fill='white')
    # Tableau Vertical
    Fen.create_line(50, 50, 50, 650, fill='black', width=1)
    Fen.create_line(250, 50, 250, 650, fill='black', width=1)
    Fen.create_line(450, 50, 450, 650, fill='black', width=1)
    Fen.create_line(650, 50, 650, 650, fill='black', width=1)

    # Tableau Horizontal
    Fen.create_line(50, 50, 650, 50, fill='black', width=1)
    Fen.create_line(50, 250, 650, 250, fill='black', width=1)
    Fen.create_line(50, 450, 650, 450, fill='black', width=1)
    Fen.create_line(50, 650, 650, 650, fill='black', width=1)


"""def Fin():
  """
#  Score J1 & 2
scj1 = 0
scj2 = 0

grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
joueur = 1
coup = 1

# Position initiale du pion
PosX = 350
PosY = 350

# Création d'un widget Canvas (zone graphique)
Largeur = 1280
Hauteur = 720

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('OXO')

Fen = Canvas(Mafenetre, width=700, height=720, bg='white')

# Tableau Vertical
Fen.create_line(50, 50, 50, 650, fill='black', width=1)
Fen.create_line(250, 50, 250, 650, fill='black', width=1)
Fen.create_line(450, 50, 450, 650, fill='black', width=1)
Fen.create_line(650, 50, 650, 650, fill='black', width=1)

# Tableau Horizontal
Fen.create_line(50, 50, 650, 50, fill='black', width=1)
Fen.create_line(50, 250, 650, 250, fill='black', width=1)
Fen.create_line(50, 450, 650, 450, fill='black', width=1)
Fen.create_line(50, 650, 650, 650, fill='black', width=1)
# O
Pion = Fen.create_oval(PosX-50, PosY-50, PosX+50, PosY+50, width=2)
# X
Pionx1 = Fen.create_line(PosX-50, PosY-50, PosX+50,
                         PosY+50, width=2, state='hidden')
Pionx2 = Fen.create_line(PosX+50, PosY-50, PosX-50,
                         PosY+50, width=2, state='hidden')

j2 = Text(Mafenetre, width=10, height=2)
j2.pack(side=RIGHT)
j2.insert(END, "Joueur 2:\n")
j2.insert(END, scj2)

j1 = Text(Mafenetre, width=10, height=2)
j1.pack(side=RIGHT)
j1.insert(END, "Joueur 1:\n")
j1.insert(END, scj1)

Fen.focus_set()
Fen.bind('<Key>', on_key)
Fen.bind('<Return>', on_enter)
Fen.pack(padx=5, pady=5)


# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Fin du Game', command=Mafenetre.destroy).pack(
    side=BOTTOM, padx=5, pady=5)

Mafenetre.mainloop()
