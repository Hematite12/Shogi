MARGIN = 20
CELLDIM = 60
CELLMARGIN = 5
CANVASSIZE = CELLDIM*9+2*MARGIN

CELL = (255,200,160)
CELLATTACKABLE = (255, 140, 140)
CELLMOVABLE = (220, 200, 255)
CELLSELECTED = (220, 255, 155)

PROMOTION = (220, 130, 220, 150)
BOXWIDTH = 150
BOXHEIGHT = 70
OPTIONCOLOR = (100, 0, 100)
OPTIONDIM = 50

Xpos1 = (BOXWIDTH-2*OPTIONDIM)//3+CANVASSIZE//2-BOXWIDTH//2
Xpos2 = 2*(BOXWIDTH-2*OPTIONDIM)//3+CANVASSIZE//2-BOXWIDTH//2+OPTIONDIM
Ypos = (BOXHEIGHT-OPTIONDIM)//2+CANVASSIZE//2-BOXHEIGHT//2

x = None
M = "move"
S = "start"

BOARD = [["L", "N", "S", "G", "K", "G", "S", "N", "L" ],
         [None,"R", None,None,None,None,None,"B", None],
         ["P", "P", "P", "P", "P", "P", "P", "P", "P" ],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         ["P", "P", "P", "P", "P", "P", "P", "P", "P" ],
         [None,"B", None,None,None,None,None,"R", None],
         ["L", "N", "S", "G", "K", "G", "S", "N", "L" ]]

PAWNBOT = [[M],
           [S],
           [x]]

PAWNTOP = [[X],
           [S],
           [M]]

KNIGHTBOT = [[M,x,M],
             [x,x,x],
             [x,S,x],
             [x,x,x],
             [x,x,x]]

KNIGHTTOP = [[x,x,x],
             [x,x,x],
             [x,S,x],
             [x,x,x],
             [M,x,M]]

SILVERBOT = [[M,M,M],
             [x,S,x],
             [M,x,M]]

SILVERTOP = [[M,x,M],
             [x,S,x],
             [M,M,M]]

GOLDBOT = [[M,M,M],
           [M,S,M],
           [x,M,x]]

GOLDTOP = [[x,M,x],
           [M,S,M],
           [M,M,M]]

KING = [[M,M,M],
        [M,S,M],
        [M,M,M]]

LANCEBOT = [[M],
            [M],
            [M],
            [M],
            [M],
            [M],
            [M],
            [M],
            [S],
            [x],
            [x],
            [x],
            [x],
            [x],
            [x],
            [x],
            [x]]

LANCETOP = [[x],
            [x],
            [x],
            [x],
            [x],
            [x],
            [x],
            [x],
            [S],
            [M],
            [M],
            [M],
            [M],
            [M],
            [M],
            [M],
            [M]]

BISHOP = [[M,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,M],
          [x,M,x,x,x,x,x,x,x,x,x,x,x,x,x,M,x],
          [x,x,M,x,x,x,x,x,x,x,x,x,x,x,M,x,x],
          [x,x,x,M,x,x,x,x,x,x,x,x,x,M,x,x,x],
          [x,x,x,x,M,x,x,x,x,x,x,x,M,x,x,x,x],
          [x,x,x,x,x,M,x,x,x,x,x,M,x,x,x,x,x],
          [x,x,x,x,x,x,M,x,x,x,M,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,x,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,S,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,x,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,M,x,x,x,M,x,x,x,x,x,x],
          [x,x,x,x,x,M,x,x,x,x,x,M,x,x,x,x,x],
          [x,x,x,x,M,x,x,x,x,x,x,x,M,x,x,x,x],
          [x,x,x,M,x,x,x,x,x,x,x,x,x,M,x,x,x],
          [x,x,M,x,x,x,x,x,x,x,x,x,x,x,M,x,x],
          [x,M,x,x,x,x,x,x,x,x,x,x,x,x,x,M,x],
          [M,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,M]]

HORSE  = [[M,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,M],
          [x,M,x,x,x,x,x,x,x,x,x,x,x,x,x,M,x],
          [x,x,M,x,x,x,x,x,x,x,x,x,x,x,M,x,x],
          [x,x,x,M,x,x,x,x,x,x,x,x,x,M,x,x,x],
          [x,x,x,x,M,x,x,x,x,x,x,x,M,x,x,x,x],
          [x,x,x,x,x,M,x,x,x,x,x,M,x,x,x,x,x],
          [x,x,x,x,x,x,M,x,x,x,M,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,M,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,S,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,M,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,M,x,x,x,M,x,x,x,x,x,x],
          [x,x,x,x,x,M,x,x,x,x,x,M,x,x,x,x,x],
          [x,x,x,x,M,x,x,x,x,x,x,x,M,x,x,x,x],
          [x,x,x,M,x,x,x,x,x,x,x,x,x,M,x,x,x],
          [x,x,M,x,x,x,x,x,x,x,x,x,x,x,M,x,x],
          [x,M,x,x,x,x,x,x,x,x,x,x,x,x,x,M,x],
          [M,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,M]]

ROOK = [[x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [M,M,M,M,M,M,M,M,S,M,M,M,M,M,M,M,M],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
        [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x]]

DRAGON = [[x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,M,M,M,x,x,x,x,x,x,x],
          [M,M,M,M,M,M,M,M,S,M,M,M,M,M,M,M,M],
          [x,x,x,x,x,x,x,M,M,M,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x],
          [x,x,x,x,x,x,x,x,M,x,x,x,x,x,x,x,x]]