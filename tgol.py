import numpy as np
import matplotlib.pyplot as plt

debug = 1
epochs = 5
width, height = 100, 100
board = np.zeros([height, width])

# Player Cell
board[50:55, 48:52] = 1
board[49:53, 49] = 1
board[43:55, 48:50] = 1
plt.ion()

while 1:

    if debug == 1:
     
        plt.imshow(board)
        plt.show()
        plt.pause(0.00001)
        

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

    




        






