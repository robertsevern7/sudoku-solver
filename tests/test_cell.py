import pytest

from src.sudoku_solver.cell import Cell


def test_new_cell_is_not_found():
    cell = Cell()
    assert cell.isValueFound() is False
    assert cell.getNumberPossible() == 9

def test_some_eliminated():
    cell = Cell()
    cell.markNotPossible(2)
    assert cell.isValueFound() is False
    assert cell.getNumberPossible() == 8
    assert 1 in cell.getPossible()
    assert 2 not in cell.getPossible()
    assert 8 in cell.getPossible()

def test_cell_value_found_1():
    cell = Cell()
    cell.markNotPossible(2)
    cell.markNotPossible(3)
    cell.markNotPossible(4)
    cell.markNotPossible(5)
    cell.markNotPossible(6)
    cell.markNotPossible(7)
    cell.markNotPossible(8)
    cell.markNotPossible(9)

    assert cell.isValueFound() is True
    assert cell.getValue() is 1

def test_cell_value_found_2():
    cell = Cell()
    cell.markNotPossible(1)
    cell.markNotPossible(3)
    cell.markNotPossible(4)
    cell.markNotPossible(5)
    cell.markNotPossible(6)
    cell.markNotPossible(7)
    cell.markNotPossible(8)
    cell.markNotPossible(9)

    assert cell.isValueFound() is True
    assert cell.getValue() is 2

def test_cell_value_found_9():
    cell = Cell()
    cell.markNotPossible(1)
    cell.markNotPossible(2)
    cell.markNotPossible(3)
    cell.markNotPossible(4)
    cell.markNotPossible(5)
    cell.markNotPossible(6)
    cell.markNotPossible(7)
    cell.markNotPossible(8)

    assert cell.isValueFound() is True
    assert cell.getValue() is 9

def test_preset_value():
    cell = Cell(4)

    assert cell.isValueFound() is True
    assert cell.getValue() is 4

def test_mark_not_possible_rejects_out_of_range_number():
    cell = Cell()

    with pytest.raises(RuntimeError):
        cell.markNotPossible(0)

    with pytest.raises(RuntimeError):
        cell.markNotPossible(10)

def test_set_value():
    cell = Cell()
    cell.setValue(3)

    assert cell.getValue() == 3

def test_fail_set_value():
    cell = Cell()

    cell.markNotPossible(3)
    with pytest.raises(RuntimeError):
        cell.setValue(3)

def test_clone():
    cell = Cell()

    cell.markNotPossible(1)
    cell.markNotPossible(5)

    cell_clone = cell.clone()

    assert 1 not in cell_clone.getPossible()
    assert 2 in cell_clone.getPossible()
    assert 3 in cell_clone.getPossible()
    assert 4 in cell_clone.getPossible()
    assert 5 not in cell_clone.getPossible()
    assert 6 in cell_clone.getPossible()
    assert 7 in cell_clone.getPossible()
    assert 8 in cell_clone.getPossible()
    assert 9 in cell_clone.getPossible()

    cell.markNotPossible(2)

    assert 2 not in cell.getPossible()
    assert 2 in cell_clone.getPossible()

    cell_clone.markNotPossible(7)

    assert 7 not in cell.getPossible()
    assert 7 in cell_clone.getPossible()
