'''
--- Day 9: Encoding Error ---
The first step of attacking the weakness in the XMAS data is to find
the first number in the list (after the preamble) which is not the sum
of two of the 25 numbers before it.

What is the first number that does not have this property?
'''
def sol():
    f = open("input.txt", "r")
    lines = [line for line in f]

    for idx, line in enumerate(lines):
        if idx >= 25 and check_sum(lines[idx - 25:idx], int(line)) is False:
            return int(line)
    
def check_sum(arr, target):
    '''
    Checks if any of the items in the array add to the target value.
    '''
    for i in arr:
        for j in arr:
            if int(i) + int(j) == target:
                return True
    return False

if __name__ == "__main__":
    print(f'answer is {sol()}')