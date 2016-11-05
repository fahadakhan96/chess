import pyglet
from pyglet.window import mouse
import Pieces as p


class Chess(pyglet.window.Window):
    chessboard = pyglet.resource.image('resources/chessboard.png')
    validImg = pyglet.resource.image('resources/validmove.png')
    # hoverImg = pyglet.resource.image('resources/hoversquare.png')
    currentPos = (-1, -1)

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Sudoku',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)
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

    def on_draw(self):
        self.clear()
        self.chessboard.blit(0, 0)
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None: self.board[i][j].Draw()
                self.validsprites[i][j].draw()

    def on_mouse_press(self, x, y, button, modifiers):
        boardX = x//75
        boardY = y//75
        if self.currentPos[0] < 0 and self.currentPos[1] < 0:
            if self.board[boardY][boardX] is not None:
                self.currentPos = (boardY, boardX)
                ValidMoves = self.board[boardY][boardX].GetValidMoves(self.board)
                if len(ValidMoves) == 0:
                    self.currentPos = (-1, -1)
                else:
                    for move in ValidMoves:
                        self.validsprites[move[0]][move[1]].visible = True
        else:
            if self.validsprites[boardY][boardX].visible:
                self.board[boardY][boardX] = self.board[self.currentPos[0]][self.currentPos[1]]
                self.board[self.currentPos[0]][self.currentPos[1]].ChangeLocation(boardX, boardY)
                self.board[self.currentPos[0]][self.currentPos[1]] = None
                self.currentPos = (-1, -1)
                for row in self.validsprites:
                    for sprite in row:
                        sprite.visible = False


    def update(self, dt):
        self.on_draw()