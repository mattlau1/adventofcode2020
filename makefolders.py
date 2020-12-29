'''
Making day{n} folders

Usage: python3 makefolders.py | xargs mkdir
'''
for i in range(32):
    if i != 1 and i != 0:
        print(f'day{i}')
