import json

with open('questions.json') as f:
    content = f.read()

data = json.loads(content)
score = 0
for question in data:
    print(question['question_text'])
    for index, answer in enumerate(question['alternatives']):
        print(index + 1, "-", answer)
    user_choice = int(input("Enter your answer: "))
    question['user_choice'] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1

for index, question in enumerate(data):
    print(f"Question {index + 1}, Your answer: {question['user_choice']}, " \
          f"Correct answer: {question['correct_answer']}")

print(f"Your score is: {score} of {len(data)}.")
