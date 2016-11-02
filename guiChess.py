import pyglet
import Pieces as p


class Chess(pyglet.window.Window):
    chessboard = pyglet.resource.image('resources/chessboard.jpg')

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Sudoku',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)

    def on_draw(self):
        self.chessboard.blit(0, 0)
        whitepawn1 = p.Pawn(16, 9.5)
