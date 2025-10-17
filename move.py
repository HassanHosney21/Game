from typing import List, Optional
from abc import ABC,abstractmethod
from board import Board
import random

class MoveStrategy(ABC):
    @abstractmethod
    def choose(self, board: Board, choose: str):
        pass      

class RandomMove(MoveStrategy):
    def choose(self, board: Board, choose: str):
        return random.choice(board.legal_moves())






