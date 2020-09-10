import time
from operator import itemgetter


def main():
    size = int(input('Board Size: '))
    board = [[0 for i in range(size)] for j in range(size)]
    if size % 2 == 0:
        board = placeBlocksAlgorithmEven(board, size)
    else:
        board = placeBlocksAlgorithmOdd(board, size)
    input('Press any key to exit...')


def calcCOG(board):
    denominator = 0
    for row in board:
        for block in row:
            denominator += block

    numerator = 0
    for row in board:
        x_pos = 0
        for block in row:
            numerator += (block * (x_pos + 0.5))
            x_pos += 1
    x = numerator / denominator

    numerator = 0
    y_pos = len(board) - 1
    for row in board:
        for block in row:
            numerator += (block * (y_pos + 0.5))
        y_pos -= 1
    y = numerator / denominator

    return [x, y]


def checkBalance(size, cog):
    if size % 2 == 0:
        if (cog[0] < (size / 2) + 1) and (cog[0] > (size / 2) - 1) and (cog[1] < (size / 2) + 1) and (cog[1] > (size / 2) - 1):
            return True
        else:
            return False
    else:
        if (cog[0] < (size / 2) + 2) and (cog[0] > (size / 2) - 2) and (cog[1] < (size / 2) + 2) and (cog[1] > (size / 2) - 2):
            return True
        else:
            return False


def placeBlocksAlgorithmEven(board, size):
    layers = int(size / 2)
    current = size * size
    board[layers - 1][layers - 1] = current
    printBoard(board, size)

    current -= 1
    board[layers][layers] = current
    printBoard(board, size)

    current -= 1
    board[layers - 1][layers] = current
    printBoard(board, size)

    current -= 1
    board[layers][layers - 1] = current
    printBoard(board, size)

    current -= 1

    TL = (layers-1, layers-1)
    TR = (layers-1, layers)
    BL = (layers, layers-1)
    BR = (layers, layers)

    for layer in range(layers - 1, 0, -1):
        start = [[board[TL[0]][TL[1]], [TL[0] - 1, TL[1]], [0, 1]],
                 [board[TR[0]][TR[1]], [TR[0], TR[1] + 1], [1, 0]],
                 [board[BL[0]][BL[1]], [BL[0], BL[1] - 1], [-1, 0]],
                 [board[BR[0]][BR[1]], [BR[0] + 1, BR[1]], [0, -1]]]
        start.sort(key=itemgetter(0), reverse=False)

        layer_length = 2 * (layers - layer)
        if layer == 1:
            layer_length = size-2

        for _ in range(layer_length):
            for i in range(4):
                board[start[i][1][0]][start[i][1][1]] = current
                printBoard(board, size)

                current -= 1
                start[i][1][0] += start[i][2][0]
                start[i][1][1] += start[i][2][1]

        corners = [[board[TL[0]][TL[1]], [TL[0]-1, TL[1]-1]],
                   [board[TR[0]][TR[1]], [TR[0]-1, TR[1]+1]],
                   [board[BL[0]][BL[1]], [BL[0]+1, BL[1]-1]],
                   [board[BR[0]][BR[1]], [BR[0]+1, BR[1]+1]]]

        corners.sort(key=itemgetter(0), reverse=False)

        for i in range(4):
            board[corners[i][1][0]][corners[i][1][1]] = current
            printBoard(board, size)

            current -= 1

        TL = (TL[0]-1, TL[1]-1)
        TR = (TR[0]-1, TR[1]+1)
        BL = (BL[0]+1, BL[1]-1)
        BR = (BR[0]+1, BR[1]+1)

    print(board)
    return board


def placeBlocksAlgorithmOdd(board, size):
    center = int((size)/2)
    current = size * size
    board[center][center] = current
    printBoard(board, size)

    current -= 1
    board[center-1][center] = current
    printBoard(board, size)

    current -= 1
    board[center][center-1] = current
    printBoard(board, size)

    current -= 1
    board[center+1][center] = current
    printBoard(board, size)

    current -= 1
    board[center][center+1] = current
    printBoard(board, size)

    current -= 1
    board[center+1][center-1] = current
    printBoard(board, size)

    current -= 1
    board[center+1][center+1] = current
    printBoard(board, size)

    current -= 1
    board[center-1][center+1] = current
    printBoard(board, size)

    current -= 1
    board[center-1][center-1] = current
    printBoard(board, size)

    current -= 1

    TL = (center-1, center-1)
    TR = (center-1, center+1)
    BL = (center+1, center-1)
    BR = (center+1, center+1)

    for layer in range(center - 1, 0, -1):
        start = [[board[TL[0]][TL[1]], [TL[0] - 1, TL[1]], [0, 1]],
                 [board[TR[0]][TR[1]], [TR[0], TR[1] + 1], [1, 0]],
                 [board[BL[0]][BL[1]], [BL[0], BL[1] - 1], [-1, 0]],
                 [board[BR[0]][BR[1]], [BR[0] + 1, BR[1]], [0, -1]]]
        start.sort(key=itemgetter(0), reverse=False)

        layer_length = size - (2 * layer)

        for _ in range(layer_length):
            for i in range(4):
                board[start[i][1][0]][start[i][1][1]] = current
                printBoard(board, size)

                current -= 1
                start[i][1][0] += start[i][2][0]
                start[i][1][1] += start[i][2][1]

        corners = [[board[TL[0]][TL[1]], [TL[0]-1, TL[1]-1]],
                   [board[TR[0]][TR[1]], [TR[0]-1, TR[1]+1]],
                   [board[BL[0]][BL[1]], [BL[0]+1, BL[1]-1]],
                   [board[BR[0]][BR[1]], [BR[0]+1, BR[1]+1]]]

        corners.sort(key=itemgetter(0), reverse=False)

        for i in range(4):
            board[corners[i][1][0]][corners[i][1][1]] = current
            printBoard(board, size)

            current -= 1

        TL = (TL[0]-1, TL[1]-1)
        TR = (TR[0]-1, TR[1]+1)
        BL = (BL[0]+1, BL[1]-1)
        BR = (BR[0]+1, BR[1]+1)

    print(board)
    return board


def printBoard(board, size):
    for row in board:
        print("\n")
        for _ in row:
            print(str(_).rjust(4, ' '), end=" ")
    print("\n\n")
    cog = calcCOG(board)
    balanced = checkBalance(size, cog)
    print('Center of Gravity: ', end=" ")
    print(cog)
    if balanced:
        print("Balanced!")
    else:
        print("Out of Balance!")
    print("--------------------------------------------")


if __name__ == "__main__":
    #main()
    printBoard([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 4)
