# imports the relevant libraries
import pygame as pg
import sys
import time

# declares global variables
WIDTH, HEIGHT = 400, 400
GAME_NAME = 'Tic-Tac-Toe'
BOARD_COLOUR = (244, 235, 208)

pg.font.init()
FONT = pg.font.Font("motley.ttf", 20)
DRAW_COLOUR = (0,0,0)
FPS = 30

game_state = 'playing'
turn = 'X' # X always starts the game
winner = None

# 3 by 3 game board
board = [[None]*3, [None]*3, [None]*3]

# initializes the game window
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(GAME_NAME)

# keeps track of time
clock = pg.time.Clock()

# loads in key visual assets
BOARD = pg.image.load("game_board.png")
X = pg.image.load("X_icon.png")
O = pg.image.load("O_icon.png")

# initial display window (blank game board)
def initial_window():
    pg.display.update()
    time.sleep(2)
    window.fill(BOARD_COLOUR)
    
    window.blit(BOARD, (50,50))
    update_caption()

# updates the caption indicating the game state
def update_caption():
    global game_state, turn
    
    if game_state == 'win':
        caption = winner + ' won!'
    elif game_state == 'draw':
        caption = 'Draw!'
    else:
        caption = turn + ' \'s turn'
    
    text = FONT.render(caption, True, DRAW_COLOUR)
    window.fill(BOARD_COLOUR, (160, 15, 100, 21))
    window.blit(text, (160, 15))
    
    pg.display.update()

# updates the game state
def update_game_state():
    global board, game_state
    
    # checking for a horizontal win
    for row in range(3):
        if ((board[row][0] == board[row][1] == board[row][2]) and board[row][0] != None):
            game_state = 'win'
            pg.draw.line(window, DRAW_COLOUR, (50, (row+1)*100),(350, (row+1)*100), 6)
            break
            
    # checking for a vertical win
    for col in range(3):
        if ((board[0][col] == board[1][col] == board[2][col]) and board[0][col] != None):
            game_state = 'win'
            pg.draw.line(window, DRAW_COLOUR, ((col+1)*100, 50),((col+1)*100, 350), 6)
            break
    
    # checking for a diagonal win
    if ((board[0][0] == board[1][1] == board[2][2]) and board[0][0] != None):
        game_state = 'win'
        pg.draw.line(window, DRAW_COLOUR, (100,100), (300, 300), 9)
    elif ((board[0][2] == board[1][1] == board[2][0]) and board[0][2] != None):
        game_state = 'win'
        pg.draw.line(window, DRAW_COLOUR, (300,100), (100,300), 9)
    
    # checking for a draw
    if (all([all(row) for row in board]) and game_state == 'playing'):
        game_state = 'draw'
    
    update_caption()

# if within the game board, draws an X or O (depending who's turn it is)
def drawXO(row, col):
    global board, turn, winner
    
    if row == 1:
        x_pos = 55
    elif row == 2:
        x_pos = 155
    else:
        x_pos = 255
    
    if col == 1:
        y_pos = 55
    elif col == 2:
        y_pos = 155
    else:
        y_pos = 255
        
    board[row-1][col-1] = turn
    
    if (turn == 'X'):
        window.blit(X, (y_pos, x_pos))
        turn = 'O'
        winner = 'X'
    else:
        window.blit(O, (y_pos, x_pos))
        turn = 'X'
        winner = 'O'

    pg.display.update()

# handles user mouse input
def user_input():
    x, y = pg.mouse.get_pos()
    
    # finding column of mouse click
    if (50 < x < 350):
        if ((x-50) < 100):
            col = 1
        elif ((x-50) < 200):
            col = 2
        else:
            col = 3
    else:
        col = None
    
    # finding row of mouse click
    if (50 < y < 350):
        if ((y-50) < 100):
            row = 1
        elif ((y-50) < 200):
            row = 2
        else:
            row = 3
    else:
        row = None
    
    if ((row != None) and (col != None) and board[row-1][col-1] is None):
        drawXO(row, col)
        update_game_state()
    
# resets key global variables, redraws blank board
def restart():
    global turn, game_state, winner, board
    
    time.sleep(1)
    turn = 'X'
    game_state = 'playing'
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
    initial_window()

initial_window()

#main game loop
while(True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_input()
            if (game_state == 'win' or game_state == 'draw'):
                restart()
    pg.display.update()
    clock.tick(FPS)
    
    
