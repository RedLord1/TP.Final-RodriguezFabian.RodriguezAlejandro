import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def player_move(board):
    while True:
        move = input("Selecciona tu movimiento (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Espacio ya elegido. Selecciona otro.")
        else:
            print("Movimiento inválido, elige un número entre 1 y 9.")

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Bienvenido a Ta-Te-Ti!")
    print_board(board)

    while True:
        # Player move
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Bien jugado! Felicidades!!")
            break
        if is_board_full(board):
            print("Oh, es un empate")
            break

        # Computer move
        computer_move(board)
        print("La IA juega:")
        print_board(board)
        if check_winner(board, 'O'):
            print("Mala suerte, Ganó la IA")
            break
        if is_board_full(board):
            print("Es un Empate")
            break

if __name__ == "__main__":
    main()
