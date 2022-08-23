from tkinter import *
from tkinter.messagebox import *
from func import draw_cells
from game import Game


# http://tkinter.fdex.eu/doc/caw.html#lignes
# http://fsincere.free.fr/isn/python/cours_python_tkinter.php#executable
# http://fr.wikibooks.org/wiki/Programmation_Python/Tkinter
# http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Utilisation_de_fen%C3%AAtres_et_de_graphismes
# http://sametmax.com/la-difference-entre-__new__-et-__init__-en-python/


def reset_window():
    global grille, coup, curr_x, curr_y, window
    grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    coup = 1
    curr_x = 350
    curr_y = 350

    window.destroy()
    window = Canvas(main_window, width=700, height=720, bg='white')

    draw_cells(window)


if __name__ == '__main__':
    #  Score J1 & 2
    scj1 = 0
    scj2 = 0

    grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    joueur = 1
    coup = 1

    # Position initiale du pion
    curr_x = 350
    curr_y = 350

    # Création de la fenêtre principale
    main_window = Tk()
    main_window.title('OXO')

    game = Game(main_window)

    window.focus_set()

    # Création d'un widget Button (bouton Quitter)
    Button(main_window, text='Fin du Game', command=main_window.destroy).pack(
        side=BOTTOM, padx=5, pady=5)

    main_window.mainloop()
