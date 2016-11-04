import pyglet


class Piece(object):
    white = True
    piecesprite = None
    captured = False
    x = 0
    y = 0

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.white = type
        self.captured = False

    def Draw(self):
        self.piecesprite.draw()


class Pawn(Piece):
    def __init__(self, x, y, type=True):
        super(Pawn, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = pyglet.resource.image('resources/whitepawn.png')
        else:
            self.pieceimage = pyglet.resource.image('resources/blackpawn.png')
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75 + 16, self.y * 75 + 9.5)


class Rook(Piece):
    def __init__(self, x, y, type=True):
        super(Rook, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = pyglet.resource.image('resources/whiterook.png')
        else:
            self.pieceimage = pyglet.resource.image('resources/blackrook.png')
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75 + 13.5, self.y * 75 + 9.5)

class Knight(Piece):
    def __init__(self)