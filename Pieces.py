import pyglet

spriteimage = pyglet.resource.image('resources/spritesheet.png')
spritesheet = pyglet.image.ImageGrid(spriteimage, 2, 6)
BLACK_KING, BLACK_QUEEN, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK, BLACK_PAWN, WHITE_KING, WHITE_QUEEN, WHITE_BISHOP, \
    WHITE_KNIGHT, WHITE_ROOK, WHITE_PAWN = range(12)


class Piece(object):
    white = True
    piecesprite = None
    captured = False
    # x = 0
    # y = 0

    def __init__(self, type):
        # self.x = x
        # self.y = y
        self.white = type
        self.captured = False

    def ChangeLocation(self, x, y):
        # self.x = x
        # self.y = y
        self.piecesprite.x = x * 75
        self.piecesprite.y = y * 75

    def Draw(self):
        self.piecesprite.draw()


class Pawn(Piece):
    def __init__(self, x, y, type=True):
        super(Pawn, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_PAWN]
        else:
            self.pieceimage = spritesheet[BLACK_PAWN]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)

    def GetValidMoves(self, board):
        x = self.piecesprite.x//75
        y = self.piecesprite.y//75
        ListOfMoves = []
        if self.white and y < 7:
            if board[y + 1][x] is None:
                ListOfMoves.append((y + 1, x))
                if y == 1 and board[y + 2][x] is None:
                    ListOfMoves.append((y + 2, x))
            if x < 7 and board[y+1][x+1] is not None and not board[y+1][x+1].white:
                ListOfMoves.append((y + 1, x + 1))
            if x > 0 and board[y+1][x-1] is not None and not board[y+1][x-1].white:
                ListOfMoves.append((y + 1, x - 1))
        elif not self.white and y > 0:
            if board[y-1][x] is None:
                ListOfMoves.append((y - 1, x))
                if y == 6 and board[y-2][x] is None:
                    ListOfMoves.append((y - 2, x))
            if x < 7 and board[y-1][x+1] is not None and board[y-1][x+1].white:
                ListOfMoves.append((y - 1, x + 1))
            if x > 0 and board[y-1][x-1] is not None and board[y-1][x-1].white:
                ListOfMoves.append((y - 1, x - 1))
        return ListOfMoves


class Rook(Piece):
    def __init__(self, x, y, type=True):
        super(Rook, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_ROOK]
        else:
            self.pieceimage = spritesheet[BLACK_ROOK]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)

    def GetValidMoves(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        ListOfMoves = []
        if y > 0:
            for i in range(y - 1, -1, -1):
                if board[i][x] is not None:
                    if board[i][x].white != self.white:
                        ListOfMoves.append((i, x))
                    break
                ListOfMoves.append((i, x))
        if y < 7:
            for i in range(y + 1, 8):
                if board[i][x] is not None:
                    if board[i][x].white != self.white:
                        ListOfMoves.append((i, x))
                    break
                ListOfMoves.append((i, x))
        if x > 0:
            for i in range(x - 1, -1, -1):
                if board[y][i] is not None:
                    if board[y][i].white != self.white:
                        ListOfMoves.append((y, i))
                    break
                ListOfMoves.append((y, i))
        if x < 7:
            for i in range(x + 1, 8):
                if board[y][i] is not None:
                    if board[y][i].white != self.white:
                        ListOfMoves.append((y, i))
                    break
                ListOfMoves.append((y, i))
        return ListOfMoves


class Knight(Piece):
    def __init__(self, x, y, type=True):
        super(Knight, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_KNIGHT]
        else:
            self.pieceimage = spritesheet[BLACK_KNIGHT]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)


class Bishop(Piece):
    def __init__(self, x, y, type=True):
        super(Bishop, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_BISHOP]
        else:
            self.pieceimage = spritesheet[BLACK_BISHOP]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)


class Queen(Piece):
    def __init__(self, x, y, type=True):
        super(Queen, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_QUEEN]
        else:
            self.pieceimage = spritesheet[BLACK_QUEEN]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)


class King(Piece):
    def __init__(self, x, y, type=True):
        super(King, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_KING]
        else:
            self.pieceimage = spritesheet[BLACK_KING]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)
