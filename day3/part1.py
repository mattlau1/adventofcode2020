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
        if idx == 1:
            continue

        if (x_coord + slope_x) >= len(line) - 1:
            x_coord -= len(line) - 1
        
        x_coord += slope_x

        # print(line)
        # print(f'index is {x_coord}')
        # print(line[x_coord])

        if line[x_coord] == '#':
            tree_count += 1
        
    return tree_count

if __name__ == "__main__":
    print(f'answer is {sol(3)}')