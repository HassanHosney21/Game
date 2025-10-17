from typing import List, Optional

class Board:
    """the game board form 0 to 8
        index mapping: 
         0|1|2
         3|4|5
         6|7|8 
    """
    WINNING_LINES = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (2,4,6),
        (0,4,8)
    ]

    def __init__(self, cells:Optional[List[Optional[str]]] = None) :
        self.cells = cells or [None] * 9
    
    def place(self, index: int, symbol:str):
        if not (0 <= index <= 8):
            raise ValueError("choose number bettwen 0 and 8")
        if self.cells[index] is not None:
            raise ValueError("this  place is not vaild")
        self.cells[index] = symbol

    def is_full(self)-> bool:
        return all(c is not None  for c in self.cells)
    
    def legal_moves(self) -> List[int]:
        return [index for index, value in enumerate(self.cells) if value is None]

    def winner(self) -> Optional[str]:
        for a, b, c in self.WINNING_LINES :
            if self.cells[a] and self.cells[a] ==  self.cells[b] ==  self.cells[c]:
                return self.cells[a]
        return None

    def is_terminal(self) -> bool:
        return self.winner() is not None or self.is_full()

    def __str__(self) -> str:
        def ch(i):
            return self.cells[i] if self.cells[i] is not None else str(i)
        rows = [
            f"{ch(0)} | {ch(1)} | {ch(2)}",
            f"{ch(3)} | {ch(4)} | {ch(5)}",
            f"{ch(6)} | {ch(7)} | {ch(8)}",
            ]
        return "\n--+---+--\n".join(rows)
    
if __name__ == "__main__":
    board = Board(cells=["x", None, None, "o", None, None, None,None, None])
    print(board)
    print(board.legal_moves())