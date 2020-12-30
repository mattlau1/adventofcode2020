'''
--- Day 4: Passport Processing ---
You can continue to ignore the cid field, but each other field has strict rules 
about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''
import re
def sol():
    f = open('input.txt')
    # f = open('part2invalid')
    valid_passports = 0
    fld_dict = {}
    

    for line in f:
        # loop through lines in file

        # look for fields (3 letters + colon) and field values using regex
        field = re.findall(r"(\w{3}):", line)
        field_val = re.findall(r":([#]?\w+)[\s\n]?", line)

        for count, key in enumerate(field):
            fld_dict[key] = field_val[count]

        # print(fld_dict)
        if not line.strip():
            if len(fld_dict) == 8:
                print("test 1 passed")
                valid_passports += check_conditions(fld_dict)
            elif len(fld_dict) == 7 and 'cid' not in fld_dict:
                print("test 1 passed")
                valid_passports += check_conditions(fld_dict)
                    
            fld_dict = {}
            field = []
            field_val = []

    return valid_passports
        
def check_conditions(fld_dict):
    '''
    Checks conditions for a valid passport and returns 1 if passport is valid:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    '''
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hgt_units = ['cm', 'in']
    valid_passports = 0

    if 1920 <= int(fld_dict['byr']) <= 2002 and len(fld_dict['byr']) == 4:
        print("test 2 passed")
        if 2010 <= int(fld_dict['iyr']) <= 2020 and len(fld_dict['iyr']) == 4:
            print("test 3 passed")
            if 2020 <= int(fld_dict['eyr']) <= 2030 and len(fld_dict['eyr']) == 4:
                print("test 4 passed")
                if fld_dict['hcl'][0] == '#' and len(fld_dict['hcl']) == 7 and fld_dict['hcl'][1:].isalnum() is True:
                    print("test 5 passed")
                    if fld_dict['ecl'] in ecl_list:
                        print("test 6 passed")
                        if len(fld_dict['pid']) == 9:
                            print("test 7 passed")
                            if fld_dict['hgt'][-2:] in hgt_units:
                                print("test 8 passed")
                                if fld_dict['hgt'][-2:] == hgt_units[0] and 150 <= int(fld_dict['hgt'][:-2]) <= 193:
                                    valid_passports += 1
                                elif fld_dict['hgt'][-2:] == hgt_units[1] and 59 <= int(fld_dict['hgt'][:-2]) <= 76:
                                    valid_passports += 1
    return valid_passports

if __name__ == "__main__":
    print(f'Number of valid passports are: {sol()}')