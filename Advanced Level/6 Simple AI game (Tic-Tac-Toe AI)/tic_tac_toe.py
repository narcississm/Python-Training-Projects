import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Satırlar ve sütunlar
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Çaprazlar
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            row = int(input("Satır (0-2): "))
            col = int(input("Sütun (0-2): "))
            if (row in range(3) and col in range(3)) and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Geçersiz hamle, tekrar deneyin.")
        except ValueError:
            print("Lütfen geçerli sayı girin.")

def ai_move(board):
    empty = get_empty_positions(board)
    # Basit AI: Rastgele seçim
    move = random.choice(empty)
    board[move[0]][move[1]] = "O"
    print(f"AI hamlesi: Satır {move[0]}, Sütun {move[1]}")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    print("Tic Tac Toe - X (Sen) vs O (AI)")

    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            player_move(board)
            if check_winner(board, "X"):
                print_board(board)
                print("Tebrikler, kazandınız!")
                return
        else:
            ai_move(board)
            if check_winner(board, "O"):
                print_board(board)
                print("AI kazandı!")
                return

    print_board(board)
    print("Oyun berabere bitti.")

if __name__ == "__main__":
    tic_tac_toe()
