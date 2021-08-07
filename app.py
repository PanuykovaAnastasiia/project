from Question import Question

question_prompts = [
    "How many days do we have in a week?\n (a) seven; (b) five; (c) three\n Theme: General\n Author: Дмитриев Дмитрий Дмитриевич\n Complexity: 1/5\n Mark: 2",
    "Which animal is known as the ‘Ship of the Desert?’\n (a) pinguin; (b) camel; (c) zebra\n Theme: Animals\n Author: Иванов Иван Иванович\n Complexity: 3/5\n Mark: 6",
    "Which month of the year has the least number of days?\n (a) february; (b) November; (c) June\n Theme: General\n Author: Васильев Василий Васильевич\n Complexity: 2/5\n Mark: 4",
    "Which is the largest animal in the world?\n (a) elephant; (b) bear; (c) whale\n Theme: Animals\n Author: Михайлов Михаил Михайлович\n Complexity: 5/5\n Mark: 10",
]

questions = [
    Question(question_prompts[0], "a", "Theme: General", "Author: Дмитриев Дмитрий Дмитриевич", 1/5),
    Question(question_prompts[1], "b", "Theme: Animals", "Author: Иванов Иван Иванович", 3/5),
    Question(question_prompts[2], "a", "Theme: General", "Author: Васильев Василий Васильевич", 2/5),
    Question(question_prompts[3], "c", "Theme: Animals", "Author: Михайлов Михаил Михайлович", 5/5),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)