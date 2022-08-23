from tkinter import *
from tkinter.messagebox import *
from func import draw_cells
import constants
from game import Game


# http://tkinter.fdex.eu/doc/caw.html#lignes
# http://fsincere.free.fr/isn/python/cours_python_tkinter.php#executable
# http://fr.wikibooks.org/wiki/Programmation_Python/Tkinter
# http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Utilisation_de_fen%C3%AAtres_et_de_graphismes
# http://sametmax.com/la-difference-entre-__new__-et-__init__-en-python/


def on_key(event):
    # Gestion de l'événement Appui sur une touche du clavier
    global curr_x, curr_y, joueur, Pion, Pionx1, Pionx2
    touche = event.keysym
    # déplacement vers le haut
    if (touche == 'Up' and curr_y - constants.CELL_SIZE > 100):
        curr_y -= constants.CELL_SIZE
     # déplacement vers le bas
    if (touche == 'Down' and curr_y + constants.CELL_SIZE < 700):
        curr_y += constants.CELL_SIZE
     # déplacement vers la droite
    if (touche == 'Right' and curr_x + constants.CELL_SIZE < 700):
        curr_x += constants.CELL_SIZE
     # déplacement vers la gauche
    if (touche == 'Left' and curr_x - constants.CELL_SIZE > 100):
        curr_x -= constants.CELL_SIZE

    # on dessine le pion à sa nouvelle position
    if (joueur == 1):
        window.coords(Pion, curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x+constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)
    elif (joueur == 0):
        window.coords(Pionx1, curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x+constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)
        window.coords(Pionx2, curr_x+constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x-constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)


def on_enter(event):
    global joueur, curr_x, curr_y, grille, coup, window, Pion, Pionx1, Pionx2
    x = int(((curr_x+constants.CELL_CENTER_OFFSET)/constants.CELL_SIZE)-1)
    y = int(((curr_y+constants.CELL_CENTER_OFFSET)/constants.CELL_SIZE)-1)

    if (joueur == 1 and grille[y][x] == "-"):
        joueur = 0
        grille[y][x] = "o"
        window.create_oval(curr_x-constants.CELL_SHAPE_OFFSET, curr_y-constants.CELL_SHAPE_OFFSET,
                           curr_x+constants.CELL_SHAPE_OFFSET, curr_y+constants.CELL_SHAPE_OFFSET, width=2)
        window.coords(Pionx1, curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x+constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)
        window.coords(Pionx2, curr_x+constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x-constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)
        coup += 1
    elif (joueur == 0 and grille[y][x] == "-"):
        joueur = 1
        grille[y][x] = "x"
        window.create_line(curr_x-constants.CELL_SHAPE_OFFSET, curr_y-constants.CELL_SHAPE_OFFSET,
                           curr_x+constants.CELL_SHAPE_OFFSET, curr_y+constants.CELL_SHAPE_OFFSET, width=2)
        window.create_line(curr_x+constants.CELL_SHAPE_OFFSET, curr_y-constants.CELL_SHAPE_OFFSET,
                           curr_x-constants.CELL_SHAPE_OFFSET, curr_y+75, width=2)
        window.coords(Pion, curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                      curr_x+constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET)
        coup += 1

    end = is_win()

    

    print(f'0{grille[0]}')
    print(f'1{grille[1]}')
    print(f'2{grille[2]}')

    if (end != None):
        win(end)
    elif (coup == 9):
        not_win()


def is_win():
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
        player1_text.delete(1.0, 2.10)
        player1_text.insert(END, "Joueur 1:\n")
        player1_text.insert(END, scj1)
        showinfo("Résultat", "Le joueur 1 a gagné")
    if (joueur == "x"):
        scj2 += 1
        player2_text.delete(1.0, 2.10)
        player2_text.insert(END, "Joueur 2:\n")
        player2_text.insert(END, scj2)
        showinfo("Résultat", "Le joueur 2 a gagné")
    reset_window()


def not_win():
    showinfo("Résultat", "Aucun joueur n'a gagné")
    reset_window()


def reset_window():
    global grille, coup, curr_x, curr_y, window
    grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    coup = 1
    curr_x = 350
    curr_y = 350

    window.destroy()
    window = Canvas(main_window, width=700, height=720, bg='white')
    window.pack(side=LEFT)

    draw_cells(window)


#  Score J1 & 2
scj1 = 0
scj2 = 0

grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
joueur = 1
coup = 1

# Position initiale du pion
curr_x = 350
curr_y = 350

# Création d'un widget Canvas (zone graphique)
width = 1280
height = 720

# Création de la fenêtre principale
main_window = Tk()
main_window.title('OXO')

window = Canvas(main_window, width=700, height=720, bg='white')

draw_cells(window)

# O
Pion = window.create_oval(curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET,
                          curr_x+constants.CELL_CENTER_OFFSET, curr_y+constants.CELL_CENTER_OFFSET, width=2)
# X
Pionx1 = window.create_line(curr_x-constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET, curr_x+constants.CELL_CENTER_OFFSET,
                            curr_y+constants.CELL_CENTER_OFFSET, width=2)
Pionx2 = window.create_line(curr_x+constants.CELL_CENTER_OFFSET, curr_y-constants.CELL_CENTER_OFFSET, curr_x-constants.CELL_CENTER_OFFSET,
                            curr_y+constants.CELL_CENTER_OFFSET, width=2)

player2_text = Text(main_window, width=10, height=2)
player2_text.pack(side=RIGHT)
player2_text.insert(END, "Joueur 2:\n")
player2_text.insert(END, scj2)

player1_text = Text(main_window, width=10, height=2)
player1_text.pack(side=RIGHT)
player1_text.insert(END, "Joueur 1:\n")
player1_text.insert(END, scj1)

window.focus_set()
window.event_add('<<arrow>>', '')
window.bind('<Key>', on_key)
window.bind('<Return>', on_enter)
window.pack(padx=5, pady=5)


game = Game()


# Création d'un widget Button (bouton Quitter)
Button(main_window, text='Fin du Game', command=main_window.destroy).pack(
    side=BOTTOM, padx=5, pady=5)

main_window.mainloop()
