from binairo_solver.board import Board, CellVector
from binairo_solver.cell import CellState
from binairo_solver.strategy import ALL_STRATEGIES


def solve(board: Board) -> Board | None:
    _board = board.clone()

    apply_strategies_to_board(_board)

    if _board.is_filled():
        if _board.meets_constraints():
            return _board

        # we seem to have filled all cells, but the constraints are not met
        return None

    _board_try_black = _board.clone()
    next(_board_try_black.empty_cells()).set(CellState.BLACK)
    if not _board_try_black.is_filled():
        return solve(_board_try_black)

    _board_try_white = _board.clone()
    next(_board_try_white.empty_cells()).set(CellState.WHITE)
    if not _board_try_white.is_filled():
        return solve(_board_try_white)


def apply_strategies_to_board(board: Board) -> None:
    board_states: set[str] = set()

    while (board_state := hash(str(board))) not in board_states:
        board_states.add(board_state)

        for row_cellvector in board.rows():
            apply_strategies_to_cellvector(row_cellvector)
        for col_cellvector in board.columns():
            apply_strategies_to_cellvector(col_cellvector)


def apply_strategies_to_cellvector(cellvector: CellVector) -> None:
    for strategy in ALL_STRATEGIES:
        strategy(cellvector)
