'''
--- Day 10: Adapter Array ---
Find a chain that uses all of your adapters to connect the charging
outlet to your device's built-in adapter and count the joltage differences
between the charging outlet, the adapters, and your device.

What is the number of 1-jolt differences multiplied
by the number of 3-jolt differences?
'''
def sol():
    # Get adapter joltage ratings
    lines = [int(line.rstrip()) for line in open("input.txt", "r")]

    # Charging outlet joltage rating
    lines.append(0)

    # Device joltage rating
    lines.append(max(lines) + 3)

    # Sort all ratings so we can use all of the adapters
    lines.sort()

    # Add all joltage differences to list
    diff_list = [lines[i + 1] - lines[i] for i in range(len(lines) - 1)]

    return diff_list.count(1) * diff_list.count(3)

if __name__ == "__main__":
    print(f'{sol()}')