from src.sudoku_solver.cell import Cell


class Grid:
    def __init__(self, predefinedValues = None):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]

        if predefinedValues != None:
            for r, row in enumerate(predefinedValues):
                for c, value in enumerate(row):
                    if value != None:
                        self.grid[r] [c] = Cell(value)

    def isSolved(self):
        unfoundCount = sum(1 for row in self.grid if
            sum(1 for cell in row if not cell.isValueFound())
        )

        return unfoundCount == 0

    def getCell(self, row: int, column: int) -> Cell:
        return self.getRow(row)[column]

    def getRow(self, row: int):
        return self.grid[row]

    def getColumn(self, column):
        return [row[column] for row in self.grid]

    def getSubgridAsSingleArray(self, row: int, column: int):
        if row < 0 or row > 2:
            raise RuntimeError("Row out of range")

        if column < 0 or column > 2:
            raise RuntimeError("Column out of range")

        startRow = row * 3
        startColumn = column * 3

        subGrid = [None for _ in range(9)]

        for rowIndex in range(3):
            for columnIndex in range(3):
                subGrid[3 * rowIndex + columnIndex] = self.grid[startRow + rowIndex][startColumn + columnIndex]

        return subGrid

    def getTotalPossibleCount(self) -> int:
        total = 0
        for row in range(9):
            for column in range(9):
                total += self.grid[row][column].getNumberPossible()

        return total

    def hasSolved(self) -> int:
        return self.getTotalPossibleCount() == 81


# ########################################################
    def printGrid(self):
        rowSeparator = "+" + "+".join(["-------"] * 9) + "+"
        for row in self.grid:
            print(rowSeparator)
            cellLines = [cell.render() for cell in row]
            for lineIndex in range(3):
                print("|" + "|".join(cellLines[c][lineIndex] for c in range(9)) + "|")
        print(rowSeparator)
