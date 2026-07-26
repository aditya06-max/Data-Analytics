def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"],
            "answer": "B) Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B) Mars"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D) Pacific Ocean"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"],
            "answer": "A) William Shakespeare"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Ag", "B) Au", "C) Fe", "D) Hg"],
            "answer": "B) Au"
        },
        {
            "question": "Which country is home to the kangaroo?",
            "options": ["A) South Africa", "B) Canada", "C) Australia", "D) Brazil"],
            "answer": "C) Australia"
        },
        {
            "question": "How many bones are there in an adult human body?",
            "options": ["A) 106", "B) 206", "C) 306", "D) 406"],
            "answer": "B) 206"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["A) Helium", "B) Oxygen", "C) Hydrogen", "D) Carbon"],
            "answer": "C) Hydrogen"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
            "answer": "C) Diamond"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["A) 1912", "B) 1905", "C) 1920", "D) 1898"],
            "answer": "A) 1912"
        },
        {
            "question": "What is the main gas found in the air we breathe?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "C) Nitrogen"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"\nQ{index + 1}: {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"][0]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}\n")

    print("=" * 40)
    print(f"🎉 Your final score is {score}/{len(questions)}")
    print("=" * 40)


run_quiz()

# f stands for "Formatted String" (also called an f-string).
#
# It lets us insert variables or expressions directly inside a string
# by writing them inside curly braces {}.
#
# Syntax:
# f"Text {variable}"
#
# Example:
# name = "Aditya"
# print(f"Hello {name}")
#
# Output:
# Hello Aditya
#
# Without 'f':
# print("Hello {name}")
#
# Output:
# Hello {name}
#
# Why?
# Without 'f', Python treats everything inside the quotes as plain text.
# With 'f', Python looks inside {} and replaces the variable with its value.
#
# We can also perform calculations inside {}.
#
# Example:
# age = 22
# print(f"Next year I will be {age + 1} years old.")
#
# Output:
# Next year I will be 23 years old.

# enumerate() is used when we need BOTH:
# 1. The index (position number)
# 2. The value (actual item)
#
# Syntax:
# for index, item in enumerate(list_name):
#
# Example:
#
# fruits = ["Apple", "Banana", "Orange"]
#
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
#
# Output:
# 0 Apple
# 1 Banana
# 2 Orange
#
# 'index' stores the position number.
# 'item' (or any variable name) stores the actual value.
#
# In this quiz:
#
# for index, q in enumerate(questions):
#
# index = Question number starting from 0
# q = One dictionary (one complete question)
#
# First iteration:
# index = 0
# q = First question
#
# Second iteration:
# index = 1
# q = Second question
#
# Since humans count from 1 instead of 0,
# we print:
#
# index + 1
#
# So the output becomes:
# Q1
# Q2
# Q3
# instead of
# Q0
# Q1
# Q2