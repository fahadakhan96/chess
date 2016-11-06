import pyglet
from copy import deepcopy

spriteimage = pyglet.resource.image('resources/spritesheet.png')
spritesheet = pyglet.image.ImageGrid(spriteimage, 2, 6)
dangerImg = pyglet.resource.image('resources/danger.png')
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

    def MakeMove(self, board, move, king):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        board[move[0]][move[1]] = board[y][x]
        board[y][x] = None
        self.piecesprite.x = move[1] * 75
        self.piecesprite.y = move[0] * 75
        check = king.InCheck(board)
        print check
        self.piecesprite.x = x * 75
        self.piecesprite.y = y * 75
        return check

    def GetValidMoves(self, board, king):
        ListOfMoves = self.GetThreatSquares(board)
        ValidMoves = []
        for move in ListOfMoves:
            tempboard = deepcopy(board)                                         # Can be optimized. Edit MakeMove function to simply revert any changes
            if not self.MakeMove(tempboard, move, king):
                ValidMoves.append(move)
        return ValidMoves

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

    def GetThreatSquares(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        ListOfMoves = []
        if self.white and y < 7:
            if board[y + 1][x] is None:
                ListOfMoves.append((y + 1, x))
                if y == 1 and board[y + 2][x] is None:
                    ListOfMoves.append((y + 2, x))
            if x < 7 and board[y + 1][x + 1] is not None and not board[y + 1][x + 1].white:
                ListOfMoves.append((y + 1, x + 1))
            if x > 0 and board[y + 1][x - 1] is not None and not board[y + 1][x - 1].white:
                ListOfMoves.append((y + 1, x - 1))
        elif not self.white and y > 0:
            if board[y - 1][x] is None:
                ListOfMoves.append((y - 1, x))
                if y == 6 and board[y - 2][x] is None:
                    ListOfMoves.append((y - 2, x))
            if x < 7 and board[y - 1][x + 1] is not None and board[y - 1][x + 1].white:
                ListOfMoves.append((y - 1, x + 1))
            if x > 0 and board[y - 1][x - 1] is not None and board[y - 1][x - 1].white:
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

    def GetThreatSquares(self, board):
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

    def GetThreatSquares(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        ListOfMoves = []
        try:
            if board[y + 2][x + 1] is None or self.white != board[y + 2][x + 1].white:
                ListOfMoves.append((y + 2, x + 1))
        except IndexError:
            pass
        try:
            if x > 0 and (board[y + 2][x - 1] is None or self.white != board[y + 2][x - 1].white):
                ListOfMoves.append((y + 2, x - 1))
        except IndexError:
            pass
        try:
            if board[y + 1][x + 2] is None or self.white != board[y + 1][x + 2].white:
                ListOfMoves.append((y + 1, x + 2))
        except IndexError:
            pass
        try:
            if x > 1 and (board[y + 1][x - 2] is None or self.white != board[y + 1][x - 2].white):
                ListOfMoves.append((y + 1, x - 2))
        except IndexError:
            pass
        try:
            if y > 0 and (board[y - 1][x + 2] is None or self.white != board[y - 1][x + 2].white):
                ListOfMoves.append((y - 1, x + 2))
        except IndexError:
            pass
        try:
            if y > 1 and (board[y - 2][x + 1] is None or self.white != board[y - 2][x + 1].white):
                ListOfMoves.append((y - 2, x + 1))
        except IndexError:
            pass
        if x > 1 and y > 0 and (board[y - 1][x - 2] is None or self.white != board[y - 1][x - 2].white):
            ListOfMoves.append((y - 1, x - 2))
        if x > 0 and y > 1 and (board[y - 2][x - 1] is None or self.white != board[y - 2][x - 1].white):
            ListOfMoves.append((y - 2, x - 1))
        return ListOfMoves


class Bishop(Piece):
    def __init__(self, x, y, type=True):
        super(Bishop, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_BISHOP]
        else:
            self.pieceimage = spritesheet[BLACK_BISHOP]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)

    def GetThreatSquares(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        ListOfMoves = []
        for i in range(1, 8):
            if y-i < 0 or x-i < 0:
                break
            if board[y-i][x-i] is not None:
                if board[y-i][x-i].white != self.white:
                    ListOfMoves.append((y-i, x-i))
                break
            ListOfMoves.append((y-i, x-i))
        for i in range(1, 8):
            try:
                if board[y+i][x+i] is not None:
                    if board[y+i][x+i].white != self.white:
                        ListOfMoves.append((y+i, x+i))
                    break
                ListOfMoves.append((y+i, x+i))
            except IndexError:
                break
        for i in range(1, 8):
            try:
                if x-i < 0:
                    break
                if board[y+i][x-i] is not None:
                    if board[y+i][x-i].white != self.white:
                        ListOfMoves.append((y+i, x-i))
                    break
                ListOfMoves.append((y+i, x-i))
            except IndexError:
                break
        for i in range(1, 8):
            try:
                if y - i < 0:
                    break
                if board[y-i][x+i] is not None:
                    if board[y-i][x+i].white != self.white:
                        ListOfMoves.append((y-i, x+i))
                    break
                ListOfMoves.append((y-i, x+i))
            except IndexError:
                break
        return ListOfMoves


class Queen(Piece):
    def __init__(self, x, y, type=True):
        super(Queen, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_QUEEN]
        else:
            self.pieceimage = spritesheet[BLACK_QUEEN]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)

    def GetThreatSquares(self, board):
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
        for i in range(1, 8):
            if y-i < 0 or x-i < 0:
                break
            if board[y-i][x-i] is not None:
                if board[y-i][x-i].white != self.white:
                    ListOfMoves.append((y-i, x-i))
                break
            ListOfMoves.append((y-i, x-i))
        for i in range(1, 8):
            try:
                if board[y+i][x+i] is not None:
                    if board[y+i][x+i].white != self.white:
                        ListOfMoves.append((y+i, x+i))
                    break
                ListOfMoves.append((y+i, x+i))
            except IndexError:
                break
        for i in range(1, 8):
            try:
                if x-i < 0:
                    break
                if board[y+i][x-i] is not None:
                    if board[y+i][x-i].white != self.white:
                        ListOfMoves.append((y+i, x-i))
                    break
                ListOfMoves.append((y+i, x-i))
            except IndexError:
                break
        for i in range(1, 8):
            try:
                if y - i < 0:
                    break
                if board[y-i][x+i] is not None:
                    if board[y-i][x+i].white != self.white:
                        ListOfMoves.append((y-i, x+i))
                    break
                ListOfMoves.append((y-i, x+i))
            except IndexError:
                break
        return ListOfMoves


class King(Piece):
    def __init__(self, x, y, type=True):
        super(King, self).__init__(type)
        if self.white:
            self.pieceimage = spritesheet[WHITE_KING]
        else:
            self.pieceimage = spritesheet[BLACK_KING]
        self.piecesprite = pyglet.sprite.Sprite(self.pieceimage, x * 75, y * 75)
        self.danger = pyglet.sprite.Sprite(dangerImg, x * 75, y * 75)
        self.danger.visible = False

    def ChangeLocation(self, x, y):
        self.piecesprite.x = x * 75
        self.piecesprite.y = y * 75
        self.danger.x = x * 75
        self.danger.y = y * 75

    def GetThreatSquares(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        ListOfMoves = []
        try:
            if x > 0 and (board[y+1][x-1] is None or self.white != board[y+1][x-1].white):
                ListOfMoves.append((y+1, x-1))
        except IndexError:
            pass
        try:
            if board[y+1][x] is None or self.white != board[y+1][x].white:
                ListOfMoves.append((y+1, x))
        except IndexError:
            pass
        try:
            if board[y+1][x+1] is None or self.white != board[y+1][x+1].white:
                ListOfMoves.append((y+1, x+1))
        except IndexError:
            pass
        try:
            if board[y][x+1] is None or self.white != board[y][x+1].white:
                ListOfMoves.append((y, x+1))
        except IndexError:
            pass
        try:
            if y > 0 and (board[y-1][x+1] is None or self.white != board[y-1][x+1].white):
                ListOfMoves.append((y-1, x+1))
        except IndexError:
            pass
        if y > 0 and (board[y-1][x] is None or self.white != board[y-1][x].white):
            ListOfMoves.append((y-1, x))
        if y > 0 and x > 0 and (board[y-1][x-1] is None or self.white != board[y-1][x-1].white):
            ListOfMoves.append((y-1, x-1))
        if x > 0 and (board[y][x-1] is None or self.white != board[y][x-1].white):
            ListOfMoves.append((y, x-1))
        return ListOfMoves

    def Draw(self):
        self.piecesprite.draw()
        self.danger.draw()

    def InCheck(self, board):
        x = self.piecesprite.x // 75
        y = self.piecesprite.y // 75
        for row in board:
            for piece in row:
                if piece is not None and piece.white != self.white:
                    validmoves = piece.GetThreatSquares(board)
                    if (y, x) in validmoves:
                        return True
        return False
