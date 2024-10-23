import json

with open("txt_files/questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"] + "? ")
    for index, option in enumerate(question["alternatives"]):
        print(index + 1, "-", option)
    user_answer = int(input("Enter your answer: "))
    if user_answer == question["correct_answer"]:
        score += 1

print(f"\nCorrect answers: {score}/{len(data)}")

# for question in data:
#     message = f"{question}"
