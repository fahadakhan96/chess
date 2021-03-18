import pyglet
from pyglet.window import mouse
import Pieces as p


class Chess(pyglet.window.Window):
    chessboard = pyglet.resource.image('resources/chessboard.png')
    validImg = pyglet.resource.image('resources/validmove.png')
    # hoverImg = pyglet.resource.image('resources/hoversquare.png')
    # wpromoImg = pyglet.resource.image('resources/pawn_promotion_colored.png')
    # bpromoImg = pyglet.resource.image('resources/bpawn_promotion_colored.png')
    promoImg = pyglet.resource.image('resources/promotion.png')
    currentPos = (-1, -1)
    move = True
    promotion = False
    spriteimage = pyglet.resource.image('resources/spritesheet.png')
    spritesheet = pyglet.image.ImageGrid(spriteimage, 2, 6)

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Chess',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)
        self.wKing = p.King(4, 0)
        self.bKing = p.King(4, 7, False)
        self.board = [[p.Rook(0, 0), p.Knight(1, 0), p.Bishop(2, 0), p.Queen(3, 0), self.wKing, p.Bishop(5, 0),
                       p.Knight(6, 0), p.Rook(7,0)],
                      [p.Pawn(i, 1) for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [None for i in range(8)],
                      [p.Pawn(i, 6, False) for i in range(8)],
                      [p.Rook(0, 7, False), p.Knight(1, 7, False), p.Bishop(2, 7, False), p.Queen(3, 7, False),
                       self.bKing, p.Bishop(5, 7, False), p.Knight(6, 7, False), p.Rook(7, 7, False)]]
        self.validsprites = []
        for i in range(8):
            rowsprites = []
            for j in range(8):
                sprite = pyglet.sprite.Sprite(self.validImg, 75 * j, 75 * i)
                sprite.visible = False
                rowsprites.append(sprite)
            self.validsprites.append(rowsprites)
        self.wQueen = pyglet.sprite.Sprite(self.spritesheet[7], 131.25, 225)
        self.wRook = pyglet.sprite.Sprite(self.spritesheet[10], 218.75, 225)
        self.wBishop = pyglet.sprite.Sprite(self.spritesheet[8], 306.25, 225)
        self.wKnight = pyglet.sprite.Sprite(self.spritesheet[9], 393.75, 225)
        self.bQueen = pyglet.sprite.Sprite(self.spritesheet[1], 131.25, 225)
        self.bRook = pyglet.sprite.Sprite(self.spritesheet[4], 218.75, 225)
        self.bBishop = pyglet.sprite.Sprite(self.spritesheet[2], 306.25, 225)
        self.bKnight = pyglet.sprite.Sprite(self.spritesheet[3], 393.75, 225)


    def on_draw(self):
        self.clear()
        self.chessboard.blit(0, 0)
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None: self.board[i][j].Draw()
                self.validsprites[i][j].draw()
        if self.promotion:
            self.promoImg.blit(100, 200)
            if self.move:
                self.bQueen.draw()
                self.bRook.draw()
                self.bBishop.draw()
                self.bKnight.draw()
            else:
                self.wQueen.draw()
                self.wRook.draw()
                self.wBishop.draw()
                self.wKnight.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.promotion:
            if button == mouse.LEFT:
                if 225 < y < 300:
                    if 131.25 < x < 206.25:
                        self.board[self.promoPawn[0]][self.promoPawn[1]] = p.Queen(self.promoPawn[1], self.promoPawn[0], not self.move)
                    elif 218.75 < x < 293.75:
                        self.board[self.promoPawn[0]][self.promoPawn[1]] = p.Rook(self.promoPawn[1], self.promoPawn[0], not self.move)
                    elif 306.25 < x < 381.25:
                        self.board[self.promoPawn[0]][self.promoPawn[1]] = p.Bishop(self.promoPawn[1], self.promoPawn[0], not self.move)
                    elif 393.75 < x < 468.75:
                        self.board[self.promoPawn[0]][self.promoPawn[1]] = p.Knight(self.promoPawn[1], self.promoPawn[0], not self.move)
                self.promoPawn = (-1, -1)
                self.promotion = False
                if not self.move:
                    if self.bKing.NoValidMoves(self.board) and not self.bKing.InCheck(self.board):
                        print('Stalemate!')
                    if self.bKing.InCheck(self.board):
                        self.bKing.danger.visible = True
                        if self.bKing.NoValidMoves(self.board):
                            print("Checkmate! White wins.")
                    if self.wKing.danger.visible:
                        if not self.wKing.InCheck(self.board):
                            self.wKing.danger.visible = False
                else:
                    if self.wKing.NoValidMoves(self.board) and not self.wKing.InCheck(self.board):
                        print('Stalemate!')
                    if self.wKing.InCheck(self.board):
                        self.wKing.danger.visible = True
                        if self.wKing.NoValidMoves(self.board):
                            print("Checkmate! Black wins.")
                    if self.bKing.danger.visible:
                        if not self.bKing.InCheck(self.board):
                            self.bKing.danger.visible = False
        else:
            if button == mouse.LEFT:
                boardX = x//75
                boardY = y//75
                if self.currentPos[0] < 0 and self.currentPos[1] < 0:
                    if self.board[boardY][boardX] is not None and self.move == self.board[boardY][boardX].white:
                        self.currentPos = (boardY, boardX)
                        if self.move:
                            ValidMoves = self.board[boardY][boardX].GetValidMoves(self.board, self.wKing)
                        else:
                            ValidMoves = self.board[boardY][boardX].GetValidMoves(self.board, self.bKing)
                        if len(ValidMoves) == 0:
                            self.currentPos = (-1, -1)
                        else:
                            for move in ValidMoves:
                                self.validsprites[move[0]][move[1]].visible = True
                elif self.board[boardY][boardX] is not None and self.move == self.board[boardY][boardX].white:
                    for row in self.validsprites:
                        for sprite in row:
                            sprite.visible = False
                    self.currentPos = (boardY, boardX)
                    if self.move:
                        ValidMoves = self.board[boardY][boardX].GetValidMoves(self.board, self.wKing)
                    else:
                        ValidMoves = self.board[boardY][boardX].GetValidMoves(self.board, self.bKing)
                    if len(ValidMoves) == 0:
                        self.currentPos = (-1, -1)
                    else:
                        for move in ValidMoves:
                            self.validsprites[move[0]][move[1]].visible = True
                else:
                    if self.validsprites[boardY][boardX].visible:
                        self.board[boardY][boardX] = self.board[self.currentPos[0]][self.currentPos[1]]
                        self.board[self.currentPos[0]][self.currentPos[1]].ChangeLocation(boardX, boardY, self.board)
                        if type(self.board[self.currentPos[0]][self.currentPos[1]]) is p.Pawn and (boardY == 0 or boardY == 7):
                            self.promotion = True
                            self.promoPawn = (boardY, boardX)
                        self.board[self.currentPos[0]][self.currentPos[1]] = None
                        self.currentPos = (-1, -1)
                        if self.move:
                            if self.bKing.NoValidMoves(self.board) and not self.bKing.InCheck(self.board):
                                print('Stalemate!')
                            if self.bKing.InCheck(self.board):
                                self.bKing.danger.visible = True
                                if self.bKing.NoValidMoves(self.board):
                                    print("Checkmate! White wins.")
                            if self.wKing.danger.visible:
                                if not self.wKing.InCheck(self.board):
                                    self.wKing.danger.visible = False
                        else:
                            if self.wKing.NoValidMoves(self.board) and not self.wKing.InCheck(self.board):
                                print('Stalemate!')
                            if self.wKing.InCheck(self.board):
                                self.wKing.danger.visible = True
                                if self.wKing.NoValidMoves(self.board):
                                    print("Checkmate! Black wins.")
                            if self.bKing.danger.visible:
                                if not self.bKing.InCheck(self.board):
                                    self.bKing.danger.visible = False
                        self.move = not self.move
                        for row in self.validsprites:
                            for sprite in row:
                                sprite.visible = False

    def update(self, dt):
        self.on_draw()