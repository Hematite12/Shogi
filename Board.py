from BoardCell import *
from Constants import *
from Piece import *
from Hand import *

class Board:
    def __init__(self, imgs):
        self.playing = "bot"
        self.imgs = imgs
        self.SELECTED = None
        self.PROMOTING = None
        self.matrix = [[BoardCell(x, y) for x in range(9)] for y in range(9)]
        self.placePieces()
        self.promotionData = None
        self.botHand = Hand("bot")
        self.topHand = Hand("top")
    
    def changePlayer(self):
        if self.playing == "bot":
            self.playing = "top"
        else:
            self.playing = "bot"
    
    def placePieces(self):
        for x in range(9):
            for y in range(9):
                if y < 5:
                    side = "top"
                else:
                    side = "bot"
                if BOARD[y][x]!=None:
                    if BOARD[y][x]=="L":
                        p = Piece(side, "lance", x, y, self.imgs)
                    elif BOARD[y][x]=="N":
                        p = Piece(side, "knight", x, y, self.imgs)
                    elif BOARD[y][x]=="S":
                        p = Piece(side, "silver", x, y, self.imgs)
                    elif BOARD[y][x]=="G":
                        p = Piece(side, "gold", x, y, self.imgs)
                    elif BOARD[y][x]=="K":
                        p = Piece(side, "king", x, y, self.imgs)
                    elif BOARD[y][x]=="P":
                        p = Piece(side, "pawn", x, y, self.imgs)
                    elif BOARD[y][x]=="B":
                        p = Piece(side, "bishop", x, y, self.imgs)
                    elif BOARD[y][x]=="R":
                        p = Piece(side, "rook", x, y, self.imgs)
                    self.matrix[y][x].placePiece(p)
    
    def show(self):
        for x in range(9):
            for y in range(9):
                self.matrix[y][x].show()
    
    def unmarkAll(self):
        for x in range(9):
            for y in range(9):
                self.matrix[y][x].unmark()
    
    def setAttackMove(self, x, y, friendly):
        square = self.matrix[y][x]
        if square.piece == None:
            square.movable = True
        else:
            if square.piece.side != friendly:
                square.attackable = True
    
    def applyMovesMat(self, x, y, mat, friendly):
        xDist = len(mat[0]) // 2
        yDist = len(mat) // 2
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                xSquare = x+i-xDist
                ySquare = y+j-yDist
                if xSquare>=0 and xSquare<9 and ySquare>=0 and ySquare<9:
                    if mat[j][i] == "move":
                        self.setAttackMove(xSquare, ySquare, friendly)
    
    def applyKnightJump(self, x, y, mat, friendly):
        xDist = len(mat[0]) // 2
        yDist = len(mat) // 2
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                xSquare = x+i-xDist
                ySquare = y+j-yDist
                if xSquare>=0 and xSquare<9 and ySquare>=0 and ySquare<9:
                    if mat[j][i] == "move":
                        self.setAttackMove(x+i-xDist, y+j-yDist, friendly)
    
    def unvisitAll(self):
        for x in range(9):
            for y in range(9):
                self.matrix[y][x].visited = False
    
    def checkCellSight(self, x, y):
        cell = self.matrix[y][x]
        cell.visited = True
        dirX = self.SELECTED.origPos[0] - x
        dirY = self.SELECTED.origPos[1] - y
        if dirX == 0 and dirY == 0:
            return True
        if dirX > 0:
            newX = x + 1
        elif dirX == 0:
            newX = x
        elif dirX < 0:
            newX = x - 1
        if dirY > 0:
            newY = y + 1
        elif dirY == 0:
            newY = y
        elif dirY < 0:
            newY = y - 1
        check = self.checkCellSight(newX, newY)
        if not check:
            cell.movable = False
            cell.attackable = False
            return False
        elif cell.piece != None:
            return False
        else:
            return True
    
    def lineOfSight(self):
        for x in range(9):
            for y in range(9):
                if not self.matrix[y][x].visited:
                    self.checkCellSight(x, y)
        self.unvisitAll()
    
    def markMoves(self, x, y, piece):
        if piece.side == "bot":
            if piece.piece == "pawn":
                self.applyMovesMat(x, y, PAWNBOT, piece.side)
            elif piece.piece == "lance":
                self.applyMovesMat(x, y, LANCEBOT, piece.side)
            elif piece.piece == "silver":
                self.applyMovesMat(x, y, SILVERBOT, piece.side)
            elif piece.piece in ["gold","tokin","lancePro","knightPro","silverPro"]:
                self.applyMovesMat(x, y, GOLDBOT, piece.side)
            elif piece.piece == "knight":
                self.applyKnightJump(x, y, KNIGHTBOT, piece.side)
        elif piece.side == "top":
            if piece.piece == "pawn":
                self.applyMovesMat(x, y, PAWNTOP, piece.side)
            elif piece.piece == "lance":
                self.applyMovesMat(x, y, LANCETOP, piece.side)
            elif piece.piece == "silver":
                self.applyMovesMat(x, y, SILVERTOP, piece.side)
            elif piece.piece in ["gold","tokin","lancePro","knightPro","silverPro"]:
                self.applyMovesMat(x, y, GOLDTOP, piece.side)
            elif piece.piece == "knight":
                self.applyKnightJump(x, y, KNIGHTTOP, piece.side)
        if piece.piece == "king":
            self.applyMovesMat(x, y, KING, piece.side)
        elif piece.piece == "bishop":
            self.applyMovesMat(x, y, BISHOP, piece.side)
        elif piece.piece == "rook":
            self.applyMovesMat(x, y, ROOK, piece.side)
        elif piece.piece == "horse":
            self.applyMovesMat(x, y, HORSE, piece.side)
        elif piece.piece == "dragon":
            self.applyMovesMat(x, y, DRAGON, piece.side)
        if piece.piece != "knight":
            self.lineOfSight()
    
    def checkSelect(self, x, y):
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            xSquare = (x-MARGIN) // CELLDIM
            ySquare = (y-MARGIN) // CELLDIM
            piece = self.matrix[ySquare][xSquare].piece
            if piece != None and piece.side == self.playing:
                self.matrix[ySquare][xSquare].selected = True
                self.SELECTED = piece
                piece.select()
                self.markMoves(xSquare, ySquare, piece)
    
    def checkDeselect(self, x, y):
        self.SELECTED.deselect()
        if x>MARGIN and x<CANVASSIZE-MARGIN and y>MARGIN and y<CANVASSIZE-MARGIN:
            xSquare = (x-MARGIN) // CELLDIM
            ySquare = (y-MARGIN) // CELLDIM
            cell = self.matrix[ySquare][xSquare]
            if cell.attackable or cell.movable:
                cell.placePiece(self.SELECTED)
                self.SELECTED.moved = True
                self.matrix[self.SELECTED.origPos[1]][self.SELECTED.origPos[0]].piece = None
                self.changePlayer()
                self.checkPromote(self.SELECTED)
        self.SELECTED = None
        self.unmarkAll()
    
    def checkPromote(self, piece):
        if piece.side == "bot":
            if piece.piece in ["pawn", "lance"]:
                if piece.y == 0:
                    piece.promote()
                elif piece.y < 3:
                    self.PROMOTING = piece
                    self.getPromotionData()
            elif piece.piece == "knight":
                if piece.y < 2:
                    piece.promote()
                elif piece.y == 2:
                    self.PROMOTING = piece
                    self.getPromotionData()
            elif piece.piece in ["bishop", "rook", "silver"]:
                if piece.y < 3:
                    self.PROMOTING = piece
                    self.getPromotionData()
        elif piece.side == "top":
            if piece.piece in ["pawn", "lance"]:
                if piece.y == 8:
                    piece.promote()
                elif piece.y > 5:
                    self.PROMOTING = piece
                    self.getPromotionData()
            elif piece.piece == "knight":
                if piece.y > 6:
                    piece.promote()
                elif piece.y == 6:
                    self.PROMOTING = piece
                    self.getPromotionData()
            elif piece.piece in ["bishop", "rook", "silver"]:
                if piece.y > 5:
                    self.PROMOTING = piece
                    self.getPromotionData()
    
    def getPromotionData(self):
        unPromoted = Piece(self.PROMOTING.side,self.PROMOTING.piece,0,0,self.imgs)
        promoted = Piece(self.PROMOTING.side,self.PROMOTING.piece,0,0,self.imgs)
        promoted.promote()
        self.promotionData = (unPromoted, promoted)
    
    def showPromote(self):
        fill(*PROMOTION)
        rect(width//2-BOXWIDTH//2,height//2-BOXHEIGHT//2,BOXWIDTH,BOXHEIGHT)
        fill(*OPTIONCOLOR)
        rect(Xpos1, Ypos, OPTIONDIM, OPTIONDIM)
        rect(Xpos2, Ypos, OPTIONDIM, OPTIONDIM)
        self.promotionData[0].showPromotionImage(Xpos1, Ypos)
        self.promotionData[1].showPromotionImage(Xpos2, Ypos)
    
    def checkPromotionSelection(self, x, y):
        if x>Xpos1 and x<Xpos2+OPTIONDIM and y>Ypos and y<Ypos+OPTIONDIM:
            if x<Xpos1+OPTIONDIM:
                self.PROMOTING = None
            elif x>Xpos2:
                self.PROMOTING.promote()
                self.PROMOTING = None
    
    
    
    
    
    
    
    
    
    
    