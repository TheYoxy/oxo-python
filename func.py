from tkinter import Canvas
from typing import List

from constants import CELL_CENTER_OFFSET, CELL_SHAPE_OFFSET, CELL_SIZE


def draw_cells(canvas: Canvas):
  cell_count = 4
  last_pos = (cell_count - 1) * CELL_SIZE + CELL_CENTER_OFFSET
  for x in range(cell_count):
    pos = x * CELL_SIZE + CELL_CENTER_OFFSET
    canvas.create_line(pos, CELL_CENTER_OFFSET,
                       pos, last_pos, fill='black', width=1)
    canvas.create_line(CELL_CENTER_OFFSET, pos, last_pos,
                       pos, fill='black', width=1)


def round_position(x: int, y: int) -> List[int]:
  return [x - CELL_CENTER_OFFSET, y - CELL_CENTER_OFFSET,
          x + CELL_CENTER_OFFSET, y + CELL_CENTER_OFFSET]


def draw_round_position(x: int, y: int) -> List[int]:
  return [x - CELL_SHAPE_OFFSET, y - CELL_SHAPE_OFFSET,
          x + CELL_SHAPE_OFFSET, y + CELL_SHAPE_OFFSET]


def cross_position(x: int, y: int) -> List[int]:
  return [x, y,
          x + CELL_CENTER_OFFSET, y - CELL_CENTER_OFFSET,
          x, y,
          x - CELL_CENTER_OFFSET, y + CELL_CENTER_OFFSET,
          x, y,
          x - CELL_CENTER_OFFSET, y - CELL_CENTER_OFFSET,
          x, y,
          x + CELL_CENTER_OFFSET, y + CELL_CENTER_OFFSET]


def draw_cross_position(x: int, y: int) -> List[int]:
  return [x, y,
          x + CELL_SHAPE_OFFSET, y - CELL_SHAPE_OFFSET,
          x, y,
          x - CELL_SHAPE_OFFSET, y + CELL_SHAPE_OFFSET,
          x, y,
          x - CELL_SHAPE_OFFSET, y - CELL_SHAPE_OFFSET,
          x, y,
          x + CELL_SHAPE_OFFSET, y + CELL_SHAPE_OFFSET]
