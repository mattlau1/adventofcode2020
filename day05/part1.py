'''
--- Day 5: Binary Boarding ---
Instead of zones or groups, this airline uses binary space 
partitioning to seat people. A seat might be specified like 
FBFBBFFRLR, where F means "front", B means "back", L means "left", 
and R means "right".

Every seat also has a unique seat ID: multiply the row by 8, then add 
the column.

What is the highest seat ID on a boarding pass?
'''
import numpy
def sol():
    f = open("input.txt", "r")
    seat_ids = []
    for line in f:
        r_lower_bound = 0
        r_upper_bound = 127

        c_lower_bound = 0
        c_upper_bound = 7
        
        for letter in line:
            if letter == 'F':
                r_upper_bound = numpy.floor((r_lower_bound + r_upper_bound) / 2)

            elif letter == 'B':
                r_lower_bound = numpy.ceil((r_lower_bound + r_upper_bound) / 2)
            
            elif letter == 'L':
                c_upper_bound = numpy.floor((c_lower_bound + c_upper_bound) / 2)

            elif letter == 'R':
                c_lower_bound = numpy.ceil((c_lower_bound + c_upper_bound) / 2)

        # print(line)
        # print(f'r_lower_bound = {r_lower_bound}, r_upper_bound = {r_upper_bound}')
        # print(f'c_lower_bound = {c_lower_bound}, c_upper_bound = {c_upper_bound}')

        if r_lower_bound == r_upper_bound and c_lower_bound == c_upper_bound:
            row = int(r_lower_bound)
            col = int(c_lower_bound)

        seat_ids.append(row * 8 + col)

    return seat_ids

if __name__ == "__main__":
    print(f"answer for part1 is {max(sol())}")
