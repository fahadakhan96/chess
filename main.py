from guiChess import Chess, pyglet

def main():
    mygame = Chess()
    pyglet.clock.schedule_interval(mygame.update, 1 / 60.)
    pyglet.app.run()


if __name__ == '__main__':
    main()