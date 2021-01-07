import re
def sol():
    lines = []
    with open("input.txt", "r") as f:
        [lines.append(line) for line in f]
        
    executed_lines = []
    accumulator = 0
    i = 0
    while (i < len(lines)):

        match = re.findall(r"(\w{3})\s([+-]\d+)", lines[i])[0]
        instr = match[0]
        num = int(match[1])

        print(f'line {i}: {instr} +{num}')
        executed_lines.append(i)

        if instr == 'acc':
            accumulator += num
            print(f'accumulator is at {accumulator}')
            i += 1

        elif instr == 'nop':
            i += 1

        else:
            print(f'curr index {i} jump to {i + num}')
            i += num
        print()

        
            
    return accumulator


if __name__ == "__main__":
    print(f'answer is {sol()}')