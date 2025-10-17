from dataclasses import dataclass
from board import Board 

@dataclass
class Player:
    name: str
    symbol: str

    def get_move(self, board:Board ) -> int:
        raise NotImplementedError

class HumanPlayer(Player):
    def get_move(self, board:Board ) -> int:
        legal = board.legal_moves()
        while True:
            try:
                idx = int(input(f"{self.name} - {self.symbol.capitalize()} Enter Your number ").strip())
                if idx in legal :
                    return idx
                print(f"Cell {idx} is not legal, Legal moves: {legal}")
            except (ValueError, EOFError):
                print("Please enter a vaild integer between 0 and 8.")
                
if __name__ == "__main__":
    human = HumanPlayer()
    board = Board()
    print(board)
    print(human.get_move(board))