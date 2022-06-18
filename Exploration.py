import sys
from ast import literal_eval
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
    # Get the neighbours
    neighboursList = getNeighbours(pos)

    # Process each one
    for neighbour in neighboursList:

        # Check if it is valid
        isValid = mySnake.validateNeighbour(neighbour)

        # If valid, but depth not reached, move snake and repeat
        if isValid and 1 < depth:
            mySnake.moveSnake(neighbour)
            exploration(neighbour, depth - 1, mySnake)
            mySnake.undoMoveSnake()

        # If valid and depth reached increase count of paths
        if isValid and depth == 1:
            mySnake.increasePathCount()


def main(argv):

    # If there are arguments
    if len(sys.argv) == 4:

        mySnake = Snake(
            body=literal_eval(sys.argv[2]),
            board=literal_eval(sys.argv[1]),
            depth=int(sys.argv[3]),
        )

        exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

        print(
            f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
        )

    # If the are no arguments
    else:
        # Depth 3
        mySnake = Snake(
            body=[[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]],
            board=[4, 3],
            depth=3,
        )

        exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

        print(
            f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
        )

        # Depth 10
        mySnake = Snake(
            body=[[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]],
            board=[2, 3],
            depth=10,
        )

        exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

        print(
            f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
        )

        # Depth 4
        mySnake = Snake(body=[[5, 5], [5, 4], [4, 4], [4, 5]], board=[10, 10], depth=4)

        exploration(mySnake.getCurrentHead(), mySnake.getDepth(), mySnake)

        print(
            f"{mySnake.getPathCount()} rutas de profundidad {mySnake.getDepth()} posibles"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
