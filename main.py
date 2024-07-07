import random
import sys
import os
from game_functions import initialize_grid, add_random_two, move, can_move, print_grid

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    grid = initialize_grid()
    add_random_two(grid)
    add_random_two(grid)
    
    while True:
        clear_screen()
        print_grid(grid)
        
        if any(2048 in row for row in grid):
            print("Congratulations! You've reached 2048!")
            break
        
        if not can_move(grid):
            print("Game Over! No more possible moves.")
            break

        try:
            move_direction = input("Enter move (w/a/s/d): ").strip().lower()
            if move_direction not in ['w', 'a', 's', 'd']:
                raise ValueError("Invalid input! Please enter 'w', 'a', 's', or 'd'.")
            grid, moved = move(grid, move_direction)
            if moved:
                add_random_two(grid)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
