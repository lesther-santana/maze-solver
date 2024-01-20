from tkinter import Tk
from game import MazeGame


def main():

    root = Tk()
    root.geometry("800x800")
    game = MazeGame(root)
    game.start()


if __name__ == "__main__":
    main()