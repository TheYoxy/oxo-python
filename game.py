from copy import deepcopy
from tkinter import BOTTOM, END, HIDDEN, NORMAL, TOP, Button, Canvas, Text, Tk
from tkinter.messagebox import showinfo
from typing import List

from constants import CELL_CENTER_OFFSET, CELL_SIZE, EMPTY_CELL, EMPTY_GRID, PLAYER_1, PLAYER_2
from func import cross_position, draw_cells, draw_cross_position, draw_round_position, round_position


class Game(object):
    grid = deepcopy(EMPTY_GRID)
    current_player = 0
    turn = 1
    scores = [0, 0]
    position = [1, 1]

    def __init__(self, main_window: Tk) -> None:
        self._main_window = main_window
        self.create_canvas()
        self.players_texts = [Text(main_window, width=15, height=2),
                              Text(main_window, width=15, height=2)]

        self._end_button = Button(
            self._main_window, text='Fin du Game', command=main_window.destroy)
        self._end_button.pack(side=BOTTOM, padx=5, pady=5)

        for i in reversed(range(len(self.players_texts))):
            self.players_texts[i].pack(side=BOTTOM)
        self.write_scores()

        self.create_players()

    def create_canvas(self):
        self._canvas = Canvas(self._main_window, width=700,
                              height=720, bg='white')
        self._canvas.pack(padx=5, pady=5, side=TOP)
        self._canvas.focus_set()

        self._canvas.bind('<Key>', lambda event: self.on_key(event), add=True)
        self._canvas.bind('<Return>', lambda event: self.on_enter(), add=True)

        draw_cells(self._canvas)

    def create_players(self):
        pos = self.canvas_position
        self.players = [
            self._canvas.create_line(*cross_position(*pos),
                                     width=1,
                                     fill='black',
                                     state=NORMAL if self.current_player == 0 else HIDDEN),
            self._canvas.create_oval(*round_position(*pos),
                                     width=1,
                                     outline='black',
                                     state=NORMAL if self.current_player == 1 else HIDDEN)]

    def write_scores(self):
        for i in range(len(self.players_texts)):
            text = self.players_texts[i]
            text.delete('1.0', END)
            text.insert('1.0', f'Player {i + 1}: {self.scores[i]}')

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
        self._canvas.coords(self.current_element, *self.draw_position)

    def update_position(self, key: str):
        if (key == 'Up' and self.y > 0):
            self.y -= 1
        if (key == 'Down' and self.y < 2):
            self.y += 1
        if (key == 'Right' and self.x < 2):
            self.x += 1
        if (key == 'Left' and self.x > 0):
            self.x -= 1

    def next_turn(self):
        self._canvas.itemconfig(
            self.players[self.current_player], state=HIDDEN)

        if (self.current_player == 0):
            self.grid[self.x][self.y] = PLAYER_1
            self._canvas.create_line(*draw_cross_position(*self.canvas_position),
                                     width=2, fill='black', state=NORMAL)

            self.current_player = 1
        elif (self.current_player == 1):
            self.grid[self.x][self.y] = PLAYER_2
            self._canvas.create_oval(*draw_round_position(*self.canvas_position),
                                     width=2, outline='black', state=NORMAL)

            self.current_player = 0
        self._canvas.itemconfig(
            self.players[self.current_player], state=NORMAL)

        self.move_current_player()
        self.turn += 1

    def is_win(self) -> str | None:
        for e in range(0, 2):
            if (self.grid[e][0] != EMPTY_CELL and self.grid[e][0] == self.grid[e][1] and self.grid[e][1] == self.grid[e][2]):
                return self.grid[e][0]
            if (self.grid[0][e] != EMPTY_CELL and self.grid[0][e] == self.grid[1][e] and self.grid[1][e] == self.grid[2][e]):
                return self.grid[0][e]

        if (self.grid[0][0] != EMPTY_CELL and self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]):
            return self.grid[0][0]

        elif (self.grid[0][2] != EMPTY_CELL and self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]):
            return self.grid[0][2]

        return None

    def on_key(self, event):
        key = event.keysym

        self.update_position(key)
        self.move_current_player()

    def on_enter(self):
        if self.grid[self.x][self.y] != EMPTY_CELL:
            return None
        self.next_turn()

        winner = self.is_win()
        if (winner is not None):
            self.win(winner)
        elif (self.turn == 9):
            self.not_win()
        else:
            return None
        self.reset_canvas()

    def win(self, winner):
        if (winner == PLAYER_2):
            self.scores[1] += 1
            showinfo("Résultat", "Le joueur 2 a gagné")
        if (winner == PLAYER_1):
            self.scores[0] += 1
            showinfo("Résultat", "Le joueur 1 a gagné")
        self.write_scores()

    def not_win(self):
        showinfo("Résultat", "Aucun joueur n'a gagné")

    def reset_canvas(self):
        self._canvas.destroy()
        # time.sleep(0.0001)
        self.create_canvas()
        self.create_players()

        self.grid = deepcopy(EMPTY_GRID)
        self.turn = 1
        self.position = [1, 1]
