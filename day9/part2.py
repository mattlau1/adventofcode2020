'''
--- Day 9: Encoding Error ---
The first step of attacking the weakness in the XMAS data is to find
the first number in the list (after the preamble) which is not the sum
of two of the 25 numbers before it.

What is the first number that does not have this property?
'''
from part1 import sol as part1_sol
def sol():
    f = open("input.txt", "r")
    lines = [int(line.rstrip()) for line in f]
    part1_ans = part1_sol()

    results = check_sum(lines, part1_ans)

    return min(results) + max(results)
            
    
    
def check_sum(arr, target):
    results = []
    for i in arr:
        for j in arr:
            if j >= i:
                # j must be bigger than i or it will compare values from
                # indexes before i
                if sum(arr[i:j]) == target:
                    if len(arr[i:j]) > len(results):
                        print(arr[i:j])
                        results = arr[i:j].copy()   
    print(results)              
                
    return results

    # print(f'{int(i)} + {int(j)} != {target}')
    

if __name__ == "__main__":
    print(f'answer is {sol()}')