from Constants import *
from Piece import *

class Hand:
    def __init__(self, side):
        self.side = side
        self.pawns,self.rooks,self.bishops,self.lances,self.knights,\
        self.silvers,self.golds = ([],[],[],[],[],[],[])
        self.display = [self.pawns,self.rooks,self.bishops,self.lances,self.knights,\
        self.silvers,self.golds]
    
    def show(self):
        pass
    
    def addPiece(self, piece):
        piece.dePromote()
        piece.side = self.side
        if piece.piece == "pawn": self.pawns.append(piece)
        elif piece.piece == "rook": self.rooks.append(piece)
        elif piece.piece == "bishop": self.bishops.append(piece)
        elif piece.piece == "lance": self.lances.append(piece)
        elif piece.piece == "knight": self.knights.append(piece)
        elif piece.piece == "silver": self.silvers.append(piece)
        elif piece.piece == "gold": self.golds.append(piece)
    
    def removePiece(self, piece):
        for i in range(len(self.display)):
            for p in range(len(self.display[i])):
                    self.display[i] = self.display[i][:p]+self.display[i][p+1:]