from Driver import Driver
from minimax import getBestMove

driver = Driver()

moves_str = ['UP', 'DOWN', 'LEFT', 'RIGHT']
moves_count = 1

while True:
    board = driver.getBoard()
    if board.isGameOver():
        print("Game Over!")
        break
    moveCode = getBestMove(board, 5) # Adjust depth here as desired
    print(f'Move #{moves_count}: {moves_str[moveCode]}')
    driver.move(moveCode)
    moves_count += 1