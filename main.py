from tkinter import *
from tkinter.messagebox import *
from game import Game


# http://tkinter.fdex.eu/doc/caw.html#lignes
# http://fsincere.free.fr/isn/python/cours_python_tkinter.php#executable
# http://fr.wikibooks.org/wiki/Programmation_Python/Tkinter
# http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Utilisation_de_fen%C3%AAtres_et_de_graphismes
# http://sametmax.com/la-difference-entre-__new__-et-__init__-en-python/


if __name__ == '__main__':
    main_window = Tk()
    main_window.title('OXO')
    Game(main_window)
    main_window.mainloop()
