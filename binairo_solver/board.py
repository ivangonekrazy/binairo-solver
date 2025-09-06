# Implements the board state for Binairo

from typing import Iterator

from binairo_solver.cell import CELL_STATE_GLYPH_MAP, Cell, CellState, CellVector
from binairo_solver.constraint import ALL_CONSTRAINTS
from binairo_solver.error import BoardBoundaryError, BoardConstraintError


class Board:
    def __init__(self, size: int) -> None:
        if size % 2 != 0:
            raise BoardConstraintError("size must be even")
        self.size = size
        self.cells = [Cell() for _ in range(size * size)]

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.rows())

    def clone(self) -> "Board":
        board = Board(self.size)
        for i, cell in enumerate(self.cells):
            board.set_cell(i, cell.state)
        return board

    def set_cell(self, index: int, state: CellState) -> None:
        if index < 0 or index >= len(self.cells):
            raise BoardBoundaryError()
        self.cells[index].set(state)

    def get_row(self, row: int) -> CellVector:
        start = row * self.size
        end = start + self.size
        return CellVector(self.cells[start:end])

    def get_column(self, column: int) -> CellVector:
        return CellVector(self.cells[column :: self.size])

    def rows(self) -> Iterator[CellVector]:
        for i in range(self.size):
            yield self.get_row(i)

    def columns(self) -> Iterator[CellVector]:
        for i in range(self.size):
            yield self.get_column(i)

    def empty_cells(self) -> Iterator[Cell]:
        for cell in self.cells:
            if cell.is_empty():
                yield cell

    def is_filled(self) -> bool:
        return all(not cell.is_empty() for cell in self.cells)

    def meets_constraints(self) -> bool:
        for row in self.rows():
            for c in ALL_CONSTRAINTS:
                if not c(row):
                    return False

        for col in self.columns():
            for c in ALL_CONSTRAINTS:
                if not c(col):
                    return False

        return True

    @classmethod
    def from_text_instructions(cls, text: str) -> "Board":
        lines = iter(text.strip().split("\n"))

        size = int(next(lines).strip())
        board = cls(size)

        for line in lines:
            line = line.strip()
            idx, state = line.split(" ")
            board.set_cell(int(idx), CellState.from_str(state.strip()))

        return board

    @classmethod
    def from_text_map(cls, text: str) -> "Board":
        """this is the inverse of the __str__ method"""

        lines = [line.strip() for line in text.strip().split("\n")]

        size = len(lines[0].strip())
        board = cls(size)

        for row in range(size):
            for col in range(size):
                idx = row * size + col
                state = CELL_STATE_GLYPH_MAP.get(lines[row][col])
                board.set_cell(idx, state)

        return board
