from textwrap import dedent

from binairo_solver.board import Board
from binairo_solver.solver import Solver


class TestSolverFillUsingStrategies:

    def test_solver(self):
        board = Board.from_text_map(
            """
            *_o___
            _*_*__
            ____o_
            _____*
            __*_o*
            ______
            """
        )

        Solver(board).fill_using_strategies()

        assert board.is_filled() is True
        assert str(board.get_row(0)) == "**oo*o"
        assert str(board.get_row(1)) == "o*o*o*"
        assert str(board.get_row(2)) == "*o**oo"
        assert str(board.get_row(3)) == "o*oo**"
        assert str(board.get_row(4)) == "oo**o*"
        assert str(board.get_row(5)) == "*o*o*o"

    def test_unsolvable(self):
        board = Board.from_text_map(
            """
            *_o___
            _*_*__
            ____o_
            _____*
            __*_o_
            ______
            """
        )

        Solver(board).fill_using_strategies()

        assert board.is_filled() is False


class TestSolverSolve:

    def test_hard_solve(self):
        board = Board.from_text_map(
            """
            *_____
            ______
            ______
            ______
            ______
            ______
            """
        )

        solved_board = Solver(board).solve()

        assert solved_board.is_filled()
        assert solved_board.meets_constraints()

        assert str(solved_board.get_row(0)) == "**o*oo"
        assert str(solved_board.get_row(1)) == "**o*oo"
        assert str(solved_board.get_row(2)) == "oo*o**"
        assert str(solved_board.get_row(3)) == "**o*oo"
        assert str(solved_board.get_row(4)) == "oo*o**"
        assert str(solved_board.get_row(5)) == "oo*o**"
