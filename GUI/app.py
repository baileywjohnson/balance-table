import eel
import time
from operator import itemgetter
eel.init('web')


@eel.expose
def start_table(size):
    print("Building table of size " + size)
    board = [[0 for i in range(int(size))] for j in range(int(size))]
    if int(size) % 2 == 0:
        board = placeBlocksAlgorithmEven(board, int(size))
    else:
        board = placeBlocksAlgorithmOdd(board, int(size))


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
    updateJSBoard(board, size)

    current -= 1
    board[layers][layers] = current
    updateJSBoard(board, size)

    current -= 1
    board[layers - 1][layers] = current
    updateJSBoard(board, size)

    current -= 1
    board[layers][layers - 1] = current
    updateJSBoard(board, size)

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
                updateJSBoard(board, size)

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
            updateJSBoard(board, size)

            current -= 1

        TL = (TL[0]-1, TL[1]-1)
        TR = (TR[0]-1, TR[1]+1)
        BL = (BL[0]+1, BL[1]-1)
        BR = (BR[0]+1, BR[1]+1)

    return board


def placeBlocksAlgorithmOdd(board, size):
    center = int((size)/2)
    current = size * size
    board[center][center] = current
    updateJSBoard(board, size)

    current -= 1
    board[center-1][center] = current
    updateJSBoard(board, size)

    current -= 1
    board[center][center-1] = current
    updateJSBoard(board, size)

    current -= 1
    board[center+1][center] = current
    updateJSBoard(board, size)

    current -= 1
    board[center][center+1] = current
    updateJSBoard(board, size)

    current -= 1
    board[center+1][center-1] = current
    updateJSBoard(board, size)

    current -= 1
    board[center+1][center+1] = current
    updateJSBoard(board, size)

    current -= 1
    board[center-1][center+1] = current
    updateJSBoard(board, size)

    current -= 1
    board[center-1][center-1] = current
    updateJSBoard(board, size)

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
                updateJSBoard(board, size)

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
            updateJSBoard(board, size)

            current -= 1

        TL = (TL[0]-1, TL[1]-1)
        TR = (TR[0]-1, TR[1]+1)
        BL = (BL[0]+1, BL[1]-1)
        BR = (BR[0]+1, BR[1]+1)

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
    time.sleep(2)


def updateJSBoard(board, size):
    js_board = []
    for row in board:
        for column in row:
            js_board.append(column)
    cog = calcCOG(board)
    balanced = checkBalance(size, cog)
    eel.updateBoard(js_board, cog, balanced)
    time.sleep(1)


eel.start('main.html', block=False)
while True:
    eel.sleep(10)
