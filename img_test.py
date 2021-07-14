#!/usr/bin/env python3
from dataclasses import dataclass
from opensign import OpenSign, OpenSignCanvas
from time import sleep


@dataclass
class Player:
    '''Simple class for tracking player stats.'''
    score: int = 0
    games: int = 0


def draw_canvas(p1: Player, p2: Player) -> OpenSignCanvas:
    canvas = OpenSignCanvas()
    # p1 NAME
    canvas.cursor = [0, 0]
    canvas.add_text('HOME',
                    color=(222, 224, 222),
                    x_offset=3
                    )
    # p2 NAME
    canvas.cursor = [37, 0]
    canvas.add_text('AWAY',
                    color=(222, 224, 222)
                    )
    # p1 SCORE
    canvas.cursor = [11, 8]
    canvas.add_text(text=f'{p1.score}',
                    color=(76, 107, 138)
                    )
    # p2 SCORE
    canvas.cursor = [47, 8]
    canvas.add_text(text=f'{p2.score}',
                    color=(76, 107, 138)
                    )
    # GAMES
    canvas.cursor = [17, 14]
    canvas.add_text('GAMES',
                    color=(222, 224, 222)
                    )
    # p1 GAMES
    canvas.cursor = [23, 22]
    canvas.add_text(f'{p1.games}',
                    color=(76, 107, 138)
                    )
    # p2 GAMES
    canvas.cursor = [35, 22]
    canvas.add_text(f'{p2.games}',
                    color=(76, 107, 138)
                    )
    return canvas


def save_image(canvas: OpenSignCanvas):
    img = canvas.get_image()
    # print(img)
    img.save('scoreboard_background.png')


def show_canvas(canvas: OpenSignCanvas) -> None:
    sign = OpenSign(rows=32, columns=64)
    sign.show(canvas)


def main():
    # INITIALIZE PLAYERS
    # HOME - p1
    p1 = Player()
    # AWAY - p2
    p2 = Player()

    canvas = draw_canvas(p1, p2)
    save_image(canvas)

    bkgd = OpenSignCanvas()
    bkgd.add_image('scoreboard_background.png')

    sign = OpenSign(rows=32, columns=64)

    while True:
        sign.show(bkgd)
        sleep(5)


if __name__ == '__main__':
    main()
