#!/usr/bin/env python3

import random
import time

BLANK = 0
JACKPOT = 1


def strategy_change(N: int) -> int:
    doors = [JACKPOT, BLANK, BLANK]
    n_won = 0
    for _ in range(N):
        random.shuffle(doors)
        # The jackpot is behind the door with index win_idx
        win_idx = doors.index(JACKPOT)
        # Let the player choose a door at random
        chosen_idx = random.randint(0, 2)
        # Get indices of the doors with a blank behind
        remaining_door_indices = list(filter(lambda i: i != win_idx, [0, 1, 2]))
        # Now the player changes the initial choice to one of the remaining doors.
        # We simulate that behavior by removing the initial choice from the remaining ones.
        choices = list(filter(lambda idx: idx != chosen_idx, remaining_door_indices))
        # Now, if there are two choices left, the player initially chose the jackpot,
        # but if only one door is left, the player switched to the jackpot.
        if len(choices) == 1:
            n_won += 1
    return n_won


def strategy_keep(N: int) -> int:
    doors = [JACKPOT, BLANK, BLANK]
    n_won = 0
    for _ in range(N):
        random.shuffle(doors)
        chosen_idx = random.randint(0, 2)
        if doors[chosen_idx] == 1:
            n_won += 1
    return n_won


def main():
    random.seed(int(time.time() * 1000))
    N = 100_000
    a = strategy_keep(N)
    b = strategy_change(N)
    print(f'N = {N}')
    print(f'keep = {a} ({100*a/N:.1f}%)')
    print(f'change = {b} ({100*b/N:.1f}%)')


if __name__ == '__main__':
    main()