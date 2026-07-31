class Cell:
    def __init__(self, value = None):
        if value is None:
            self.possibleValues = [True, True, True, True, True, True, True, True, True]
        else:
            self.possibleValues = [False, False, False, False, False, False, False, False, False]
            self.possibleValues[value - 1] = True

    def markNotPossible(self, number: int):
        if (number < 1 or number > 9):
            raise RuntimeError('Must be between 1 and 9')
        self.possibleValues[number - 1] = False

    def isValueFound(self):
        return self.getNumberPossible() == 1

    def getNumberPossible(self) -> int:
        return sum(1 for value in self.possibleValues if value)

    def getPossible(self) -> set:
        return set(index + 1 for index, value in enumerate(self.possibleValues) if value)

    def isPossible(self, number: int) -> bool:
        return number in self.getPossible()

    def getValue(self):
        if self.isValueFound():
            return 1 + next((index for index, value in enumerate(self.possibleValues) if value))

    def render(self) -> list:
        if self.isValueFound():
            return [
                "       ",
                f"   {self.getValue()}   ",
                "       ",
            ]

        lines = []
        for row in range(3):
            chars = []
            for col in range(3):
                number = row * 3 + col + 1
                chars.append(str(number) if self.possibleValues[number - 1] else " ")
            lines.append(" " + " ".join(chars) + " ")
        return lines