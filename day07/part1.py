import re
def sol():
    bag_dict = {}
    with open("input.txt") as f:
        for line in f:
            print(line)
            matches = re.findall(
                r"(\d)?\s?(\w+\s\w+)\sbag[s]?",
                line
            )
            
            for i in matches:
                if i == matches[0]:
                print(i)
            break


if __name__ == "__main__":
    sol()