from scripts.game import *

def main():
    while True:
        game = Game()
        game.start_Screen()
        game.gameLoop()
        game.end_Screen()

        quit()


if __name__ == '__main__':
    main()

