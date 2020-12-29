'''
--- Day 3: Toboggan Trajectory ---
Determine the number of trees you would encounter if, 
for each of the following slopes, you start at the top-left corner 
and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
'''

def sol(slope_x, slope_y):
    f = open('input.txt', 'r')
    x_coord = 0
    tree_count = 0
    print(f'----------- BEGIN sol({slope_x},{slope_y}) ------------')

    for idx, line in enumerate(f):

        # slope_y is 2 and line is an odd numbered line 
        # (need to skip every second line)
        # or we are on the 0th line (need to skip first line)
        if slope_y == 2 and idx % 2 != 0 or idx == 0:
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
    print(f'answer is {sol(1,1) * sol(3,1) * sol(5,1) * sol(7,1) * sol(1,2)}')

