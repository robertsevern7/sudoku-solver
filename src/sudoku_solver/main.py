from src.sudoku_solver.grid import Grid
from src.sudoku_solver.solver import Solver
from tests.sample_grids import EXPERT_GRID, HARD_GRID_2, HARD_GRID_3


def main() -> None:
    # grid = Grid(EASY_GRID)
    # grid = Grid(MEDIUM_GRID)
    # grid = Grid(HARD_GRID)
    # grid = Grid(HARD_GRID_2)
    grid = Grid(HARD_GRID_3)
    # grid = Grid(EXPERT_GRID)

    solver = Solver()
    solver.solve(grid)


if __name__ == "__main__":
    main()







