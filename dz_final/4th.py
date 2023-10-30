class Cell:
    def __init__(self):
        self.value = ' '

    def __str__(self):
        return self.value


class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.cells:
            print("|".join(str(cell) for cell in row))
            print("-" * 5)

    def is_full(self):
        return all(cell.value != ' ' for row in self.cells for cell in row)

    def make_move(self, row, col, player):
        if 0 <= row < 3 and 0 <= col < 3 and self.cells[row][col].value == ' ':
            self.cells[row][col].value = player.symbol
            return True
        return False

    def check_winner(self, player):
        for row in self.cells:
            if all(cell.value == player.symbol for cell in row):
                return True
        for col in range(3):
            if all(self.cells[row][col].value == player.symbol for row in range(3)):
                return True
        if all(self.cells[i][i].value == player.symbol for i in range(3)) or all(
                self.cells[i][2 - i].value == player.symbol for i in range(3)):
            return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name}, enter row (0, 1, 2): "))
                col = int(input(f"{self.name}, enter column (0, 1, 2): "))
                if board.make_move(row, col, self):
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")


def play_game():
    board = Board()
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    current_player = player1

    while not board.is_full():
        board.display()
        current_player.make_move(board)
        if board.check_winner(current_player):
            board.display()
            print(f"{current_player.name} wins!")
            break
        current_player = player1 if current_player == player2 else player2
    else:
        board.display()
        print("It's a draw!")


if __name__ == "__main__":
    play_game()