import pytest

from binairo_solver.board import Board, CellState, CellVector
from binairo_solver.error import BoardBoundaryError, BoardConstraintError


class TestBoard:

    def test_new_board(self):
        board = Board(4)
        assert board.size == 4
        assert len(board.cells) == 16

    def test_board_size(self):
        with pytest.raises(BoardConstraintError):
            Board(3)
        with pytest.raises(BoardConstraintError):
            Board(5)

        try:
            Board(10)
        except BoardConstraintError:
            assert False, "Board size of 10 should be valid."

    def test_board_set(self):
        board = Board(4)
        board.set_cell(0, CellState.BLACK)
        assert board.cells[0].state == CellState.BLACK
        board.set_cell(15, CellState.WHITE)
        assert board.cells[15].state == CellState.WHITE

        with pytest.raises(BoardBoundaryError):
            board.set_cell(99, CellState.BLACK)

    def test_get_row(self):
        board = Board(4)
        board.set_cell(0, CellState.BLACK)
        board.set_cell(1, CellState.WHITE)
        board.set_cell(2, CellState.BLACK)
        board.set_cell(3, CellState.WHITE)

        row_vector = board.get_row(0)

        assert row_vector == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
                CellState.WHITE,
            ]
        )

    def test_get_column(self):
        board = Board(4)
        board.set_cell(0, CellState.BLACK)
        board.set_cell(4, CellState.WHITE)
        board.set_cell(8, CellState.BLACK)
        board.set_cell(12, CellState.WHITE)

        col_vector = board.get_column(0)

        assert col_vector == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
                CellState.WHITE,
            ]
        )

    def test_from_text_instructions(self):

        # note that we're testing a 4x4 board here
        # with mixed case letters for states
        board = Board.from_text_instructions(
            """
            4
            0 B
            1 W
            2 b
            15 B
            10 B
            3 W
            15 w
            """
        )

        assert board.size == 4
        assert str(board.get_row(0)) == "*o*o"
        assert str(board.get_row(1)) == "____"
        assert str(board.get_row(2)) == "__*_"
        assert str(board.get_row(3)) == "___o"

    def test_from_text_map(self):

        board = Board.from_text_map(
            """
            *o*o
            _**_
            __*_
            ___o
            """
        )

        assert board.size == 4
        assert str(board.get_row(0)) == "*o*o"
        assert str(board.get_row(1)) == "_**_"
        assert str(board.get_row(2)) == "__*_"
        assert str(board.get_row(3)) == "___o"
