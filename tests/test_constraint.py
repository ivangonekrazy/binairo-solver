from binairo_solver.board import Board, CellState, CellVector
from binairo_solver.constraint import equal_number_of_states, no_three_in_a_row


class TestConstraintBoard:

    def test_meets_constraint(self):
        board = Board.from_text_map(
            """
            **oo*o
            o*o*o*
            *o**oo
            o*oo**
            oo**o*
            *o*o*o
            """
        )

        assert board.meets_constraints() is True

    def test_does_not_meet_constraint(self):
        board = Board.from_text_map(
            """
            oooooo
            o*o*o*
            *o**oo
            o*oo**
            oo**o*
            *o*o*o
            """
        )

        assert board.meets_constraints() is False


class TestConstraintNoThreeInARow:

    def test_no_three_in_a_row(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
                CellState.BLACK,
            ]
        )

        assert no_three_in_a_row(vec) is True

    def test_three_in_a_row(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        assert no_three_in_a_row(vec) is False

    def test_no_three_empty_in_a_row(self):
        vec = CellVector.from_states(
            [
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.BLACK,
            ]
        )

        assert no_three_in_a_row(vec) is True


class TestConstraintEqualNumberOfStates:

    def test_equal_number_of_states(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        assert equal_number_of_states(vec) is True

    def test_equal_number_of_states_with_empty(self):
        vec = CellVector.from_states(
            [
                CellState.EMPTY,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        assert equal_number_of_states(vec) is True

    def test_unequal_number_of_states(self):
        vec = CellVector.from_states(
            [
                CellState.WHITE,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.WHITE,
                CellState.WHITE,
            ]
        )

        assert equal_number_of_states(vec) is False
