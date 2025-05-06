#!/usr/bin/python3
import random
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # pick unique mine positions as indices 0..width*height-1
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False]*width for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # header
        print('   ' + ' '.join(f'{i:2d}' for i in range(self.width)))
        for y in range(self.height):
            row = []
            for x in range(self.width):
                idx = y*self.width + x
                if reveal or self.revealed[y][x]:
                    if idx in self.mines:
                        row.append(' *')
                    else:
                        c = self.count_mines_nearby(x, y)
                        row.append(f' {c}' if c>0 else '  ')
                else:
                    row.append(' .')
            print(f'{y:2d} ' + ''.join(row))
        print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1,0,1):
            for dx in (-1,0,1):
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny*self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Return False if mine hit, True otherwise."""
        idx = y*self.width + x
        if idx in self.mines:
            return False
        # flood-fill reveal
        def _reveal_cell(cx, cy):
            if not (0 <= cx < self.width and 0 <= cy < self.height):
                return
            if self.revealed[cy][cx]:
                return
            self.revealed[cy][cx] = True
            if self.count_mines_nearby(cx, cy) == 0:
                for dy in (-1,0,1):
                    for dx in (-1,0,1):
                        _reveal_cell(cx+dx, cy+dy)

        _reveal_cell(x, y)
        return True

    def is_won(self):
        """All non-mine cells revealed?"""
        total = self.width*self.height - len(self.mines)
        cnt = sum(row.count(True) for row in self.revealed)
        return cnt == total

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
            except ValueError:
                print("Invalid input. Please enter integer coordinates.")
                continue
            # bounds check
            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Coordinates out of range.")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            if self.is_won():
                self.print_board(reveal=True)
                print("Congratulations! You cleared all safe cells!")
                break

if __name__ == "__main__":
    # optional width/height/mines from sys.argv
    game = Minesweeper()
    game.play()

