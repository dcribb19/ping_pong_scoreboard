#!/usr/bin/env python3
from dataclasses import dataclass
from gpiozero import Button
from time import sleep


@dataclass
class Player:
    score: int = 0


# INITIALIZE BUTTONS FOR REMOTES
button_A = Button(7, pull_up=False)     # GPIO7, BOARD26
button_B = Button(8, pull_up=False)     # GPIO8, BOARD24
button_C = Button(15, pull_up=False)    # GPIO15, BOARD10
button_D = Button(14, pull_up=False)    # GPIO14, BOARD8
p1 = Player()
p2 = Player()


def main():
    while True:
        if button_A.is_active:
            p1.score += 1
            # DEBUG
            print(f'p1: {p1.score}')
            print(f'p2: {p2.score}')
            sleep(1)
        if button_B.is_active:
            p2.score += 1
            # DEBUG
            print(f'p1: {p1.score}')
            print(f'p2: {p2.score}')
            sleep(1)

        # DECREASE SCORE
        if button_C.is_active:
            p1.score -= 1
            # DEBUG
            print(f'p1: {p1.score}')
            print(f'p2: {p2.score}')
            sleep(1)
        if button_D.is_active:
            p2.score -= 1
            # DEBUG
            print(f'p1: {p1.score}')
            print(f'p2: {p2.score}')
            sleep(1)


if __name__ == '__main__':
    main()
