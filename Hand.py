from Constants import *
from Piece import *

class Hand:
    def __init__(self, side, imgs):
        self.side = side
        self.imgs = imgs
        self.x = MARGIN + 5
        if self.side == "bot":
            self.y = MARGIN+5+CELLDIM*9
        elif self.side == "top":
            self.y = 5
        self.display = [[],[],[],[],[],[],[]]
        
        self.incrementVal = 75
        
        self.pawnDisplay = Piece(self.side, "pawn", 0, 0, self.imgs)
        self.bishopDisplay = Piece(self.side, "bishop", 0, 0, self.imgs)
        self.rookDisplay = Piece(self.side, "rook", 0, 0, self.imgs)
        self.lanceDisplay = Piece(self.side, "lance", 0, 0, self.imgs)
        self.knightDisplay = Piece(self.side, "knight", 0, 0, self.imgs)
        self.silverDisplay = Piece(self.side, "silver", 0, 0, self.imgs)
        self.goldDisplay = Piece(self.side, "gold", 0, 0, self.imgs)
        
        self.pieceDisplays = [self.pawnDisplay, self.lanceDisplay, self.knightDisplay, 
                              self.silverDisplay, self.goldDisplay, self.bishopDisplay, 
                              self.rookDisplay]
        
        yPosPiece = self.y + 5
        for i in range(len(self.pieceDisplays)):
            self.pieceDisplays[i].setPos(self.x+i*self.incrementVal+5,yPosPiece)
            self.pieceDisplays[i].origPos = (self.x+i*self.incrementVal+5,yPosPiece)
    
    def show(self):
        fill(*HANDCOLOR)
        rect(self.x, self.y, HANDWIDTH, HANDHEIGHT)
        fill(255)
        yPosNum = self.y + HANDHEIGHT - 10
        for i in range(len(self.display)):
            numPieces = len(self.display[i])
            if numPieces > 0:
                self.pieceDisplays[i].showAtPos()
                xPosNum = self.x + i * self.incrementVal + 60
                textSize(15)
                text(str(numPieces), xPosNum, yPosNum)
    
    def addPiece(self, piece):
        piece.dePromote()
        piece.side = self.side
        if piece.piece == "pawn": self.display[0].append(piece)
        elif piece.piece == "lance": self.display[1].append(piece)
        elif piece.piece == "knight": self.display[2].append(piece)
        elif piece.piece == "silver": self.display[3].append(piece)
        elif piece.piece == "gold": self.display[4].append(piece)
        elif piece.piece == "bishop": self.display[5].append(piece)
        elif piece.piece == "rook": self.display[6].append(piece)
    
    def removePiece(self, piece):
        for i in range(len(self.display)):
            for p in range(len(self.display[i])):
                    self.display[i] = self.display[i][:p]+self.display[i][p+1:]
    
    def removeIndex(self, i):
        if len(self.display[i]) > 0:
            temp = self.display[i][0]
            self.display[i] = self.display[i][1:]
            return temp
    
    def checkClick(self, x, y):
        xMax = self.x + 8 * self.incrementVal
        if x>self.x+5 and x<xMax and y>self.y+5 and y<self.y+HANDHEIGHT-5:
            choice = (x - self.x - 5) // self.incrementVal
            return self.removeIndex(choice)