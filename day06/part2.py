
def sol():
    # f = open("input.txt", "r")
    f = open("example", "r")
    question_count = 0
    questions = []
    person_count = 0
    match_found = False
    for line in f:
        person_count += 1
        # print(f'line: {line}')
        # for letter in line:
        #     if letter.isalpha():
        questions.append(line.rstrip())
                

        
        # if empty line found
        if not line.strip():
            
            if len(questions[:-1])== 1:
                # 1 person
                print(f'1 person in {questions[:-1]}')
                question_count += len(questions[0])
            else:
                print(questions[:-1])
               
                        
                
            questions = []
            print("------------------")
    return question_count

if __name__ == "__main__":
    print(f'answer is {sol()}')