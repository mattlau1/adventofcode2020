'''
--- Day 3: Toboggan Trajectory ---
From your starting position at the top-left, 
check the position that is right 3 and down 1. 
Then, check the position that is right 3 and down 1 
from there, and so on until you go past the bottom of the map.
'''

def sol(slope_x):
    f = open('input.txt', 'r')
    x_coord = 0
    tree_count = 0

    for idx, line in enumerate(f):
        
        # skip first line
        if idx == 0:
            continue

        # if we go over the length of the line, go back to the
        # start of the line
        if (x_coord + slope_x) >= len(line) - 1:
            x_coord -= len(line) - 1
        
        # move right slope_x amount of spaces
        x_coord += slope_x

        print(f'we are on line {idx}')
        print(f"{' ' * x_coord}v")
        print(line)

        if line[x_coord] == '#':
            tree_count += 1
        
    return tree_count

if __name__ == "__main__":
    print(f'answer is {sol(3)}')