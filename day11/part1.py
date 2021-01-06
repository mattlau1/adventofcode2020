
def sol():
    lines = [list(line.rstrip()) for line in open("input.txt", "r")]

    occupied_seats = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            curr_seat = lines[i][j]
            print(curr_seat)

            # current seat is empty
            if curr_seat == 'L' and count_adjacent_seats(i, j, lines) == 0:
                curr_seat = '#'
                lines[i][j] = curr_seat
                occupied_seats += 1
            elif curr_seat == '#' and count_adjacent_seats(i, j, lines) >= 4:
                curr_seat = 'L'
                lines[i][j] = curr_seat
                occupied_seats += 1

    return occupied_seats

def count_adjacent_seats(i, j, arr):
    '''
    L  L  .
    L  L  L
    L  L  L

    Adjacent Seats from middle
    ---------------------------
    MID   = arr[i][j]

    up    = arr[i - 1][j]
    down  = arr[i + 1][j]
    left  = arr[i][j - 1]
    right = arr[i][j + 1]

    t_left  =  arr[i - 1][j - 1]
    t_right =  arr[i - 1][j + 1]
    b_left  =  arr[i + 1][j - 1]
    b_right =  arr[i + 1][j + 1]
    
    '''
    occupied_adjacent_seats = 0
    print(f'i = {i}, j = {j}')
    # if i > 1 and arr[i - 1][j] == '#':
    #     # up
    #     occupied_adjacent_seats += 1

    # if i < len(arr[i]) - 1 and arr[i + 1][j] == '#':
    #     # down
    #     occupied_adjacent_seats += 1

    # if j > 1 and arr[i][j - 1] == '#':
    #     # left
    #     occupied_adjacent_seats += 1

    # if i < len(arr[i]) - 1 and j < len(arr) - 1 and arr[i][j + 1] == '#':
    #     # right
    #     occupied_adjacent_seats += 1

    # if i > 1 and j > 1 and arr[i - 1][j - 1] == '#':
    #     # t_left
    #     occupied_adjacent_seats += 1

    # if i > 1 and j < len(arr) - 1 and arr[i - 1][j + 1] == '#':
    #     # t_right
    #     occupied_adjacent_seats += 1

    # if i < len(arr[i]) - 1 and j > 1 and arr[i + 1][j - 1] == '#':
    #     # b_left
    #     occupied_adjacent_seats += 1

    # if i < len(arr[i]) - 1 and j < len(arr) - 1 and arr[i + 1][j + 1] == '#':
    #     # b_right
    #     occupied_adjacent_seats += 1


    return occupied_adjacent_seats

if __name__ == "__main__":
    print(f'answer is {sol()}')

    # test_arr = [['#.##.##.##'],
    #             ['#######.##'],
    #             ['#.#.#..#..'],
    #             ['####.##.##'],
    #             ['#.##.##.##'],
    #             ['#.#####.##'],
    #             ['..#.#.....'],
    #             ['##########'],
    #             ['#.######.#'],
    #             ['#.#####.##']]
    # for i in range(len(test_arr)):
    #     for j in range(len(test_arr[i])):
            
    #         print(f'count: {count_adjacent_seats(i, j, test_arr)}')