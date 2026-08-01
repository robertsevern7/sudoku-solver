from src.sudoku_solver.grid import Grid

# A realistic starting Sudoku grid (a well-known, uniquely-solvable puzzle).
# `None` represents an empty cell. Shape of the puzzle below, `.` = empty:
#
# 5 3 . | . 7 . | . . .
# 6 . . | 1 9 5 | . . .
# . 9 8 | . . . | . 6 .
# ------+-------+------
# 8 . . | . 6 . | . . 3
# 4 . . | 8 . 3 | . . 1
# 7 . . | . 2 . | . 6 .
# ------+-------+------
# . 6 . | . . . | 2 8 .
# . . . | 4 1 9 | . . 5
# . . . | . 8 . | . 7 9

STARTING_GRID = [
    [5,    3,    None, None, 7,    None, None, None, None],
    [6,    None, None, 1,    9,    5,    None, None, None],
    [None, 9,    8,    None, None, None, None, 6,    None],
    [8,    None, None, None, 6,    None, None, None, 3   ],
    [4,    None, None, 8,    None, 3,    None, None, 1   ],
    [7,    None, None, None, 2,    None, None, None, None],
    [None, 6,    None, None, None, None, 2,    8,    None],
    [None, None, None, 4,    1,    9,    None, None, 5   ],
    [None, None, None, None, 8,    None, None, 7,    9   ],
]

EMPTY_GRID = [
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
]

EASY_GRID = [
    [7,    None, None, None, 4   , None, None, 9   , 3   ],
    [8,    4,    None, None, None, None, None, 2   , 1   ],
    [9,    1,    2   , 8   , None, 7   , None, None, None],
    [1,    6,    7   , None, None, 4   , None, None, None],
    [None, 2,    None, 5   , 7   , 6   , None, 8   , None],
    [None, None, 9   , None, 2   , None, 4   , 6   , None],
    [6,    7,    None, None, 9   , None, 3   , None, 8   ],
    [None, None, 1   , None, 6   , None, 9   , None, 4   ],
    [4   , None, None, 3   , None, None, 6   , None, None],
]

MEDIUM_GRID = [
    [6   , None, None, None, 7   , None, None, None, None],
    [None, None, None, None, None, 4   , 2   , None, None],
    [None, None, 4   , None, 1   , None, None, 9   , 8   ],
    [None, None, None, 8   , None, None, None, None, None],
    [5   , None, 1   , None, None, None, 9   , None, None],
    [None, None, 2   , None, 5   , 3   , None, None, None],
    [None, 1   , None, None, None, None, None, 7   , None],
    [None, None, 9   , None, None, None, None, 8   , 5   ],
    [None, None, None, 5   , None, 6   , None, None, 3   ],
]

HARD_GRID = [
    [None, None, None, None, None, None, None, 5   , 3   ],
    [3,    None, None, None, 6   , None, None, None, None],
    [6,    None, 8   , None, None, 7   , 2   , None, None],
    [None, 5   , None, 8   , 4   , None, None, 9   , 7   ],
    [None, None, None, None, None, 6   , 4   , None, None],
    [None, None, None, None, 7   , None, None, None, None],
    [5   , 1   , None, None, None, None, None, None, None],
    [None, None, None, 3   , None, 1   , None, None, None],
    [None, None, 9   , None, None, None, None, None, 8   ],
]

HARD_GRID_2 = [
    [7   , None, None, 6   , None, None, 4   , None, 2   ],
    [None, 1   , None, None, 8   , None, None, None, None],
    [None, None, None, 5   , None, None, None, None, None],
    [4   , None, None, None, None, 7   , None, None, None],
    [3   , None, None, None, 1   , None, None, 8   , 6   ],
    [None, None, None, None, None, None, 7   , 9   , None],
    [None, None, 7   , None, None, None, None, None, None],
    [None, 5   , None, None, None, 2   , 3   , 6   , None],
    [None, 4   , 1   , None, None, None, None, None, 9   ],
]

# A puzzle with a unique solution that the current solver cannot fully solve
# (it stalls partway through). Shape below, `.` = empty:
#
# . . 3 | 2 9 . | 4 1 7
# . . 1 | 8 . . | . 5 .
# . 9 5 | 3 . . | 8 6 2
# ------+-------+------
# 5 . . | . 3 . | . . .
# 8 4 . | . 7 . | . 2 .
# . . 9 | 6 . . | 5 7 .
# ------+-------+------
# 1 . 8 | 4 . . | 7 . .
# 9 6 . | . . . | 2 . 1
# 2 . . | . . . | . 4 .

EXPERT_GRID = [
    [None, None, 3   , 2   , 9   , None, 4   , 1   , 7   ],
    [None, None, 1   , 8   , None, None, None, 5   , None],
    [None, 9   , 5   , 3   , None, None, 8   , 6   , 2   ],
    [5   , None, None, None, 3   , None, None, None, None],
    [8   , 4   , None, None, 7   , None, None, 2   , None],
    [None, None, 9   , 6   , None, None, 5   , 7   , None],
    [1   , None, 8   , 4   , None, None, 7   , None, None],
    [9   , 6   , None, None, None, None, 2   , None, 1   ],
    [2   , None, None, None, None, None, None, 4   , None],
]

# The candidate state the current solver reaches on EXPERT_GRID before it
# stalls (i.e. running Solver().solve() on EXPERT_GRID stops here). Each
# cell holds the digits still possible for it at that point; a single-item
# list means the cell was already solved. Frozen here so this exact state
# stays available as a regression fixture even after the solver improves
# and can get past it.
EXPERT_GRID_STUCK_CANDIDATES = [
    [[6], [8], [3], [2], [9], [5], [4], [1], [7]],
    [[4, 7], [2], [1], [8], [4, 6], [4, 6, 7], [3, 9], [5], [3, 9]],
    [[4, 7], [9], [5], [3], [1, 4], [1, 4, 7], [8], [6], [2]],
    [[5], [7], [2], [1, 9], [3], [4, 8], [1, 6, 9], [8, 9], [4, 6, 8]],
    [[8], [4], [6], [5], [7], [1, 9], [1, 3, 9], [2], [3, 9]],
    [[3], [1], [9], [6], [2, 4, 8], [2, 4, 8], [5], [7], [4, 8]],
    [[1], [3, 5], [8], [4], [2, 6], [2, 3, 6, 9], [7], [3, 9], [5, 6]],
    [[9], [6], [4], [7], [5], [3, 8], [2], [3, 8], [1]],
    [[2], [3, 5], [7], [1, 9], [1, 6, 8], [1, 3, 6, 8, 9], [3, 6, 9], [4], [5, 6, 8]],
]


def build_grid_from_candidates(candidates):
    grid = Grid()
    for r, row in enumerate(candidates):
        for c, possible in enumerate(row):
            cell = grid.getCell(r, c)
            for number in range(1, 10):
                if number not in possible:
                    cell.markNotPossible(number)
    return grid