from src.sudoku_solver.cell import Cell
from src.sudoku_solver.grid import Grid
from src.sudoku_solver.solver import Solver
from tests.sample_grids import EASY_GRID, EXPERT_GRID_STUCK_CANDIDATES, HARD_GRID, HARD_GRID_2, MEDIUM_GRID, STARTING_GRID, build_grid_from_candidates


def test_eliminate_single_values_row():
    grid = Grid(STARTING_GRID)

    solver = Solver()

    row = grid.getRow(0)
    solver.eliminateExisting(row, 1)

    cell = grid.getCell(0, 2)
    assert cell.getNumberPossible() == 6
    assert 1 in cell.getPossible()
    assert 2 in cell.getPossible()
    assert 3 not in cell.getPossible()
    assert 4 in cell.getPossible()
    assert 5 not in cell.getPossible()
    assert 6 in cell.getPossible()
    assert 7 not in cell.getPossible()
    assert 8 in cell.getPossible()
    assert 9 in cell.getPossible()

    grid.printGrid()

def test_eliminate_single_values_column():
    grid = Grid(STARTING_GRID)

    solver = Solver()

    column = grid.getColumn(1)
    solver.eliminateExisting(column, 1)
    grid.printGrid()
    cell = grid.getCell(1, 1)
    assert cell.getNumberPossible() == 6
    assert 1 in cell.getPossible()
    assert 2 in cell.getPossible()
    assert 3 not in cell.getPossible()
    assert 4 in cell.getPossible()
    assert 5 in cell.getPossible()
    assert 6 not in cell.getPossible()
    assert 7 in cell.getPossible()
    assert 8 in cell.getPossible()
    assert 9 not in cell.getPossible()

def test_eliminate_single_values_subgrid():
    grid = Grid(STARTING_GRID)

    solver = Solver()

    subGrid = grid.getSubgridAsSingleArray(0, 1)
    solver.eliminateExisting(subGrid, 1)
    grid.printGrid()
    cell = grid.getCell(0, 3)
    assert cell.getNumberPossible() == 5
    assert 1 not in cell.getPossible()
    assert 2 in cell.getPossible()
    assert 3 in cell.getPossible()
    assert 4 in cell.getPossible()
    assert 5 not in cell.getPossible()
    assert 6 in cell.getPossible()
    assert 7 not in cell.getPossible()
    assert 8 in cell.getPossible()
    assert 9 not in cell.getPossible()

def test_eliminate_multi_values_row():
    grid = Grid(MEDIUM_GRID)

    solver = Solver()
    grid.printGrid()

    solver.fullIterativePass(grid, 1)
    grid.printGrid()

    solver.eliminateExisting(grid.getColumn(6), 3)
    grid.printGrid()

    testCell = grid.getCell(5, 6)
    assert 1 not in testCell.getPossible()
    assert 2 not in testCell.getPossible()
    assert 3 not in testCell.getPossible()
    assert 4 not in testCell.getPossible()
    assert 5 not in testCell.getPossible()
    assert 6 not in testCell.getPossible()
    assert 7 in testCell.getPossible()
    assert 8 in testCell.getPossible()
    assert 9 not in testCell.getPossible()

def test_is_single_row_when_confined_to_one_row():
    grid = Grid()
    solver = Solver()
    subgrid = grid.getSubgridAsSingleArray(0, 0)

    # Only row 1 (indexes 3, 4, 5) can still contain the number 7.
    for index in [0, 1, 2, 6, 7, 8]:
        subgrid[index].markNotPossible(7)

    assert solver.isSingleRow(subgrid, 7) == 1

def test_is_single_row_when_spread_across_rows():
    grid = Grid()
    solver = Solver()
    subgrid = grid.getSubgridAsSingleArray(0, 0)

    # The number 7 is still possible in both row 0 and row 2, so no single row can be identified.
    for index in [3, 4, 5]:
        subgrid[index].markNotPossible(7)

    assert solver.isSingleRow(subgrid, 7) is None

def test_is_single_column_when_confined_to_one_column():
    grid = Grid()
    solver = Solver()
    subgrid = grid.getSubgridAsSingleArray(0, 0)

    # Only column 1 (indexes 1, 4, 7) can still contain the number 7.
    for index in [0, 2, 3, 5, 6, 8]:
        subgrid[index].markNotPossible(7)

    assert solver.isSingleColumn(subgrid, 7) == 1

def test_is_single_column_when_spread_across_columns():
    grid = Grid()
    solver = Solver()
    subgrid = grid.getSubgridAsSingleArray(0, 0)

    # The number 7 is still possible in both column 0 and column 2, so no single column can be identified.
    for index in [1, 4, 7]:
        subgrid[index].markNotPossible(7)

    assert solver.isSingleColumn(subgrid, 7) is None

