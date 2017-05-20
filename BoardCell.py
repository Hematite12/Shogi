from Constants import *
from Piece import *

class BoardCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None
        self.movable = False
        self.attackable = False
        self.visited = False
        self.selected = False
    
    def placePiece(self, piece):
        self.piece = piece
        self.piece.x = self.x
        self.piece.y = self.y
    
    def unmark(self):
        self.movable = False
        self.attackable = False
        self.selected = False
    
    def show(self):
        if self.attackable:
            fill(*CELLATTACKABLE)
        elif self.movable:
            fill(*CELLMOVABLE)
        elif self.selected:
            fill(*CELLSELECTED)
        else:
            fill(*CELL)
        rect(self.x*CELLDIM+MARGIN,self.y*CELLDIM+MARGIN,CELLDIM,CELLDIM)
        if self.piece!=None and not self.piece.selected:
            self.piece.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    