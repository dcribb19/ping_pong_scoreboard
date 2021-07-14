#!/usr/bin/env python3
from dataclasses import dataclass
from gpiozero import Button
from opensign import OpenSign, OpenSignCanvas
from time import sleep

# INITIALIZE BUTTONS FOR REMOTES
button_A = Button(7, pull_up=False)     # GPIO7, BOARD26
button_B = Button(8, pull_up=False)     # GPIO8, BOARD24
button_C = Button(15, pull_up=False)    # GPIO15, BOARD10
button_D = Button(14, pull_up=False)    # GPIO14, BOARD8

# COLORS
# rhinestone (222, 224, 222)
# revel blue (76, 107, 138)


@dataclass
class Player:
    '''Simple class for tracking player stats.'''
    score: int = 0
    games: int = 0


def reset(p1: Player, p2: Player):
    '''Set score and game counts to 0.'''
    p1.score = 0
    p2.score = 0
    p1.games = 0
    p2.games = 0


def score_controls(p1: Player, p2: Player):
    '''Inc/Dec score based on button press.'''
    # INCREMENT SCORE
    if button_A.is_active:
        p1.score += 1
        # DEBUG
        print(f'p1: {p1.score}')
        print(f'p2: {p2.score}')
        sleep(3)
        if check_win_game(p1, p2):
            p1.games += 1
            p1.score = 0
            p2.score = 0
        if check_win_match(p1, p2):
            reset(p1, p2)
            # TODO: WINNER MESSAGE

    if button_B.is_active:
        p2.score += 1
        # DEBUG
        print(f'p1: {p1.score}')
        print(f'p2: {p2.score}')
        sleep(3)
        if check_win_game(p2, p1):
            p2.games += 1
            p1.score = 0
            p2.score = 0
        if check_win_match(p2, p1):
            reset(p1, p2)
            # TODO: WINNER MESSAGE

    # DECREASE SCORE
    if button_C.is_active:
        p1.score -= 1
        # DEBUG
        print(f'p1: {p1.score}')
        print(f'p2: {p2.score}')
        sleep(3)
    if button_D.is_active:
        p2.score -= 1
        # DEBUG
        print(f'p1: {p1.score}')
        print(f'p2: {p2.score}')
        sleep(3)


def check_win_game(player_1: Player, player_2: Player) -> bool:
    '''Check if a Player has won the game.'''
    # CHECK FOR SKUNK
    if player_1.score == 7 and player_2.score == 0:
        return True
    elif player_1.score >= 11 and player_1.score - player_2.score >= 2:
        return True
    else:
        return False


def check_win_match(player_1: Player, player_2: Player) -> bool:
    '''Check if a Player has won the match.'''
    if player_1.games >= 5 and player_1.games - player_2.games >= 2:
        return True
    return False


def draw_canvas(p1: Player, p2: Player) -> OpenSignCanvas:
    canvas = OpenSignCanvas()
    # p1 NAME
    canvas.cursor = [0, 0]
    canvas.add_text('HOME',
                    color=(222, 224, 222),
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


def main():
    # INITIALIZE PLAYERS
    # HOME - p1
    p1 = Player()
    # AWAY - p2
    p2 = Player()

    sign = OpenSign(rows=32, columns=64)

    while True:
        # PLAY PING PONG
        canvas = draw_canvas(p1, p2)
        sign.show(canvas)
        score_controls(p1, p2)

    # TODO: RESET
    # TODO: POWER BUTTON


if __name__ == '__main__':
    main()