def test_exclude_from_other_cells_first_subgrid():
    grid = Grid(HARD_GRID)
    solver = Solver()

    array = [Cell() for _ in range(9)]
    solver.excludeFromOtherCells(array, 1, 0)

    assert 1 in array[0].getPossible()
    assert 1 in array[1].getPossible()
    assert 1 in array[2].getPossible()
    assert 1 not in array[3].getPossible()
    assert 1 not in array[4].getPossible()
    assert 1 not in array[5].getPossible()
    assert 1 not in array[6].getPossible()
    assert 1 not in array[7].getPossible()
    assert 1 not in array[8].getPossible()

def test_exclude_from_other_cells_second_subgrid():
    grid = Grid(HARD_GRID)
    solver = Solver()

    array = [Cell() for _ in range(9)]
    solver.excludeFromOtherCells(array, 1, 1)

    assert 1 not in array[0].getPossible()
    assert 1 not in array[1].getPossible()
    assert 1 not in array[2].getPossible()
    assert 1 in array[3].getPossible()
    assert 1 in array[4].getPossible()
    assert 1 in array[5].getPossible()
    assert 1 not in array[6].getPossible()
    assert 1 not in array[7].getPossible()
    assert 1 not in array[8].getPossible()

def test_exclude_from_other_cells_third_subgrid():
    grid = Grid(HARD_GRID)
    solver = Solver()

    array = [Cell() for _ in range(9)]
    solver.excludeFromOtherCells(array, 1, 2)

    assert 1 not in array[0].getPossible()
    assert 1 not in array[1].getPossible()
    assert 1 not in array[2].getPossible()
    assert 1 not in array[3].getPossible()
    assert 1 not in array[4].getPossible()
    assert 1 not in array[5].getPossible()
    assert 1 in array[6].getPossible()
    assert 1 in array[7].getPossible()
    assert 1 in array[8].getPossible()

def test_exclude_in_subgrid_row():
    grid = Grid(HARD_GRID)

    solver = Solver()
    solver.fullIterativeThroughAllGroupSizes(grid)

    grid.printGrid()

    assert solver.isSingleRow(grid.getSubgridAsSingleArray(0, 2), 6) is 0
    assert solver.isSingleRow(grid.getSubgridAsSingleArray(0, 2), 9) is None


    solver.excludeFromOtherCells(grid.getRow(0), 1, 0)
    grid.printGrid()
    assert 1 in grid.getCell(0, 0).getPossible()
    assert 1 not in grid.getCell(0, 1).getPossible()
    assert 1 in grid.getCell(0, 2).getPossible()
    assert 1 not in grid.getCell(0, 3).getPossible()
    assert 1 not in grid.getCell(0, 4).getPossible()
    assert 1 not in grid.getCell(0, 5).getPossible()
    assert 1 not in grid.getCell(0, 7).getPossible()
    assert 1 not in grid.getCell(0, 8).getPossible()


def test_exclude_in_subgrid_column():
    grid = Grid(HARD_GRID)

    solver = Solver()
    solver.fullIterativeThroughAllGroupSizes(grid)

    grid.printGrid()

    assert solver.isSingleColumn(grid.getSubgridAsSingleArray(0, 2), 9) is 2

    assert solver.isSingleColumn(grid.getSubgridAsSingleArray(0, 1), 1) is None

    solver.excludeFromOtherCells(grid.getColumn(8), 9, 0)
    grid.printGrid()
    assert 9 in grid.getCell(1, 8).getPossible()
    assert 9 not in grid.getCell(7, 8).getPossible()


def assert_fully_and_correctly_solved(grid, originalPuzzle):
    assert grid.isSolved()

    for index in range(9):
        assert {cell.getValue() for cell in grid.getRow(index)} == set(range(1, 10))
        assert {cell.getValue() for cell in grid.getColumn(index)} == set(range(1, 10))

    for row in range(3):
        for column in range(3):
            subgrid = grid.getSubgridAsSingleArray(row, column)
            assert {cell.getValue() for cell in subgrid} == set(range(1, 10))

    for r, row in enumerate(originalPuzzle):
        for c, value in enumerate(row):
            if value is not None:
                assert grid.getCell(r, c).getValue() == value

def test_solve_easy_grid():
    grid = Grid(EASY_GRID)
    solver = Solver()

    solver.solve(grid)

    assert_fully_and_correctly_solved(grid, EASY_GRID)

