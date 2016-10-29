import pyglet

class Chess(pyglet.window.Window):

    chessboard = pyglet.resource.image('resources/chessboard.jpg')

    def __init__(self):
        super(Chess, self).__init__(600, 600,
                                    resizable=False,
                                    caption='Sudoku',
                                    config=pyglet.gl.Config(double_buffer=True),
                                    vsync=False)

    def on_draw(self):
        self.chessboard.blit(0,0)


def main():
    mygame = Chess()
    pyglet.app.run()


if __name__ == '__main__':
    main()
