'''
--- Day 2: Password Philosophy ---
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of times 
a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 
time and at most 3 times.

Input file is in input.txt
Solution created using regex searches from re library.
'''

import re

def sol():
    f = open('input.txt', 'r')
    valid_count = 0

    for line in f:
        nums = re.findall(r"\d+", line)
        letters = re.search(r'\s(\w):', line)
        password = re.search(r':\s(\w+)$', line)
#         print(line, end='')
#         print(f'lower bound is {nums[0]}')
#         print(f'upper bound is {nums[1]}')
#         print(f"letter is {letters[1]}")
#         print(f"pass is {password[1]}")
        
        letter_count = password[1].count(letters[1])
#         print(f'letter count is {letter_count}')

        if letter_count >= int(nums[0]) and letter_count <= int(nums[1]):
            valid_count += 1

        print('')
    return valid_count
        

if __name__ == "__main__":
    print(f'valid passwords: {sol()}')
