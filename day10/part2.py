'''
--- Day 10: Adapter Array ---
Find a chain that uses all of your adapters to connect the charging
outlet to your device's built-in adapter and count the joltage differences
between the charging outlet, the adapters, and your device.

What is the number of 1-jolt differences multiplied
by the number of 3-jolt differences?
'''
from itertools import permutations
def sol():
    # Get adapter joltage ratings
    lines = [int(line.rstrip()) for line in open("input.txt", "r")]
    # Charging outlet joltage rating
    lines.append(0)

    # Device joltage rating
    lines.append(max(lines) + 3)

    perms = permutations(lines)

    valid_arrangements = 0
    for adapters in perms:
        diff_list = []
        for i in range(len(adapters) - 1):
            diff = lines[i + 1] - lines[i]
            if diff > 3 or diff < 1:
                diff_list = []
                break
            else:
                diff_list.append(diff)
        if len(diff_list) > 0:
            valid_arrangements += 1
    return valid_arrangements

    

if __name__ == "__main__":
    print(f'{sol()}')