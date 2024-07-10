from binairo_solver.board import CellVector


def no_three_in_a_row(vec: CellVector) -> bool:
    """
    No three cells in a row may have the same state.
    """

    for n_grams in [vec.n_grams(3), vec.n_grams_reversed(3)]:
        for n in n_grams:
            if all([c.is_empty() for c in n]):
                return True
            if n[0].state == n[1].state == n[2].state:
                return False

    return True


def equal_number_of_states(vec: CellVector) -> bool:
    """
    In a full vector, the number of black and white cells must be equal.
    """

    if vec.count_empty() > 0:
        return True

    if len(vec) % 2 != 0:
        return False

    if vec.count_black() != vec.count_white():
        return False

    return True


ALL_CONSTRAINTS = [no_three_in_a_row, equal_number_of_states]
