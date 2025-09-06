from binairo_solver.board import Cell, CellState, CellVector


class TestCellVector:
    def test_fill_empty(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.EMPTY,
                CellState.WHITE,
            ]
        )

        vec.fill_empty(CellState.WHITE)

        assert 4 == vec.count_white()
        assert 1 == vec.count_black()

    def test_vector_reference(self):
        cells = [Cell(CellState.EMPTY) for _ in range(5)]
        cell_vector = CellVector(cells)

        cells[0].set_black()

        assert id(cell_vector.cells[0]) == id(cells[0])

    def test_vector_count(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        assert vec.count_black() == 4
        assert vec.count_white() == 1
        assert vec.count_empty() == 0

    def test_ngram(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.BLACK,
                CellState.EMPTY,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        ngrams = list(vec.n_grams(3))

        assert len(ngrams) == 3
        assert [c.state for c in ngrams[0]] == [
            CellState.BLACK,
            CellState.BLACK,
            CellState.EMPTY,
        ]
        assert [c.state for c in ngrams[1]] == [
            CellState.BLACK,
            CellState.EMPTY,
            CellState.WHITE,
        ]
        assert [c.state for c in ngrams[2]] == [
            CellState.EMPTY,
            CellState.WHITE,
            CellState.BLACK,
        ]

    def test_reversed_ngram(self):
        vec = CellVector.from_states(
            [
                CellState.BLACK,
                CellState.EMPTY,
                CellState.BLACK,
                CellState.WHITE,
                CellState.BLACK,
            ]
        )

        ngrams = list(vec.n_grams_reversed(3))

        assert len(ngrams) == 3
        assert [c.state for c in ngrams[0]] == [
            CellState.BLACK,
            CellState.WHITE,
            CellState.BLACK,
        ]
        assert [c.state for c in ngrams[1]] == [
            CellState.WHITE,
            CellState.BLACK,
            CellState.EMPTY,
        ]
        assert [c.state for c in ngrams[2]] == [
            CellState.BLACK,
            CellState.EMPTY,
            CellState.BLACK,
        ]

    def test_ngram_identity(self):
        cells = [Cell(CellState.EMPTY) for _ in range(5)]
        cells[0].set_black()
        cells[1].set_black()
        cells[2].set_black()
        cells[3].set_white()
        cells[4].set_black()
        vec = CellVector(cells)

        ngrams = list(vec.n_grams(3))

        assert len(ngrams) == 3
        for i, ngram in enumerate(ngrams):
            assert id(ngram[0]) == id(cells[i])
