print("Welcome to my quiz game!!\n")

# Questions with correct answers
question_bank = [
    {
        "text": "The ability of one class to acquire methods and attributes of another class is called?",
        "answer": "A"
    },
    {
        "text": "A function defined inside a class is called?",
        "answer": "B"
    },
    {
        "text": "The process of hiding internal details and showing only necessary features is called?",
        "answer": "D"
    },
    {
        "text": "The concept where the same function name behaves differently based on context is called?",
        "answer": "C"
    },
    {
        "text": "The blueprint or template from which objects are created is known as?",
        "answer": "B"
    }
]

# Corresponding options for each question
options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Object"],
    ["A. Object", "B. Method", "C. Function", "D. Variable"],
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Method"],
    ["A. Object", "B. Class", "C. Constructor", "D. Function"]
]
score=0

def check_answer(user_guess,correst_answer):
    if user_guess==correst_answer:
        return True
    else:
        return False
    
for question_num in range(len(question_bank)):#0.1.2.3.4
    print("********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print([i])
        
    guess=input("enter your answer(A/B/C/D:)").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("correct Answer")
        score+=1
    else:
        print(" IN correct Answer")
        print(f" the correct answer s {question_bank[question_num]["answer"]}")
    print(f" ypour Current score is { score}/{question_num+1}")
print(f" your Final score is {score}")
print(f"your score is {(score /len(question_bank))*100}%")

        