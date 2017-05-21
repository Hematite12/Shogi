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
        self.origPiece = piece
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
        marg = CELLMARGIN // 2
        image(self.getPic(),x+marg,y+marg,\
              OPTIONDIM-2*marg,OPTIONDIM-2*marg)
    
    def getPic(self):
        if self.side == "bot":
            if self.piece == "lance":
                return self.L
            elif self.piece == "knight":
                return self.N
            elif self.piece == "silver":
                return self.S
            elif self.piece == "gold":
                return self.G
            elif self.piece == "king":
                return self.K
            elif self.piece == "pawn":
                return self.P
            elif self.piece == "bishop":
                return self.B
            elif self.piece == "rook":
                return self.R
            elif self.piece == "tokin":
                return self.PP
            elif self.piece == "horse":
                return self.PB
            elif self.piece == "dragon":
                return self.PR
            elif self.piece == "lancePro":
                return self.PL
            elif self.piece == "knightPro":
                return self.PN
            elif self.piece == "silverPro":
                return self.PS
        else:
            if self.piece == "lance":
                return self.RL
            elif self.piece == "knight":
                return self.RN
            elif self.piece == "silver":
                return self.RS
            elif self.piece == "gold":
                return self.RG
            elif self.piece == "king":
                return self.RK
            elif self.piece == "pawn":
                return self.RP
            elif self.piece == "bishop":
                return self.RB
            elif self.piece == "rook":
                return self.RR
            elif self.piece == "tokin":
                return self.RPP
            elif self.piece == "horse":
                return self.RPB
            elif self.piece == "dragon":
                return self.RPR
            elif self.piece == "lancePro":
                return self.RPL
            elif self.piece == "knightPro":
                return self.RPN
            elif self.piece == "silverPro":
                return self.RPS
    
    def show(self):
        self.showImage(self.getPic())
    
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
    
    def dePromote(self):
        self.piece = self.origPiece
    
    
    
    
    
    
    
    
    
    
    
    