import pyglet

spriteimage = pyglet.resource.image('resources/spritesheet.png')
spritesheet = pyglet.image.ImageGrid(spriteimage, 2, 6)
BLACK_KING, BLACK_QUEEN, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK, BLACK_PAWN, WHITE_KING, WHITE_QUEEN, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK, WHITE_PAWN = range(
    12)


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
            self.pieceimage = spritesheet[WHITE_PAWN]
        else:
            self.pieceimage = spritesheet[BLACK_PAWN]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)

    #def getMoves(self, ):


class Rook(Piece):
    def __init__(self, x, y, type=True):
        super(Rook, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_ROOK]
        else:
            self.pieceimage = spritesheet[BLACK_ROOK]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)


class Knight(Piece):
    def __init__(self, x, y, type=True):
        super(Knight, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_KNIGHT]
        else:
            self.pieceimage = spritesheet[BLACK_KNIGHT]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)


class Bishop(Piece):
    def __init__(self, x, y, type=True):
        super(Bishop, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_BISHOP]
        else:
            self.pieceimage = spritesheet[BLACK_BISHOP]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)


class Queen(Piece):
    def __init__(self, x, y, type=True):
        super(Queen, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_QUEEN]
        else:
            self.pieceimage = spritesheet[BLACK_QUEEN]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)


class King(Piece):
    def __init__(self, x, y, type=True):
        super(King, self).__init__(x, y, type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_KING]
        else:
            self.pieceimage = spritesheet[BLACK_KING]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, self.x * 75, self.y * 75)