def test_solve_medium_grid():
    grid = Grid(MEDIUM_GRID)
    solver = Solver()

    solver.solve(grid)

    assert_fully_and_correctly_solved(grid, MEDIUM_GRID)

def test_solve_hard_grid():
    grid = Grid(HARD_GRID)
    solver = Solver()

    solver.solve(grid)

    assert_fully_and_correctly_solved(grid, HARD_GRID)


def test_is_only_in_subgrid_column():
    grid = build_grid_from_candidates(EXPERT_GRID_STUCK_CANDIDATES)
    solver = Solver()

    column_with_threes = grid.getColumn(7)
    containing_subgrid = solver.is_only_in_subgrid(column_with_threes, 3)
    assert containing_subgrid is 2

    no_containing_subgrid = solver.is_only_in_subgrid(column_with_threes, 9)
    assert no_containing_subgrid is None

def test_is_only_in_subgrid_row():
    grid = build_grid_from_candidates(EXPERT_GRID_STUCK_CANDIDATES)
    solver = Solver()

    row_with_twos = grid.getRow(6)
    containing_subgrid = solver.is_only_in_subgrid(row_with_twos, 2)
    assert containing_subgrid is 1

    no_containing_subgrid = solver.is_only_in_subgrid(row_with_twos, 3)
    assert no_containing_subgrid is None

def test_exclude_within_subgrid_column():
    grid = build_grid_from_candidates(EXPERT_GRID_STUCK_CANDIDATES)
    solver = Solver()
    # Take the case where we want to remove the 3's from the first column
    subgrid_2_2 = grid.getSubgridAsSingleArray(2, 2)

    assert subgrid_2_2[0].isPossible(3) is False
    assert subgrid_2_2[1].isPossible(3) is True
    assert subgrid_2_2[2].isPossible(3) is False
    assert subgrid_2_2[3].isPossible(3) is False
    assert subgrid_2_2[4].isPossible(3) is True
    assert subgrid_2_2[5].isPossible(3) is False
    assert subgrid_2_2[6].isPossible(3) is True
    assert subgrid_2_2[7].isPossible(3) is False
    assert subgrid_2_2[8].isPossible(3) is False

    solver.exclude_within_subgrid(subgrid_2_2, 3, 1, False)

    assert subgrid_2_2[0].isPossible(3) is False
    assert subgrid_2_2[1].isPossible(3) is True
    assert subgrid_2_2[2].isPossible(3) is False
    assert subgrid_2_2[3].isPossible(3) is False
    assert subgrid_2_2[4].isPossible(3) is True
    assert subgrid_2_2[5].isPossible(3) is False
    assert subgrid_2_2[6].isPossible(3) is False
    assert subgrid_2_2[7].isPossible(3) is False
    assert subgrid_2_2[8].isPossible(3) is False

def test_exclude_within_subgrid_row():
    grid = build_grid_from_candidates(EXPERT_GRID_STUCK_CANDIDATES)
    solver = Solver()
    # Take the case where we want to remove the 9's from the third row
    subgrid_2_1 = grid.getSubgridAsSingleArray(2, 1)

    assert subgrid_2_1[0].isPossible(9) is False
    assert subgrid_2_1[1].isPossible(9) is False
    assert subgrid_2_1[2].isPossible(9) is True
    assert subgrid_2_1[3].isPossible(9) is False
    assert subgrid_2_1[4].isPossible(9) is False
    assert subgrid_2_1[5].isPossible(9) is False
    assert subgrid_2_1[6].isPossible(9) is True
    assert subgrid_2_1[7].isPossible(9) is False
    assert subgrid_2_1[8].isPossible(9) is True

    solver.exclude_within_subgrid(subgrid_2_1, 9, 0, True)

    assert subgrid_2_1[0].isPossible(9) is False
    assert subgrid_2_1[1].isPossible(9) is False
    assert subgrid_2_1[2].isPossible(9) is True
    assert subgrid_2_1[3].isPossible(9) is False
    assert subgrid_2_1[4].isPossible(9) is False
    assert subgrid_2_1[5].isPossible(9) is False
    assert subgrid_2_1[6].isPossible(9) is False
    assert subgrid_2_1[7].isPossible(9) is False
    assert subgrid_2_1[8].isPossible(9) is False


def test_delete_from_within_subgrid():
    grid = build_grid_from_candidates(EXPERT_GRID_STUCK_CANDIDATES)
    solver = Solver()

    assert grid.getCell(8, 6).isPossible(3) is True

    solver.delete_from_within_subgrid(grid)

    assert grid.getCell(6, 7).isPossible(3) is True
    assert grid.getCell(7, 7).isPossible(3) is True
    assert grid.getCell(8, 6).isPossible(3) is False


