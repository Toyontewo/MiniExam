import random
from question_data import question_data
score = 0
index = 0
print("Welcome to Afe Babalola exam portal")
name = input("Enter your username: ")
matric_number = int(input("Enter Matric number: "))
test_on = True

decide = input("Enter 'p' to Proceed to start the exam \nOr 'q' to quit \n").lower()
if decide == "p":
    # while test_on:
    for _ in range(15):
        q_question = random.choice(question_data)
        question = (q_question['question'])
        answer = (q_question['answer'])

        index += 1
        print(f"{index}). {question}")
        input_answer = int(input("Answer? "))
        if input_answer == answer:
            score += 1
        # print(f"Your score is {score}")
    print(f"{name}, {matric_number}")
    print(f"Your total score is {score}")
else:
    print("Exam Ended")



# generate random question from the dictionary


# # Add index to the question

# Ask user for an input to give to answer


# Check is answer is correct

# Print next question


