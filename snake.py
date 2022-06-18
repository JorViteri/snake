board = [10, 10]
snakeCurrent = [[5,5], [5,4], [4,4], [4,5]]
snakeHead = []  # TODO mejor unos stacks aqui
oldSnakeHeads = []
snakeTail = []
oldSnakeTails = []
depth = 4
positionsChecked = []
count = 0


# TODO CUIDADIN CON LOS pop


def moveSnake(newSnakeHead):
    global snakeCurrent, snakeHead, snakeTail, oldSnakeHeads, oldSnakeTails

    oldSnakeTails = oldSnakeTails + [snakeCurrent[len(snakeCurrent) - 1]]
    snakeTail = snakeCurrent.pop()
    oldSnakeHeads.append(snakeCurrent[0])
    snakeCurrent = [newSnakeHead] + snakeCurrent
    snakeHead = newSnakeHead


def undoMoveSnake():
    global snakeCurrent, snakeHead, snakeTail, oldSnakeHeads, oldSnakeTails

    # TODO
    if len(oldSnakeHeads) == 0:
        cosa = "aaaaaaaaaaaaaaaaaaaah"
    # TODO
    snakeHead = oldSnakeHeads.pop()
    # TODO
    if len(oldSnakeTails) == 0:
        cosa = "aaaaaaaaaaaaaaaaaaaah"
    # TODO
    snakeTail = oldSnakeTails.pop()
    snakeCurrent.pop(0)  # TODO tengo que quitarle el primero
    snakeCurrent.append(snakeTail)


def validateNeighbour(pos):
    global snakeCurrent, snakeTail, positionsChecked

    xLim = board[0] - 1
    yLim = board[1] - 1

    # Position not within matrix
    if pos[0] < 0 or pos[1] < 0 or pos[0] > xLim or pos[1] > yLim:
        return False

    # TODO no deberia ser necesario Position visited
    # if pos in positionsChecked:
    #    return False

    # Position in body of snakeCurrent

    if pos in snakeCurrent and pos != snakeCurrent[len(snakeCurrent) - 1]:
        return False

    return True


def getNeighbours(pos):

    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]

    neighboursList = []
    for i in range(4):
        adjx = pos[0] + dRow[i]
        adjy = pos[1] + dCol[i]
        neighboursList.append([adjx, adjy])
    return neighboursList


def exploration(pos, depth, paths):
    lastList = []
    neighboursList = getNeighbours(pos)

    for neighbour in neighboursList:
        isValid = validateNeighbour(neighbour)

        if isValid and 1 < depth:
            paths.append(neighbour)
            moveSnake(neighbour)
            paths = exploration(neighbour, depth - 1, paths)
            undoMoveSnake()

        if isValid and depth == 1:
            global count
            count = count + 1
            paths.append(neighbour)
            # return paths

    lastList = lastList + paths

    return lastList


if __name__ == "__main__":

    depth = 4
    result = exploration(snakeCurrent[0], depth, [])

    print(f"{count} rutas de profundidad {depth} posibles")
