import pyglet

class Piece:
    white = True
    captured = False
    x=0
    y=0

    def __init__(self, x, y, piecetype):
        self.x = x
        self.y = y
        self.captured = False
        self.white = piecetype

class Pawn(object, Piece):
    def __init__(self, x, y):
        super(Pawn, self).__init__(x, y)
        self.pieceimage = pyglet.resource.image('resource/whitepawn.png')
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x, self.y)

    def checkMove(self, x, y, piece):
        if y == self.y + 1 and x == self.x:
            return True
        if self.y == 1 and y == self.y + 2:
            return True
        if y == self.y + 1:
            if x == self.x + 1 or x == self.x -1:
                if piece is not None and piece.white is not self.white:
                    return True