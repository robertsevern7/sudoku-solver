import pytest

from src.sudoku_solver.grid import Grid
from src.sudoku_solver.cell import Cell
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

def test_get_subgrid_rejects_out_of_range_row():
    grid = Grid()

    with pytest.raises(RuntimeError):
        grid.getSubgridAsSingleArray(-1, 0)

    with pytest.raises(RuntimeError):
        grid.getSubgridAsSingleArray(3, 0)

def test_get_subgrid_rejects_out_of_range_column():
    grid = Grid()

    with pytest.raises(RuntimeError):
        grid.getSubgridAsSingleArray(0, -1)

    with pytest.raises(RuntimeError):
        grid.getSubgridAsSingleArray(0, 3)

def test_has_no_dupes():
    grid = Grid()

    array = [Cell() for _ in range(9)]
    array[0].setValue(1)
    array[1].setValue(2)
    assert not grid.hasDupes(array)

def test_has_dupes():
    grid = Grid()

    array = [Cell() for _ in range(9)]
    array[0].setValue(1)
    array[1].setValue(1)
    assert grid.hasDupes(array)

def test_is_valid():
    grid = Grid()
    grid.getCell(0, 0).setValue(1)
    grid.getCell(1, 1).setValue(2)
    grid.getCell(2, 2).setValue(3)
    grid.getCell(3, 3).setValue(4)
    grid.getCell(4, 4).setValue(5)
    grid.getCell(5, 5).setValue(6)
    grid.getCell(6, 6).setValue(7)
    grid.getCell(7, 7).setValue(8)
    grid.getCell(8, 8).setValue(9)

    assert grid.isValid()

def test_is_not_valid_row():
    grid = Grid()
    grid.getCell(0, 0).setValue(1)
    grid.getCell(1, 1).setValue(2)
    grid.getCell(2, 2).setValue(3)
    grid.getCell(3, 3).setValue(4)
    grid.getCell(4, 4).setValue(5)
    grid.getCell(5, 5).setValue(6)
    grid.getCell(6, 6).setValue(7)
    grid.getCell(7, 7).setValue(8)
    grid.getCell(8, 8).setValue(9)

    grid.getCell(0, 8).setValue(1)

    assert not grid.isValid()

def test_is_not_valid_column():
    grid = Grid()
    grid.getCell(0, 0).setValue(1)
    grid.getCell(1, 1).setValue(2)
    grid.getCell(2, 2).setValue(3)
    grid.getCell(3, 3).setValue(4)
    grid.getCell(4, 4).setValue(5)
    grid.getCell(5, 5).setValue(6)
    grid.getCell(6, 6).setValue(7)
    grid.getCell(7, 7).setValue(8)
    grid.getCell(8, 8).setValue(9)

    grid.getCell(8, 0).setValue(1)

    assert not grid.isValid()

def test_is_not_valid_subgrid():
    grid = Grid()
    grid.getCell(0, 0).setValue(1)
    grid.getCell(1, 1).setValue(2)
    grid.getCell(2, 2).setValue(3)
    grid.getCell(3, 3).setValue(4)
    grid.getCell(4, 4).setValue(5)
    grid.getCell(5, 5).setValue(6)
    grid.getCell(6, 6).setValue(7)
    grid.getCell(7, 7).setValue(8)
    grid.getCell(8, 8).setValue(9)

    grid.getCell(2, 1).setValue(1)

    assert not grid.isValid()

def test_clone():
    grid = Grid(STARTING_GRID)
    cloned = grid.clone()

    assert cloned.getCell(0, 0).getValue() == grid.getCell(0, 0).getValue()
    assert cloned.getCell(1, 1).getPossible() == grid.getCell(1, 1).getPossible()

    cloned.getCell(1, 1).markNotPossible(5)

    assert grid.getCell(1, 1).isPossible(5) is True
    assert cloned.getCell(1, 1).isPossible(5) is False
