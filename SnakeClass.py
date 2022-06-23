class Snake:
    def __init__(self, body, board, depth):
        self.snakeCurrent = body
        self.snakeLength = len(self.snakeCurrent)
        self.board = board
        self.depth = depth
        self.count = 0
        self.oldSnakeTails = []

    # Moves the snake setting the new head and saving the old tail in a stack
    def moveSnake(self, newSnakeHead):
        self.oldSnakeTails = self.oldSnakeTails + [self.snakeCurrent.pop()]
        self.snakeCurrent = [newSnakeHead] + self.snakeCurrent

    # Removes the current head and recovers the old tail
    def undoMoveSnake(self):
        self.snakeCurrent.pop(0)
        self.snakeCurrent.append(self.oldSnakeTails.pop())

    # Check if the position is valid for movement
    def validateNeighbour(self, pos):
        xLim = self.board[0] - 1
        yLim = self.board[1] - 1

        # Position not within matrix
        if pos[0] < 0 or pos[1] < 0 or pos[0] > xLim or pos[1] > yLim:
            return False

        # Position in body of snakeCurrent
        if pos in self.snakeCurrent and pos != self.snakeCurrent[self.snakeLength - 1]:
            return False

        return True

    def getCurrentHead(self):
        return self.snakeCurrent[0]

    def getCurrentTail(self):
        return self.snakeCurrent[self.snakeLength - 1]

    def increasePathCount(self):
        self.count = self.count + 1

    def getPathCount(self):
        return self.count

    def getDepth(self):
        return self.depth
