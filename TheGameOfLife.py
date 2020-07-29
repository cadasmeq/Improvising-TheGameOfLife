import numpy as np
import matplotlib.pyplot as plt

epochs = 5
width, height = 30, 30
board = np.zeros([height, width])

# Player Cell
board[21, 21] = 1
board[22, 22] = 1
board[22, 23] = 1
board[21, 23] = 1
board[20, 23] = 1
plt.ion()

while 1:

    plt.imshow(board)
    plt.show()
    plt.pause(0.1) 

    newBoard = np.copy(board)        

    for y in range(0, height):
        for x in range(0, width):

            n_neigh = board[(x-1) % width, (y-1) % height]+ \
                    board[(x) % width, (y-1) % height]+ \
                    board[(x+1) % width, (y-1) % height]+ \
                    board[(x-1) % width, (y) % height]+ \
                    board[(x+1) % width, (y) % height]+ \
                    board[(x-1) % width, (y+1) % height]+ \
                    board[(x) % width, (y+1) % height]+ \
                    board[(x+1) % width, (y+1) % height]

            if board[x, y] == 0 and n_neigh == 3:
                newBoard[x, y] = 1

            if board[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newBoard[x, y] = 0
            
    board = newBoard

    




        






