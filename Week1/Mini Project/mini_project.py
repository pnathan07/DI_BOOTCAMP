#Mini-Projet

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_input(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move in '123456789':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("This position is already occupied.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def play():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    for turn in range(9):
        display_board(board)
        row, col = player_input(current_player)
        board[row][col] = current_player
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    display_board(board)
    print("The game is a tie!")

play()
