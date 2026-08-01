import itertools

class Solver:
    def solve(self, grid):
        while True:
            originalTotalPossible = grid.getTotalPossibleCount()

            if grid.isSolved():
                print("Successfully Solved")
                grid.printGrid()
                return

            self.fullIterativeThroughAllGroupSizes(grid)
            self.excludeIfSingleIndex(grid)
            self.delete_from_within_subgrid(grid)

            updatedTotalPossibleCount = grid.getTotalPossibleCount()

            if originalTotalPossible == updatedTotalPossibleCount:
                print("I'm Stuck")
                grid.printGrid()
                return


    def fullIterativeThroughAllGroupSizes(self, grid):
        for group_size in range(9):
            self.fullIterativePass(grid, group_size)

    def fullIterativePass(self, grid, group_size: int):
        totalPossible = grid.getTotalPossibleCount()

        while True:
            self.fullSinglePass(grid, group_size)
            updateTotalPossibleCount = grid.getTotalPossibleCount()
            if totalPossible == updateTotalPossibleCount:
                return

            totalPossible = updateTotalPossibleCount


    def fullSinglePass(self, grid, group_size: int):
        for index in range(9):
            self.eliminateExisting(grid.getRow(index), group_size)

        for index in range(9):
            self.eliminateExisting(grid.getColumn(index), group_size)

        for row in range(3):
            for column in range(3):
                self.eliminateExisting(grid.getSubgridAsSingleArray(row, column), group_size)
# TECHNIQUE 1 - CONTIANED GROUPS--------------------------------------------------------
    def eliminateExisting(self, array, group_size: int):
        toTest = [[index, cell] for index, cell in enumerate(array) if cell.getNumberPossible() <= group_size]
        # If the set of unique numbers equals the group size, then eliminate those numbers from the other cells

        #  the number of possibilites here is n choose k without order mattering
        #  Think example - group size 3
        #  [1,2], [4,5], [1,3], [1,2,3]
        #  Possibles
        #  [1,2], [4,5], [1,3]
        #  [1,2], [4,5],       [1, 2, 3]
        #  [1,2],        [1,3], [1, 2, 3]
        #         [4,5], [1,3], [1, 2, 3]

        # n choose k formula is n!/k!(n-k)!
        # 4 choose 3 -> 4!/3!(4-3)! = 4

        # Slightly harder example
        #  [1,2], [4,5], [4,6], [1,3], [1,2,3]
        #  Possibles
        #  [1,2], [4,5], [4,6]
        #  [1,2], [4,5],      , [1,3]
        #  [1,2], [4,5],             , [1,2,3]
        #  [1,2],      , [4,6], [1,3]
        #  [1,2],      , [4,6],      , [1,2,3]
        #  [1,2],      ,      , [1,3], [1,2,3]
        #       , [4,5], [4,6], [1,3]
        #       , [4,5], [4,6],      , [1,2,3]
        #       , [4,5],      , [1,3], [1,2,3]
        #       ,      , [4,6], [1,3], [1,2,3]

        # 5 choose 3 -> 5!/3!(5-3)! = 5*4/2 = 10

        combinations_list = list(itertools.combinations(toTest, group_size))

        for combinations in combinations_list:
            possibleValues = set()
            groupIndexes = set()
            for [originalIndex, cell] in combinations:
                possibleValues = possibleValues.union(cell.getPossible())
                groupIndexes.add(originalIndex)


            if len(possibleValues) == group_size:
                # We have identified that combinations is a distinct group,
                # and those possible values can be removed from everything not in the group
                for value in [cell for index, cell in enumerate(array) if index not in groupIndexes]:
                    for possibleValue in possibleValues:
                        value.markNotPossible(possibleValue)

# TECHNIQUE 2 - CANDIDATES IN SINGLE COLUMNS AND ROWS--------------------------------------------------------
    def excludeIfSingleIndex(self, grid):
        for row in range(3):
            for column in range(3):
                subgrid = grid.getSubgridAsSingleArray(row, column)
                for number in range(1, 10):
                    single_row = self.isSingleRow(subgrid, number)
                    if single_row is not None:
                        self.excludeFromOtherCells(grid.getRow(row * 3 + single_row), number, column)

                    single_column = self.isSingleColumn(subgrid, number)

                    if single_column is not None:
                        self.excludeFromOtherCells(grid.getColumn(column * 3 + single_column), number, row)

    def isSingleRow(self, subgrid, target_number) -> int:
        rows = set()
        for row in range(3):
            for column in range(3):
                cell = subgrid[3 * row + column]
                if cell.isPossible(target_number):
                    rows.add(row)

        if len(rows) == 1:
            return rows.pop()

    def isSingleColumn(self, subgrid, target_number) -> int:
        columns = set()
        for row in range(3):
            for column in range(3):
                cell = subgrid[3 * row + column]

                if cell.isPossible(target_number):
                    columns.add(column)

        if len(columns) == 1:
            return columns.pop()

    def excludeFromOtherCells(self, array, to_exclude, subgrid_index):
        for index, cell in enumerate(array):
            if (index < subgrid_index * 3 or index >= subgrid_index * 3 + 3):
                cell.markNotPossible(to_exclude)

#  TECHNIQUE 3 - INVERSE OF 2--------------------------------------------------------
    def delete_from_within_subgrid(self, grid) -> int:
        for number in range(1, 10):
            for index in range(9):
                row = grid.getRow(index)
                subgrid_index_for_row = self.is_only_in_subgrid(row, number)

                if subgrid_index_for_row is not None:
                    subgrid_for_row = grid.getSubgridAsSingleArray(index // 3, subgrid_index_for_row)
                    self.exclude_within_subgrid(subgrid_for_row, number, index % 3, True)

                column = grid.getColumn(index)
                subgrid_index_for_column = self.is_only_in_subgrid(column, number)

                if subgrid_index_for_column is not None:
                    subgrid_for_column = grid.getSubgridAsSingleArray(subgrid_index_for_column, index // 3)
                    self.exclude_within_subgrid(subgrid_for_column, number, index % 3, False)


    def is_only_in_subgrid(self, array, number) -> int:
        subgrid_1 = [cell for index, cell in enumerate(array) if index < 3]
        subgrid_2 = [cell for index, cell in enumerate(array) if index >= 3 and index < 6]
        subgrid_3 = [cell for index, cell in enumerate(array) if index >= 6]

        is_in_subgrid_1 = sum(1 for cell in subgrid_1 if cell.isPossible(number)) > 0
        is_in_subgrid_2 = sum(1 for cell in subgrid_2 if cell.isPossible(number)) > 0
        is_in_subgrid_3 = sum(1 for cell in subgrid_3 if cell.isPossible(number)) > 0

        if is_in_subgrid_1 and not is_in_subgrid_2 and not is_in_subgrid_3:
            return 0

        if not is_in_subgrid_1 and is_in_subgrid_2 and not is_in_subgrid_3:
            return 1

        if not is_in_subgrid_1 and not is_in_subgrid_2 and is_in_subgrid_3:
            return 2

    def exclude_within_subgrid(self, subgrid, number, index_to_retain, is_row):
        to_exclude = ([ cell for index, cell in enumerate(subgrid) if index not in range(3*index_to_retain, (1 + index_to_retain)*3)]
                      if is_row
                      else [ cell for index, cell in enumerate(subgrid) if index not in [0 + index_to_retain, 3 + index_to_retain, 6 + index_to_retain]]
                    )

        for cell in to_exclude:
            cell.markNotPossible(number)