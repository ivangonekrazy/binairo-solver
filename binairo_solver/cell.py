from enum import Enum
from typing import Iterable, Iterator, Optional


class CellState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

    @classmethod
    def from_str(cls, s: str) -> "CellState":
        if s.casefold() == "B".casefold():
            return cls.BLACK
        elif s.casefold() == "W".casefold():
            return cls.WHITE
        elif s == "_":
            return cls.EMPTY
        else:
            raise ValueError(f"Invalid cell state: {s}")


CELL_STATE_GLYPH_MAP = {
    "_": CellState.EMPTY,
    "*": CellState.BLACK,
    "o": CellState.WHITE,
    CellState.EMPTY: "_",
    CellState.BLACK: "*",
    CellState.WHITE: "o",
}


class Cell:
    def __init__(self, state: Optional[CellState] = None) -> None:
        if state is not None:
            self.state = state
        else:
            self.clear()

    def clear(self) -> None:
        self.state = CellState.EMPTY

    def set(self, state: CellState) -> None:
        self.state = state

    def set_black(self) -> None:
        self.set(CellState.BLACK)

    def set_white(self) -> None:
        self.set(CellState.WHITE)

    def is_empty(self) -> bool:
        return self.state == CellState.EMPTY

    def set_opposite(self, state: CellState) -> None:
        if state == CellState.BLACK:
            self.set_white()
        elif state == CellState.WHITE:
            self.set_black()

    def flip(self) -> None:
        if self.state == CellState.BLACK:
            self.state = CellState.WHITE
        elif self.state == CellState.WHITE:
            self.state = CellState.BLACK

    def __str__(self) -> str:
        return CELL_STATE_GLYPH_MAP.get(self.state, "?")


class CellVector:
    def __init__(self, cells: Iterable[Cell]) -> None:
        self.cells = list(cells)

    def __iter__(self) -> Iterator[Cell]:
        return iter(self.cells)

    def __len__(self) -> int:
        return len(self.cells)

    def __eq__(self, other: "CellVector") -> bool:
        if len(self) != len(other):
            return False

        for a, b in zip(self.cells, other.cells):
            if a.state != b.state:
                return False

        return True

    def __str__(self) -> str:
        return "".join(str(cell) for cell in self.cells)

    @classmethod
    def from_states(cls, states: Iterable[CellState]) -> "CellVector":
        return cls([Cell(state) for state in states])

    def fill_empty(self, state: CellState) -> int:
        filled = 0
        for cell in self.cells:
            if cell.is_empty():
                cell.set(state)
                filled += 1
        return filled

    def is_filled(self) -> bool:
        return all(not cell.is_empty() for cell in self.cells)

    def count_state(self, state: CellState) -> int:
        return sum(1 for cell in self.cells if cell.state == state)

    def count_empty(self) -> CellState:
        return self.count_state(CellState.EMPTY)

    def count_white(self) -> CellState:
        return self.count_state(CellState.WHITE)

    def count_black(self) -> CellState:
        return self.count_state(CellState.BLACK)

    def n_grams(self, n: int) -> Iterator[Cell]:
        for i in range(len(self.cells) - n + 1):
            yield self.cells[i : i + n]

    def n_grams_reversed(self, n: int) -> Iterator[Cell]:
        for i in range(len(self.cells) - n, -1, -1):
            yield self.cells[i : i + n][::-1]
