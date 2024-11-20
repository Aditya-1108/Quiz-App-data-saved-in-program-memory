import random
import time

questions = [
    {"question": "What is the correct way to declare a variable in Python?", 
     "options": ["1. var x = 10", "2. x = 10", "3. int x = 10", "4. let x = 10"], "answer": "2"},
    {"question": "Which of these is a valid Python data type?", 
     "options": ["1. Integer", "2. String", "3. Boolean", "4. All of the above"], "answer": "4"},
    {"question": "Which of the following is a valid Python variable name?", 
     "options": ["1. 1var", "2. var_1", "3. var-1", "4. var 1"], "answer": "2"},
    {"question": "What is the correct way to write a comment in Python?", 
     "options": ["1. # This is a comment", "2. // This is a comment", "3. /* This is a comment */", "4. <!-- This is a comment -->"], "answer": "1"},
    {"question": "What is the result of the expression '5' + '3' in Python?", 
     "options": ["1. 8", "2. '53'", "3. '5' + '3'", "4. Error"], "answer": "2"}
]

leaderboard = []

def ask_question(q):
    print(f"Question: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (1/2/3/4): ")
    return answer == q['answer']

def run_quiz():
    random.shuffle(questions)
    score = 0
    for q in questions[:5]:
        print("\nNext Question:")
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
        time.sleep(1)
    print(f"\nQuiz Over! Your score: {score}")
    leaderboard.append(score)
    return score

def main():
    print("Welcome to the Python Quiz!")
    while True:
        score = run_quiz()
        print(f"Your final score is: {score}")
        print("\nLeaderboard for this session:")
        for i, score in enumerate(leaderboard, 1):
            print(f"{i}. {score}")
        retry = input("\nWould you like to play again? (yes/no): ").lower()
        if retry != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
