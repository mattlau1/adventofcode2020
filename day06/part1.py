
def sol():
    f = open("input.txt", "r")
    question_count = 0
    questions = set()
    for line in f:
        # print(f'line: {line}')
        for letter in line:
            if letter.isalpha():
                questions.add(letter)
                # print("added", letter)

        
        # if empty line found
        if not line.strip():
            question_count += len(questions)
            # print(f'{questions}')
            # print(f'question count {question_count}')
            questions = set()

    return question_count

if __name__ == "__main__":
    print(f'answer is {sol()}')