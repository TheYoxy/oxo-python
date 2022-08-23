from tkinter import END, HIDDEN, LEFT, NORMAL, RIGHT, Canvas, Text, Tk
from tkinter.messagebox import showinfo
from typing import List

from constants import CELL_CENTER_OFFSET, CELL_SIZE
from func import cross_position, draw_cells, draw_cross_position, draw_round_position, round_position

class Game(object):
    grid = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    current_player = 0
    turn = 1
    scores = [0, 0]
    position = [1, 1]

    def __init__(self, main_window: Tk) -> None:
        self._window = Canvas(main_window, width=700, height=720, bg='white')
        draw_cells(self._window)

        self._window.bind('<Key>', lambda event: self.on_key(event), add=True)
        self._window.bind('<Return>', lambda event: self.on_enter(), add=True)
        self._window.pack(padx=5, pady=5, side=LEFT)

        pos = self.canvas_position
        self.players = [
            self._window.create_line(*cross_position(*pos),
                               width=1,
                               fill='black',
                               state=NORMAL),
            self._window.create_oval(*round_position(*pos),
                               width=1,
                               outline='black',
                               state=HIDDEN)]
        self.players_texts = [Text(main_window, width=10, height=2),
                              Text(main_window, width=10, height=2)]
        for i in range(len(self.players_texts)):
            self.players_texts[i].pack(side=RIGHT)
            self.players_texts[i].insert(END, f'Player {i}: {self.scores[i]}')

    @property
    def current_element(self):
        return self.players[self.current_player]

    @property
    def draw_position(self):
        if self.current_player == 0:
            return cross_position(*self.canvas_position)
        elif (self.current_player == 1):
            return round_position(*self.canvas_position)

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]

    @x.setter
    def x(self, value: int) -> None:
        self.position[0] = value

    @y.setter
    def y(self, value: int) -> None:
        self.position[1] = value

    @property
    def canvas_position(self) -> List[int]:
        return [*map(lambda x: int(x * CELL_SIZE + CELL_SIZE /
                                   2 + CELL_CENTER_OFFSET), self.position)]

    def move_current_player(self):
        self._window.coords(self.current_element, *self.draw_position)

    def update_position(self, key: str):
        if (key == 'Up' and self.y > 0):
            self.y -= 1
        if (key == 'Down' and self.y < 2):
            self.y += 1
        if (key == 'Right' and self.x < 2):
            self.x += 1
        if (key == 'Left' and self.x > 0):
            self.x -= 1
        print(self.position)

    def next_turn(self):
        self._window.itemconfig(
            self.players[self.current_player], state=HIDDEN)

        if (self.current_player == 0):
            self.grid[self.x][self.y] = "x"
            self._window.create_line(*draw_cross_position(*self.canvas_position),
                                     width=2, fill='black', state=NORMAL)

            self.current_player = 1
        elif (self.current_player == 1):
            self.grid[self.x][self.y] = "o"
            self._window.create_oval(*draw_round_position(*self.canvas_position),
                                     width=2, outline='black', state=NORMAL)

            self.current_player = 0
        self._window.itemconfig(
            self.players[self.current_player], state=NORMAL)

        for player in self.players:
            print(
                f'Player {player}: {self._window.itemcget(player, "state")}')
        self.move_current_player()
        self.turn += 1

    def is_win(self) -> str | None:
        for e in range(0, 2):
            if (self.grid[e][0] != '-' and self.grid[e][0] == self.grid[e][1] and self.grid[e][1] == self.grid[e][2]):
                return self.grid[e][0]
            if (self.grid[0][e] != '-' and self.grid[0][e] == self.grid[1][e] and self.grid[1][e] == self.grid[2][e]):
                return self.grid[0][e]

        if (self.grid[0][0] != '-' and self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]):
            return self.grid[0][0]

        elif (self.grid[0][2] != '-' and self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]):
            return self.grid[0][2]

        return None

    def on_key(self, event):
        key = event.keysym

        self.update_position(key)
        self.move_current_player()

    def on_enter(self):
        if self.grid[self.x][self.y] != "-":
            return None
        self.next_turn()

        for item in self.grid:
            print(item)

        winner = self.is_win()
        if (winner is not None):
            self.win(winner)
        elif (self.turn == 9):
            self.not_win()

    def win(self, winner):
        if (winner == "o"):
            self.scores[1] += 1
            # player1_text.delete(1.0, 2.10)
            # player1_text.insert(END, "Joueur 1:\n")
            # player1_text.insert(END, scj1)
            showinfo("Résultat", "Le joueur 1 a gagné")
        if (winner == "x"):
            self.scores[0] += 1
            # player2_text.delete(1.0, 2.10)
            # player2_text.insert(END, "Joueur 2:\n")
            # player2_text.insert(END, scj2)
            showinfo("Résultat", "Le joueur 2 a gagné")

    def not_win(self):
        showinfo("Résultat", "Aucun joueur n'a gagné")
