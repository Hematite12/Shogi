from Constants import *

class Piece:
    def __init__(self, side, piece, x, y, imgs):
        self.moved = False
        self.x = x
        self.y = y
        self.side = side
        self.selected = False
        self.origPos = (x, y)
        self.piece = piece
        self.P,self.L,self.N,self.S,self.G,self.K,self.R,self.B,self.PP, \
        self.PL,self.PN,self.PS,self.PR,self.PB, \
        self.RP,self.RL,self.RN,self.RS,self.RG,self.RK,self.RR,self.RB,self.RPP, \
        self.RPL,self.RPN,self.RPS,self.RPR,self.RPB = imgs
    
    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def select(self):
        self.origPos = (self.x, self.y)
        self.selected = True
    
    def deselect(self):
        self.selected = False
        self.x = self.origPos[0]
        self.y = self.origPos[1]
    
    def showImage(self, img):
        if not self.selected:
            image(img,self.x*CELLDIM+MARGIN+CELLMARGIN,self.y*CELLDIM+MARGIN+CELLMARGIN,\
                  CELLDIM-2*CELLMARGIN,CELLDIM-2*CELLMARGIN)
        else:
            image(img, self.x-(CELLDIM-2*CELLMARGIN)//2, self.y-(CELLDIM-2*CELLMARGIN)//2,\
                  CELLDIM-2*CELLMARGIN, CELLDIM-2*CELLMARGIN)
    
    def showPromotionImage(self, x, y):
        pass
    
    def show(self):
        if self.side == "bot":
            if self.piece == "lance":
                self.showImage(self.L)
            elif self.piece == "knight":
                self.showImage(self.N)
            elif self.piece == "silver":
                self.showImage(self.S)
            elif self.piece == "gold":
                self.showImage(self.G)
            elif self.piece == "king":
                self.showImage(self.K)
            elif self.piece == "pawn":
                self.showImage(self.P)
            elif self.piece == "bishop":
                self.showImage(self.B)
            elif self.piece == "rook":
                self.showImage(self.R)
            elif self.piece == "tokin":
                self.showImage(self.PP)
            elif self.piece == "horse":
                self.showImage(self.PB)
            elif self.piece == "dragon":
                self.showImage(self.PR)
            elif self.piece == "lancePro":
                self.showImage(self.PL)
            elif self.piece == "knightPro":
                self.showImage(self.PN)
            elif self.piece == "silverPro":
                self.showImage(self.PS)
        else:
            if self.piece == "lance":
                self.showImage(self.RL)
            elif self.piece == "knight":
                self.showImage(self.RN)
            elif self.piece == "silver":
                self.showImage(self.RS)
            elif self.piece == "gold":
                self.showImage(self.RG)
            elif self.piece == "king":
                self.showImage(self.RK)
            elif self.piece == "pawn":
                self.showImage(self.RP)
            elif self.piece == "bishop":
                self.showImage(self.RB)
            elif self.piece == "rook":
                self.showImage(self.RR)
            elif self.piece == "tokin":
                self.showImage(self.RPP)
            elif self.piece == "horse":
                self.showImage(self.RPB)
            elif self.piece == "dragon":
                self.showImage(self.RPR)
            elif self.piece == "lancePro":
                self.showImage(self.RPL)
            elif self.piece == "knightPro":
                self.showImage(self.RPN)
            elif self.piece == "silverPro":
                self.showImage(self.RPS)
    
    def promote(self):
        if self.piece == "pawn":
            self.piece = "tokin"
        elif self.piece == "lance":
            self.piece = "lancePro"
        elif self.piece == "knight":
            self.piece = "knightPro"
        elif self.piece == "silver":
            self.piece = "silverPro"
        elif self.piece == "bishop":
            self.piece = "horse"
        elif self.piece == "rook":
            self.piece = "dragon"
    
    
    
    
    
    
    
    
    
    
    
    
    