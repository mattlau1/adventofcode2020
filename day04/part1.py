'''
--- Day 4: Passport Processing ---
Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
'''
import re
def sol():
    f = open('input.txt')
    field_count = 0
    valid_passports = 0
    pass_counter = 0
    field_list = []

    for line in f:
        # loop through lines in file

        # print(line, end='')

        # look for fields (3 letters + colon)
        matches = (re.findall(r"(\w{3}):", line))
        
        for x in matches:
            # add to field counter
            field_count += 1

            print(f'x is [{x}] field_count is {field_count}')

            # add to list of fields per passport
            field_list.append(x)

        # empty line (separator)
        if not line.strip():
            if field_count == 8:
                valid_passports += 1
                print(f'passport {pass_counter} is valid')
            elif field_count == 7 and 'cid' not in field_list:
                valid_passports += 1
                print(f'passport {pass_counter} is valid since cid not in {field_list}')
            else:
                print(f'passport {pass_counter} is invalid')

            # add to passport counter, reset field counter and list of fields
            pass_counter += 1
            field_count = 0
            field_list = []

    return valid_passports
        
if __name__ == "__main__":
    print(f'Number of valid passports are: {sol()}')