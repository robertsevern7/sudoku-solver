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