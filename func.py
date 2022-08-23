from tkinter import Canvas

from constants import CELL_CENTER_OFFSET, CELL_SIZE


def draw_cells(canvas: Canvas):
  cell_count = 4
  last_pos = (cell_count - 1) * CELL_SIZE + CELL_CENTER_OFFSET
  for x in range(cell_count):
    pos = x * CELL_SIZE + CELL_CENTER_OFFSET
    canvas.create_line(pos, CELL_CENTER_OFFSET,
                       pos, last_pos, fill='black', width=1)
    canvas.create_line(CELL_CENTER_OFFSET, pos, last_pos,
                       pos, fill='black', width=1)
