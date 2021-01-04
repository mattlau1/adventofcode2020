import re
'''
--- Day 8: Handheld Halting ---
The boot code is represented as a text file with one instruction per
line of text. Each instruction consists of an operation (acc, jmp, or nop)
and an argument (a signed number like +4 or -20).

    - acc increases or decreases a single global value called the accumulator 
    by the value given in the argument. For example, acc +7 would increase the 
    accumulator by 7. The accumulator starts at 0. After an acc instruction, the
    instruction immediately below it is executed next.

    - jmp jumps to a new instruction relative to itself.
    The next instruction to execute is found using the argument as an offset
    from the jmp instruction; for example, jmp +2 would skip the next instruction,
    jmp +1 would continue to the instruction immediately below it, and jmp -20
    would cause the instruction 20 lines above to be executed next.

    - nop stands for No OPeration - it does nothing.
    The instruction immediately below it is executed next.

Immediately before any instruction is executed a second time,
what value is in the accumulator?
'''
def sol():
    lines = []
    with open("input.txt", "r") as f:
        [lines.append(line) for line in f]
        
    executed_lines = []
    accumulator = 0
    i = 0
    while (i < len(lines)):
        if i not in executed_lines:
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

        else:
            print(f'we\'ve seen line {i} before')
            return accumulator
            
    return accumulator


if __name__ == "__main__":
    print(f'answer is {sol()}')