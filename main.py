# Simple Online Examination System (Console Based)

# Questions (Question, Options, Correct Answer)
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. All"],
        "answer": "D"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

# Login Function
def login():
    print("--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login Successful!\n")
        return True
    else:
        print("Invalid login!\n")
        return False

# Exam Function
def start_exam():
    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            score += 1
        print()

    return score

# Result Function
def show_result(score, total):
    print("--- Result ---")
    print(f"Your Score: {score}/{total}")

    if score >= total / 2:
        print("Status: PASS")
    else:
        print("Status: FAIL")

# Main Program
if login():
    total_questions = len(questions)
    score = start_exam()
    show_result(score, total_questions)
else:
    print("Exiting program...")
