from Constants import *
from Board import *

def setup():
    size(CANVASSIZE, CANVASSIZE)
    global b, P, L, N, S, G, K, R, B, PP, PL, PN, PS, PR, PB
    P = loadImage("Pawn.png")
    L = loadImage("Lance.png")
    N = loadImage("Knight.png")
    S = loadImage("Silver.png")
    G = loadImage("Gold.png")
    K = loadImage("King.png")
    R = loadImage("Rook.png")
    B = loadImage("Bishop.png")
    PP = loadImage("Tokin.png")
    PL = loadImage("ProLance.png")
    PN = loadImage("ProKnight.png")
    PS = loadImage("ProSilver.png")
    PR = loadImage("Dragon.png")
    PB = loadImage("Horse.png")
    RP = loadImage("PawnR.png")
    RL = loadImage("LanceR.png")
    RN = loadImage("KnightR.png")
    RS = loadImage("SilverR.png")
    RG = loadImage("GoldR.png")
    RK = loadImage("KingR.png")
    RR = loadImage("RookR.png")
    RB = loadImage("BishopR.png")
    RPP = loadImage("TokinR.png")
    RPL = loadImage("ProLanceR.png")
    RPN = loadImage("ProKnightR.png")
    RPS = loadImage("ProSilverR.png")
    RPR = loadImage("DragonR.png")
    RPB = loadImage("HorseR.png")
    imgs = (P, L, N, S, G, K, R, B, PP, PL, PN, PS, PR, PB, \
            RP, RL, RN, RS, RG, RK, RR, RB, RPP, RPL, RPN, RPS, RPR, PB)
    background(100)
    b = Board(imgs)
    b.show()

def draw():
    background(100)
    b.show()
    if b.SELECTED != None:
        b.SELECTED.setPos(mouseX, mouseY)
        b.SELECTED.show()
    if b.PROMOTING != None:
        b.showPromote()

def mousePressed():
    if b.SELECTED != None:
        b.checkDeselect(mouseX, mouseY)
    elif b.PROMOTING != None:
        b.checkPromotionSelection(mouseX, mouseY)
    else:
        b.checkSelect(mouseX, mouseY)