from SnakeClass import Snake


def getNeighbours(pos):

    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]

    neighboursList = []
    for i in range(4):
        adjx = pos[0] + dRow[i]
        adjy = pos[1] + dCol[i]
        neighboursList.append([adjx, adjy])
    return neighboursList


def exploration(pos, depth, mySnake):
    neighboursList = getNeighbours(pos)

    for neighbour in neighboursList:
        isValid = mySnake.validateNeighbour(neighbour)

        if isValid and 1 < depth:
            mySnake.moveSnake(neighbour)
            exploration(neighbour, depth - 1, mySnake)
            mySnake.undoMoveSnake()

        if isValid and depth == 1:
            mySnake.increasePathCount()


if __name__ == "__main__":

    mySnake = Snake(
        body=[[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]],
        board=[4, 3],
        depth=3,
    )

    exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

    print(
        f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
    )

    mySnake = Snake(
        body=[[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]], board=[2, 3], depth=10
    )

    exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

    print(
        f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
    )

    mySnake = Snake(body=[[5, 5], [5, 4], [4, 4], [4, 5]], board=[10, 10], depth=4)

    exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

    print(
        f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
    )
