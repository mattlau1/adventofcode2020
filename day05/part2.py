'''
--- Day 5: Binary Boarding ---
It's a completely full flight, so your seat should be the 
only missing boarding pass in your list. However, there's a catch: 
some of the seats at the very front and back of the plane don't exist
 on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs 
+1 and -1 from yours will be in your list.

What is the ID of your seat?
'''
from part1 import sol as part1_sol

def sol():
    l2 = sorted(part1_sol())
    l1 = []
    [l1.append(i) for i in range(min(l2),max(l2) + 1)]

    for i in range(len(l2)):
        if l1[i] != l2[i]:
            return l1[i]

if __name__ == "__main__":
    print(f'answer for part 2 is: {sol()}')