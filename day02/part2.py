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
        match1 = False
        match2 = False
        nums = re.findall(r"\d+", line)
        letters = re.search(r'\s(\w):', line)
        password = re.search(r':\s(\w+)$', line)
        # print(line, end='')
        # print(f'lower bound is {nums[0]}')
        # print(f'upper bound is {nums[1]}')
        # print(f"letter is {letters[1]}")
        # print(f"pass is {password[1]}")
        
        password_chars = list(password[1])
        
        # check if password at index lower bound is equal to letter
        if password_chars[int(nums[0]) - 1] == letters[1]:
            match1 = True
        
        # check if password at index upper bound is equal to letter
        if password_chars[int(nums[1]) - 1] == letters[1]:
            match2 = True

        if match1 != match2:
            valid_count += 1

    return valid_count
        

if __name__ == "__main__":
    print(f'valid passwords: {sol()}')
