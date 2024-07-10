from binairo_solver.board import Cell, CellState, CellVector
from binairo_solver.strategy import (
    equal_number_of_states,
    fill_in_between,
    two_in_a_row_implies_flipped_third,
)


class TestNoThreeInARowStrategy:

    def test_1_empty(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        changes = two_in_a_row_implies_flipped_third(vec)

        assert changes == 1
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

    def test_1_empty_at_head(self):
        vec = CellVector.from_states(
            [
                CellState.EMPTY,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        changes = two_in_a_row_implies_flipped_third(vec)

        assert changes == 1
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.WHITE,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

    def test_2_empty_consecutive(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.BLACK,
            ]
        )

        changes = two_in_a_row_implies_flipped_third(vec)

        assert changes == 1
        assert vec.count_empty() == 1
        assert vec == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.EMPTY,
                CellState.BLACK,
            ]
        )

        changes += two_in_a_row_implies_flipped_third(vec)
        assert changes == 1
        assert vec.count_empty() == 1

    def test_2_empty_non_consecutive(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.WHITE,
                CellState.EMPTY,
            ]
        )

        changes = two_in_a_row_implies_flipped_third(vec)

        assert changes == 2
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

    def test_2_empty_non_consecutive_2(self):
        vec = CellVector.from_states(
            [
                CellState.EMPTY,
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.WHITE,
            ]
        )

        changes = two_in_a_row_implies_flipped_third(vec)

        assert changes == 2
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.WHITE,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
            ]
        )


class TestFillInBetween:
    def test_1_empty(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.BLACK,
            ]
        )

        changes = fill_in_between(vec)

        assert changes == 1
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
                CellState.BLACK,
            ]
        )


class TestBalancedStates:
    def test_1_empty(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.WHITE,
            ]
        )

        changes = equal_number_of_states(vec)

        assert changes == 1
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [CellState.BLACK, CellState.WHITE, CellState.BLACK, CellState.WHITE]
        )

    def test_4_empty(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.EMPTY,
                CellState.BLACK,
            ]
        )

        changes = equal_number_of_states(vec)

        assert changes == 4
        assert vec.count_empty() == 0
        assert vec == CellVector.from_states(
            [
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )
