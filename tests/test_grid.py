from src.sudoku_solver.grid import Grid
from tests.sample_grids import STARTING_GRID

gridIterable = [[None for _ in range(9)] for _ in range(9)]

def test_new_grid_is_not_solved():
    grid = Grid()
    assert grid.isSolved() is False

    for r, row in enumerate(gridIterable):
        for c, cell in enumerate(row):
            assert grid.getCell(r, c).isValueFound() == False

def test_grid_with_predefined_value():
    presetValues = [[None for _ in range(9)] for _ in range(9)]
    presetValues[3][4] = 5

    grid = Grid(presetValues)

    for r, row in enumerate(gridIterable):
        for c, cell in enumerate(row):
            if (r == 3 and c == 4):
                assert grid.getCell(r, c).isValueFound() == True
                assert grid.getCell(r, c).getValue() == 5
            else:
                assert grid.getCell(r, c).isValueFound() == False


def test_get_row():
    grid = Grid(STARTING_GRID)

    row = grid.getRow(3)

    assert row[0].isValueFound() == True
    assert row[1].isValueFound() == False
    assert row[2].isValueFound() == False
    assert row[3].isValueFound() == False
    assert row[4].isValueFound() == True
    assert row[5].isValueFound() == False
    assert row[6].isValueFound() == False
    assert row[7].isValueFound() == False
    assert row[8].isValueFound() == True

    assert row[0].getValue() == 8
    assert row[4].getValue() == 6
    assert row[8].getValue() == 3

def test_get_column():
    grid = Grid(STARTING_GRID)

    column = grid.getColumn(1)

    assert column[0].isValueFound() == True
    assert column[1].isValueFound() == False
    assert column[2].isValueFound() == True
    assert column[3].isValueFound() == False
    assert column[4].isValueFound() == False
    assert column[5].isValueFound() == False
    assert column[6].isValueFound() == True
    assert column[7].isValueFound() == False
    assert column[8].isValueFound() == False

    assert column[0].getValue() == 3
    assert column[2].getValue() == 9
    assert column[6].getValue() == 6

def test_get_sub_grid():
    grid = Grid(STARTING_GRID)

    subgrid = grid.getSubgridAsSingleArray(1,2)
    assert subgrid[0].isValueFound() == False
    assert subgrid[1].isValueFound() == False
    assert subgrid[2].isValueFound() == True
    assert subgrid[3].isValueFound() == False
    assert subgrid[4].isValueFound() == False
    assert subgrid[5].isValueFound() == True
    assert subgrid[6].isValueFound() == False
    assert subgrid[7].isValueFound() == False
    assert subgrid[8].isValueFound() == False

    assert subgrid[2].getValue() == 3
    assert subgrid[5].getValue() == 1