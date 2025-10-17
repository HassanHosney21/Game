from player import Player, HumanPlayer
from board import Board
from helper import clear

class Game:
    def __init__(self, player_x: Player = HumanPlayer("Player X", "x"), player_o: Player = HumanPlayer("Player O", "o")):
        self.players = {
            "x": player_x,
            "o": player_o
        }
        self.board = Board()
        self.currunt_symbol = "x"  

    def switch(self):
        self.currunt_symbol = "o" if self.currunt_symbol == "x" else "x"

    def step(self):
        player = self.players[self.currunt_symbol]
        move = player.get_move(self.board)
        self.board.place(move, player.symbol)

    def run(self):
        while not self.board.is_terminal():
            print(self.board)
            self.step()
            self.switch()
            clear()            # optional
        winner = self.board.winner()
        print(self.board)
        if winner:
            print(f"The winner is: {self.players[winner].name}")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    x_name = input("Enter the Player X name: ")
    o_name = input("Enter the Player O name: ")
    game = Game(HumanPlayer(x_name, "x"), HumanPlayer(o_name, "o"))
    game.run()
