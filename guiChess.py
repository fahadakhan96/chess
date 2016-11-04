import pyglet
import Pieces as p


class Chess(pyglet.window.Window):
    chessboard = pyglet.resource.image('resources/chessboard.png')

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Sudoku',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)
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

    def on_draw(self):
        self.chessboard.blit(0, 0)
        for i in range(len(self.whitepieces)):
            self.whitepieces[i].Draw()
            self.blackpieces[i].Draw()
