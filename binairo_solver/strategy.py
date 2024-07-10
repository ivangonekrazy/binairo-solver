from binairo_solver.board import CellState, CellVector


def two_in_a_row_implies_flipped_third(vec: CellVector) -> int:
    """
    When two states are the same, the third must be different.
    """
    changes = 0

    for n in vec.n_grams(3):
        if (n[0].state == n[1].state) and n[2].is_empty():
            # if n[2].state == n[0].state:
            #     raise ConstraintError()

            n[2].set_opposite(n[0].state)
            changes += 1

    for n in vec.n_grams_reversed(3):
        if (n[0].state == n[1].state) and n[2].is_empty():
            # if n[2].state == n[0].state:
            #     raise ConstraintError()

            n[2].set_opposite(n[0].state)
            changes += 1

    return changes


def fill_in_between(vec: CellVector) -> int:
    """
    When there is an empty cell between two cells with the same state,
    fill it with the opposite state.
    """
    changes = 0

    for n in vec.n_grams(3):
        if (n[0].state == n[2].state) and n[1].is_empty():
            n[1].set_opposite(n[0].state)
            changes += 1

    return changes


def equal_number_of_states(vec: CellVector) -> int:
    """
    When half of the cells are of one state, the remaining cells
    must be of the opposite state.
    """
    changes = 0

    # if len(vec) % 2 != 0:
    #     raise ConstraintError("CellVector length must be even.")

    balanced_count = len(vec) // 2

    if vec.count_black() == vec.count_white():
        return changes

    if vec.count_black() == balanced_count:
        changes += vec.fill_empty(CellState.WHITE)

    if vec.count_white() == balanced_count:
        changes += vec.fill_empty(CellState.BLACK)

    return changes


ALL_STRATEGIES = [
    two_in_a_row_implies_flipped_third,
    fill_in_between,
    equal_number_of_states,
]
