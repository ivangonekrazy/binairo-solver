from binairo_solver.board import Board, CellVector
from binairo_solver.cell import CellState
from binairo_solver.strategy import ALL_STRATEGIES


class Solver:

    def __init__(self, board: Board):
        self.board = board

    def solve(self) -> Board:
        # TODO: this is recursively instantiating a Solver object.
        # We should refactor this into a function to avoid the overhead
        # and improve the ergonomics of the code.

        self.fill_using_strategies()

        if self.board.is_filled() and self.board.meets_constraints():
            return self.board

        _board = self.board.clone()
        next(_board.empty_cells()).set(CellState.BLACK)
        if _board.meets_constraints():
            return Solver(_board).solve()

        _board = self.board.clone()
        next(_board.empty_cells()).set(CellState.WHITE)
        if _board.meets_constraints():
            return Solver(_board).solve()

    def fill_using_strategies(self) -> int:
        board_states: set[str] = set()
        total_changes = 0
        iterations = 0

        while not self.board.is_filled():
            board_state = hash(str(self.board))

            if board_state in board_states:
                # we've reached a state we've seen before and our strategies
                # are not making any changes, so we'll exit the loop
                break

            board_states.add(board_state)

            changed = 0
            for row_cellvector in self.board.rows():
                changed += self.solve_cellvector(row_cellvector)
            for col_cellvector in self.board.columns():
                changed += self.solve_cellvector(col_cellvector)

            iterations += 1
            total_changes += changed

        return total_changes

    def solve_cellvector(self, cellvector: CellVector) -> int:
        count = 0

        for strategy in ALL_STRATEGIES:
            count += strategy(cellvector)

        return count
