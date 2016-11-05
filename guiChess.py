import pyglet
from pyglet.window import mouse
import Pieces as p


class Chess(pyglet.window.Window):
    chessboard = pyglet.resource.image('resources/chessboard.png')
    validImg = pyglet.resource.image('resources/validmove.png')
<<<<<<< HEAD
    hoverImg = pyglet.resource.image('resources/hoversquare.png')
=======
    # hoverImg = pyglet.resource.image('resources/hoversquare.png')
    currentPos = (-1, -1)
>>>>>>> boardchange

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Chess',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)
<<<<<<< HEAD
        self.validsprites = []
        self.hoversprites = []
        for i in range(8):
            rowsprites = []
            rowsprites2 = []
            for j in range(8):
                sprite = pyglet.sprite.Sprite(self.validImg, 75 * i, 75 * j)
                sprite.visible = False
                rowsprites.append(sprite)
                sprite2 = pyglet.sprite.Sprite(self.hoverImg, 75 * i, 75 * j)
                sprite2.visible = False
                rowsprites2.append(sprite2)
            self.validsprites.append(rowsprites)
            self.hoversprites.append(rowsprites2)
        self.whitepieces = []
        self.blackpieces = []
        for i in range(8):
            self.whitepieces.append(p.Pawn(i, 1))
            self.blackpieces.append(p.Pawn(i, 6, False))
        self.whitepieces.append(p.Rook(0, 0))
        self.whitepieces.append(p.Rook(7, 0))
        self.whitepieces.append(p.Knight(1, 0))
        self.whitepieces.append(p.Knight(6, 0))
        self.whitepieces.append(p.Bishop(2, 0))
        self.whitepieces.append(p.Bishop(5, 0))
        self.whitepieces.append(p.Queen(3, 0))
        self.whitepieces.append(p.King(4, 0))
        self.blackpieces.append(p.Rook(0, 7, False))
        self.blackpieces.append(p.Rook(7, 7, False))
        self.blackpieces.append(p.Knight(1, 7, False))
        self.blackpieces.append(p.Knight(6, 7, False))
        self.blackpieces.append(p.Bishop(2, 7, False))
        self.blackpieces.append(p.Bishop(5, 7, False))
        self.blackpieces.append(p.Queen(3, 7, False))
        self.blackpieces.append(p.King(4, 7, False))
        self.board = [['wR', 'wK', 'wB', 'wQ', 'wKK', 'wB', 'wK', 'wR'],
                      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['', '', '', '', '', '', '', ''],
                      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                      ['bR', 'bK', 'bB', 'bQ', 'bKK', 'bB', 'bK', 'bR']]
=======
        self.board = [[p.Rook(0, 0), p.Knight(1, 0), p.Bishop(2, 0), p.Queen(3, 0), p.King(4, 0), p.Bishop(5, 0),
                       p.Knight(6, 0), p.Rook(7,0)],
                      [p.Pawn(i, 1) for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [p.Pawn(i, 6, False) for i in range(8)],
                      [p.Rook(0, 7, False), p.Knight(1, 7, False), p.Bishop(2, 7, False), p.Queen(3, 7, False),
                       p.King(4, 7, False), p.Bishop(5, 7, False), p.Knight(6, 7, False), p.Rook(7, 7, False)]]
        self.validsprites = []
        for i in range(8):
            rowsprites = []
            for j in range(8):
                sprite = pyglet.sprite.Sprite(self.validImg, 75 * j, 75 * i)
                sprite.visible = False
                rowsprites.append(sprite)
            self.validsprites.append(rowsprites)
>>>>>>> boardchange

    def on_draw(self):
        self.clear()
        self.chessboard.blit(0, 0)
<<<<<<< HEAD
        for i in range(len(self.whitepieces)):
            self.whitepieces[i].Draw()
            self.blackpieces[i].Draw()

    '''def on_mouse_press(self, x, y, button, modifiers):
        boardX = x//75
        boardY = y//75'''

=======
        for i in range(8):
            for j in range(8):
                self.validsprites[i][j].draw()
                if self.board[i][j] is not None: self.board[i][j].Draw()

    def on_mouse_press(self, x, y, button, modifiers):
        boardX = x//75
        boardY = y//75
        if self.currentPos[0] < 0 and self.currentPos[1] < 0:
            if self.board[boardY][boardX] is not None:
                self.currentPos = (boardY, boardX)
                ValidMoves = self.board[boardY][boardX].GetValidMoves()
                for move in ValidMoves:
                    self.validsprites[move[0]][move[1]].visible = True
        else:
            if self.validsprites[boardY][boardX].visible:
                self.board[self.currentPos[0]][self.currentPos[1]].ChangeLocation(boardX, boardY)
                self.board[self.currentPos[0]][self.currentPos[1]], self.board[boardY][boardX] = self.board[boardY][boardX], self.board[self.currentPos[0]][self.currentPos[1]]
                self.currentPos = (-1, -1)
                for row in self.validsprites:
                    for sprite in row:
                        sprite.visible = False


    def update(self, dt):
        self.on_draw()
>>>>>>> boardchange
